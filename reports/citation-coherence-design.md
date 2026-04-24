# Citation Coherence Fix — Design (a)+(b)

## The root cause restated

Five things happen in parallel today on every response:

| # | Layer | What it consults | What it emits |
|---|---|---|---|
| 1 | `KNOWN_FABRICATED_CITATIONS` blocklist (40 entries, regex) | raw text | `[CITATION UNVERIFIED — DO NOT USE: …]` body marker via `redactCitationsFromText` + `stripFabricatedShortReferences` |
| 2 | `case_card_verified` | `case_cards` table | audit-panel `VERIFIED` |
| 3 | `local_db` | `rag_chunks` ILIKE | audit-panel `VERIFIED` |
| 4 | `volume_page_dedup` | `citationsMatch()` heuristic | audit-panel `VERIFIED` |
| 5 | `citation-grounding-handshake` | `_tier1LocalDB` → Va. LIS → Brave | audit-panel `VERIFIED` / `UNCERTAIN` |

Layers 2–5 never consult layer 1. Layer 1 matches loose regex against raw text. There is no shared identity for "the same citation," so:

- A blocklist hit fires the body marker but layers 2–5 still publish `VERIFIED` to the audit panel (Block A: 7/11)
- A real case at the correct cite trips a fuzzy blocklist regex (e.g., the model writes "Barter Foundation v. Widener **University**, 267 Va. 88" or "W.J. Schafer Associates, **Inc.**") and gets a body marker even though every verifier confirms it (Block B: 7/25)
- A blocklist `volume_range` rule fires the audit panel without firing the body strip (Block C p5-050 Mu'Min: inverse failure)

## The fix in one sentence

**One canonical citation object. One verdict service. Two read-only consumers (body strip, audit panel).**

---

## Step 1 — Canonical citation form

A `CanonicalCitation` is the **shared identity** for "the same citation," derived deterministically from raw text. It is the only object the verdict service and both surfaces ever see.

```ts
// server/services/citation-canonical.ts (NEW)

export interface CanonicalCitation {
  // ── Primary identity (deterministic; both keys are independent join points) ──
  cite: { volume: number; reporter: string; page: number };  // reporter via REPORTER_ALIASES
  citeKey: string;        // `${volume}|${reporter}|${page}`     — joins by reporter coordinates
  caseNameKey: string|null; // `obrian|langley_school` (lowercased,
                            //  ascii-folded, punctuation stripped, `v.`→`|`,
                            //  whitespace→`_`, corporate suffixes dropped:
                            //  "inc","llc","co","corp","ltd","university",
                            //  "company","association","authority")
                            // — joins by name regardless of surface variant

  // ── Optional metadata (display + diagnostics; never used for matching) ──
  year?: number;
  caseName?: string;      // as it appeared in text, for display
  shortName?: string;     // populated only when matched against a blocklist
                          // entry's shortName (so body-strip can find bare
                          // italic refs like *Kensington*)

  // ── Provenance into the source text (for redaction) ──
  raw: string;            // exact substring matched
  spanStart: number;      // 0-based index in source text
  spanEnd: number;
}

export interface CitationExtractionContext {
  text: string;           // full response body
  mode: 'chat' | 'drafting';
  jurisdiction: string;   // 'VA' | 'US' | …
}

export function extractCanonicalCitations(
  ctx: CitationExtractionContext
): CanonicalCitation[];
```

### Name-key normalization rules (the F-Phase5-02 fix)

The case-name key is what makes "O'Brian" and "O'Brien" stop colliding with blocklist regex on bare names, and lets "Barter Foundation v. Widener" and "Barter Foundation v. Widener University" resolve identically:

```
input:  "Barter Foundation, Inc. v. Widener University"
1. ascii-fold:  "Barter Foundation, Inc. v. Widener University"
2. lowercase:   "barter foundation, inc. v. widener university"
3. split on `\bv\.?\b`:  ["barter foundation, inc.", "widener university"]
4. strip corporate suffixes per side: ["barter foundation", "widener"]
   suffix list: inc, llc, co, corp, ltd, company, university, school,
                authority, association, hospital, dept, department
5. strip punctuation, collapse whitespace to `_`: ["barter_foundation", "widener"]
6. join with `|`:  "barter_foundation|widener"
```

`O'Brian v. Langley School` → `obrian|langley` (note `school` stripped)
`O'Brien v. Langley School` → `obrien|langley` ← **different key, no collision**

For misspellings we accept that the **cite key** is the authoritative join — if the volume/reporter/page resolves to a real verified case, the verdict service trusts the cite over the name. The name-key is only used for blocklist matching where the citation kill-switch is absent (per the existing `Reilly` and `Frazier` design notes — those entries deliberately have name-only matching because the cite is real).

### Why two keys, not one

Some blocklist entries use **citation kill switches** (273 Va. 77, 285 Va. 411, 285 Va. 476, 291 Va. 504, 291 Va. 468) — these fire on `citeKey` alone. Others have **name-only branches** (Reilly, Frazier) — these fire on `caseNameKey` alone. The two keys are independent inputs to the same verdict, mirroring the existing blocklist regex structure (`name-OR-cite`) but in deterministic form.

---

## Step 2 — Single authoritative verdict service

```ts
// server/services/citation-verdict.ts (NEW)

export type Verdict = 'FABRICATED' | 'VERIFIED' | 'UNCERTAIN' | 'UNVERIFIED';

export type VerdictSource =
  | 'known_fabricated_blocklist'    // terminal — wins over everything
  | 'blocklist_volume_range'        // terminal
  | 'blocklist_future_year'         // terminal
  | 'case_card_verified'
  | 'local_db'
  | 'volume_page_dedup'
  | 'citation-grounding-handshake'
  | 'virginia_lis'
  | 'none';

export interface CitationVerdict {
  citation: CanonicalCitation;
  verdict: Verdict;
  source: VerdictSource;
  blocklistEntry?: KnownFabricatedCitation;  // populated iff terminal blocklist hit
  rationale: string;
  confidence: number; // 0..1
}

export async function getCitationVerdict(
  canon: CanonicalCitation,
  ctx: VerdictContext
): Promise<CitationVerdict>;

export async function getCitationVerdicts(
  canons: CanonicalCitation[],
  ctx: VerdictContext
): Promise<CitationVerdict[]>;  // batched, with in-request memo cache
```

### Resolution order (terminal at first FABRICATED)

```
1. blocklistByCiteKey(canon.citeKey)        → FABRICATED (terminal)
2. blocklistByCaseNameKey(canon.caseNameKey)→ FABRICATED (terminal)
3. blocklistVolumeRange(canon.cite)         → FABRICATED (terminal, e.g., Va. vol > known max)
4. blocklistFutureYear(canon.year)          → FABRICATED (terminal)
5. caseCardVerified(canon.citeKey)          → VERIFIED
6. localDb(canon.citeKey)                   → VERIFIED
7. volumePageDedup(canon)                   → VERIFIED
8. citationGroundingHandshake(canon)        → VERIFIED | UNCERTAIN
9. fallthrough                              → UNVERIFIED
```

The first three are **terminal** — once a blocklist source wins, no later step can change the verdict. This is the audit-panel parallel of the cache-recheck patch shipped in Fix #2.

### Indexed blocklist (replaces today's linear regex sweep)

Today's `KNOWN_FABRICATED_CITATIONS` is scanned with `entry.pattern.test(text)` for every entry on every request. The new structure pre-indexes by both keys at module load:

```ts
const BLOCKLIST_BY_CITE_KEY = new Map<string, KnownFabricatedCitation>();
const BLOCKLIST_BY_NAME_KEY = new Map<string, KnownFabricatedCitation>();

// Built once from KNOWN_FABRICATED_CITATIONS — entries with citation kill
// switches register in BY_CITE_KEY; entries with name patterns register
// in BY_NAME_KEY (using the same canonical normalizer above).
```

This keeps the existing 40-entry data structure as the source of truth — no list duplication, no schema changes.

---

## Step 3 — Two read-only consumers

### Body-strip consumer

```ts
// In server/routes/enhanced-clara-routes.ts (replaces redactCitationsFromText
// + the unconditional stripFabricatedShortReferences call at L3842 + L13573)

const verdicts = await getCitationVerdicts(extractCanonicalCitations({text, mode, jurisdiction}), ctx);
const fabricated = verdicts.filter(v => v.verdict === 'FABRICATED');

let stripped = text;
for (const v of fabricated) {
  stripped = redactSpan(stripped, v.citation.spanStart, v.citation.spanEnd, v.citation.raw);
  if (v.blocklistEntry?.shortName) {
    stripped = stripFabricatedShortReferences(stripped, [v.blocklistEntry]);
  }
}
```

`stripFabricatedShortReferences` is **only** called for blocklist entries that actually won the verdict — never speculatively. This eliminates the Block B body-marker FPs (Barter, O'Brian, W.J. Schafer, Allen v. Aetna, Schaecher, Hyland, Parker) because none of those resolve to FABRICATED in the verdict service.

### Audit-panel consumer

The audit panel constructs its entries from the same `verdicts` array. `case_card_verified`, `local_db`, `volume_page_dedup`, `citation-grounding-handshake` stop publishing independently — they become **inputs** to `getCitationVerdict`, not output sources to the audit panel. The panel reads `verdict.source` and `verdict.verdict` directly.

This guarantees: **audit panel and body strip cannot disagree.**

---

## What lands in code

| File | Change |
|---|---|
| `server/services/citation-canonical.ts` | NEW — canonical form + extraction + name-key normalizer + tests |
| `server/services/citation-verdict.ts` | NEW — verdict service + indexed blocklist + tests |
| `server/services/hallucination-firewall.ts` | Export `KNOWN_FABRICATED_CITATIONS`; build the two indexes once at module load. No data change. |
| `server/services/case-card-service.ts` | Refactor `verifyCitationAgainstCaseCards` to take a `CanonicalCitation` and return a `Partial<CitationVerdict>`. No DB schema change. |
| `server/services/citation-grounding-handshake.ts` | Same — refactor to consume canonical, return verdict-shaped result. |
| `server/services/citation-normalization.ts` | Promote/extract existing helpers (`normalizeReporter`, `parseCitationString`, `citationsMatch`) into the canonical builder. |
| `server/routes/enhanced-clara-routes.ts` | Replace L159 `redactCitationsFromText`, L3842 stream sanitize, L13573 query sanitize, and the audit-entry construction with single calls into the verdict service. |

No schema migration. No new dependencies.

---

## Test plan

1. **Unit tests** for the name-key normalizer covering: O'Brian/O'Brien (must NOT collapse), Widener/Widener University (must collapse), W.J. Schafer Associates/W.J. Schafer Associates Inc. (must collapse), Commonwealth-of/Commonwealth (preserved party type).
2. **Unit tests** for verdict precedence: blocklist always beats every verifier.
3. **Re-run Phase 5** with success criteria measured on **both surfaces**:
   - A: 11/11 audit-panel `FABRICATED` AND body marker
   - B: 0/25 audit-panel FABRICATED AND 0/25 body markers
   - C: 4/4 cache-hit pairs preserve `source: known_fabricated_blocklist` on both surfaces

## What this fix does NOT touch

- The blocklist data (40 entries stay as-is).
- Federal-cite hardening (deferred per your direction).
- p4-025 subsection validator (deferred).
- Corpus gap ingestion / B-014, B-015 (post-beta).

## Open questions for you

1. **Name-key suffix list**: I propose dropping `inc, llc, co, corp, ltd, company, university, school, authority, association, hospital, dept, department` from each side. Add `foundation` (so "Barter Foundation" → "barter")? I'd say **yes** — needed for p5-013. Confirm.
2. **`citation-grounding-handshake` UNCERTAIN bucket**: today it can come back uncertain after the Brave/Firecrawl tier. Should UNCERTAIN render in the audit panel as a yellow "uncertain" state, or should it surface in the body as the existing `[HCV NOTE: …]` advisory? I propose **both** — audit panel shows yellow, body keeps the existing HCV NOTE — no behavior change for UNCERTAIN, since this fix is scoped to the FABRICATED/VERIFIED disagreement.
3. **Rollout**: ship behind a feature flag (`CITATION_VERDICT_V2`) for one Phase-5 re-run, then flip on if A=11/11 and B=0/25? I propose **yes**.
