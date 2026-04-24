# BUG: Va. Code NOT_FOUND citations bypass all stream-time redaction

**Severity:** High (citation-accuracy regression on Va. Code dimension)
**Filed:** 2026-04-21
**Source:** Per-cite survival analysis, run_id=`clara-2026-04-21`
**Empirical evidence:** `tests/hallucination-audit/reports/cite-survival.clara-2026-04-21.md`

## Summary

CLARA's hallucination firewall removes **3.6% of verified Va. Code statutes** but
**0% of NOT_FOUND Va. Code statutes** (0 of 34) from the stream-time response
text. On the Va. Code dimension the post-generation pipeline is producing pure
collateral damage — removing real, in-corpus statutes while never flagging or
redacting suspect ones.

The case-citation pipeline does not have this problem: NOT_FOUND case cites are
dropped at 15.9% vs verified case cites at 10.5% (a 5.4pp lift, with collateral
damage but at least directionally correct).

## Evidence

From `cite-survival.clara-2026-04-21.md`, scoping to the 195 prompts where
`preCorrectionText ≠ responseText`:

| Kind | Verification status | Pre cites | Dropped | Survived | Drop rate |
|---|---|---:|---:|---:|---:|
| case | NOT_FOUND | 389 | 62 | 327 | 15.9% |
| case | VERIFIED_CASE | 105 | 11 | 94 | 10.5% |
| **va_code** | **NOT_FOUND** | **34** | **0** | **34** | **0.0%** |
| **va_code** | **VERIFIED_STATUTE** | **389** | **14** | **375** | **3.6%** |

The expected ordering (NF drop > VERIFIED drop) is inverted on the Va. Code row.

## Root cause

`server/services/hallucination-firewall.ts` Phase 2.6 (~line 1823) runs the
`VaCodeValidator.validateAllStatuteCitations(text)` over every Va. Code citation
in the response and partitions results into three buckets:

- **`valid`** — section exists in `va_statutes` corpus (or differs only by a
  trailing letter suffix from a section that does) → pass through (correct)
- **`invalid`** — covers two sub-cases, both emit `**NONEXISTENT STATUTE
  WARNING**` advisory appended to `processedText` (correct):
  1. **Nonexistent title prefix** — the Title prefix (e.g. `99.99-`) does not
     exist anywhere in the Virginia Code corpus.
  2. **Phantom decimal suffix** ([T004] path) — the base section exists
     (e.g. `8.01-243`) but the `.N` suffixed variant (e.g. `8.01-243.99`) does
     not. The earlier prefix-strip-and-accept fallback used to silently treat
     these as valid; the validator now correctly classifies them as invalid.
- **`unverified`** — title prefix exists AND there is no decimal-suffix base
  to strip, but the specific section is not found in the 32,216-row
  `va_statutes` corpus → **`console.log` only; no advisory, no redaction,
  no user-visible signal**

The `unverified` bucket is precisely the H1_FAB_CITE pattern for Va. Code: a
plausible-looking section number invented within a real Title (e.g. fake
`§ 8.01-229.1` invented within real Title 8.01). The firewall recognizes
these as suspect (logs them) but discards the signal.

Concretely:

```
// hallucination-firewall.ts ~line 1835
if (statuteValidation.unverified.length > 0) {
  console.log(`⚠️ [VaCodeValidator] ${statuteValidation.unverified.length} section(s) ` +
              `not in corpus but title exists (may be valid): ${statuteValidation.unverified.join(', ')}`);
}
```

Compare to the `invalid` branch immediately above it, which builds an advisory
that gets appended to `processedText` at line 2454.

## Why the verified-Va-Code drop rate is 3.6%

The 14 verified Va. Code cites that *do* get removed are collateral damage
from three other firewalls that correctly redact sentences containing wrong
propositions/quotes/section-content about real statutes:

- `redactStatutePropositionViolations` (statute-proposition-firewall.ts)
- `redactSectionContentViolations` (section-content-coherence.ts)
- `redactStatuteQuoteViolations` (statute-quote-provenance.ts)

These three behave correctly: when CLARA cites a real statute and asserts
something untrue about it, the entire offending sentence is redacted, which
removes the (correct) cite along with the (incorrect) holding. That's intended
"holding goes with the cite" behavior, not the bug.

The bug is the gap: there is no equivalent of the case-NOT_FOUND
`redactCitationsFromText` path for Va. Code NOT_FOUND citations.

## Fix

Mirror the existing `fabricatedStatuteWarnings` flow for the `unverified`
bucket, with softer language to distinguish from confirmed-fabricated sections.
Specifically:

1. Build a parallel `unverifiedStatuteWarnings` array in the Phase 2.6 block
   (~line 1835).
2. Append it to `processedText` at the same spot where
   `fabricatedStatuteWarnings` is appended (~line 2454).
3. Cap at a reasonable number of distinct sections (suggest 8) to prevent
   spam in worst-case responses.
4. Use language like:
   `"⚠️ UNVERIFIED STATUTE: Va. Code § X.X-XXX — this section was not found
     in CLARA's verified Virginia Code corpus. The Title prefix is valid,
     but the section may be unindexed, repealed, renumbered, or fabricated.
     Verify against law.lis.virginia.gov before relying on this citation."`

The "softer than NONEXISTENT" framing is honest because we cannot prove
non-existence — the corpus may be incomplete. Surfacing the uncertainty to
the user is strictly better than silently passing through.

## Verification plan

After the fix:

1. Re-run the audit against a small subset (Phase 5 + edge_cases_v2_regression,
   ~50 prompts) to confirm `responseText` now contains UNVERIFIED-statute
   advisories where appropriate.
2. Re-run cite-survival analysis on that subset; the va_code NOT_FOUND drop
   rate should now be > 0 (advisories may technically not "drop" the cite
   from the text, but should at minimum surface alongside it — alternatively,
   we may want a redaction option in v2).
3. Confirm no regression on case-cite drop rates (they are produced by
   different code paths).

## Out of scope for this fix

- Bringing the verified-Va-Code drop rate down (3.6%) — that requires
  refining the proposition/section-content/quote firewalls to redact only
  the offending phrase, not the surrounding cite. Separate ticket.
- Bringing the verified-case drop rate down (10.5%) — same reason.
- The bridge-level case-NOT_FOUND drop rate of 15.9% can be improved by
  hand-coding (which cites in this bucket are real-but-uncurated vs truly
  fabricated). Separate workstream — that's the publication path, not an
  engineering fix.
