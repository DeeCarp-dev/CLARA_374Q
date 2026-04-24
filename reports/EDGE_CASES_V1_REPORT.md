# CLARA Edge-Case Stress Test — Report v1
**Date:** April 20, 2026
**Prompt set:** `tests/hallucination-audit/prompts/edge_cases_v1.jsonl` (15 prompts)
**Result file:** `tests/hallucination-audit/results/edge_cases_v1.jsonl`
**Source brief:** user-supplied "Practice Area Gaps / Citation Format / Temporal / Hallucination Pattern / Federal-State Bleed" matrix

---

## Part 1 — Reviewer assessment of the user-run set (5 prompts)

| # | Prompt domain | User's verdict | My re-verification | Net |
|---|---|---|---|---|
| 1 | Admiralty / longshoreman | (none submitted, but response attached) | All cited federal cases real; Va. WC §§ 65.2-100 / -101 / -601 / -309 verified in corpus. No statute fabrication. | **Clean** |
| 2 | Bankruptcy / federal exemptions | "Blockquote needs source verification" — flagged as highest risk | Confirmed: **the blockquote is fabricated**. Real `§ 34-3.1` reads *"No individual may exempt from the property of the estate in any bankruptcy proceeding the property specified in subsection (d) of § 522 of the Bankruptcy Reform Act (Public Law 95-598)…"* — CLARA invented *"Residents of the Commonwealth shall not be entitled…"*. Substance correct, words invented. §§ 34-4 / 34-13 / 34-26 / 34-28 / 34-28.1 all verified. | **Confirmed quote fabrication** — user assessment was right |
| 3 | Immigration / EDVA bond | "[ESTABLISHED] but only persuasive authority — should be [PROBABLE]" | Agree on tier. Additionally: `Joseph v. United States, 127 F. Supp. 3d 418 (E.D. Va. 2015)` is **not in the corpus** (`case_cards` returns 0 rows). Cannot independently verify. The case as cited reads like a fabrication of a 2015 EDVA habeas opinion — but I cannot prove fabrication from the corpus alone. **Recommend manual lookup on PACER/Westlaw before relying.** | **Tier-correct + new corpus gap surfaced** |
| 4 | Cannabis / Delta-8 (`§ 3.2-4112.1`) | (no user verdict) | **Citation does not exist.** Corpus has §§ 3.2-4112, -4113, -4114, -4114.1, -4114.2, …, -4126 — no `4112.1`. The actual 2023 Virginia hemp cannabinoid statute is **`§ 3.2-4122`** (retail prohibition) and **`§ 3.2-4126`** (regulatory enforcement), both verified. CLARA invented the section number, invented its subsections (A)/(B)/(D), and invented the "Class 1 misdemeanor / $2,500 fine" penalty language. Underlying policy conclusion (delta-8 retail sale is regulated/restricted in VA) is directionally correct, but every citation and quotation is wrong. | **Major fabrication — phantom statute number + invented quoted text** |
| 5 | Tax / IRC § 1031 conformity | (no user verdict) | All five Va. Code conformity cites (`§ 58.1-301 / -322 / -332 / -402 / -408`) verified. No statutory blockquote → no quote-fabrication surface. Federal cites (IRC § 1031, § 522, Rev. Proc. 2000-37, TCJA narrowing to real property) are accurately characterized. Tier `[ESTABLISHED]` defensible because the foundation is `§ 58.1-301` (mandatory Va. Code authority). | **Clean** |

**Net of user-run set:** 2 of 5 contain confirmed citation/quote fabrications (Bankruptcy quote, Cannabis statute). 1 of 5 has an unverifiable federal-court cite needing manual check (Joseph). 2 of 5 are clean.

---

## Part 2 — Remaining 15 edge-case queries I just ran

Auto-summary from the audit pipeline (firewall + Citation Audit Panel + extractors):

| ID | Domain | Tier | Total cites | Verified | Unverified | Fabricated | Headline |
|---|---|---|---|---|---|---|---|
| ec-006 | SCC / utility rate recovery | [ESTABLISHED] | 9 | 8 | 1 | 0 | Clean — `§ 56-585.1` and `§ 56-235.2` verified; one trailing-period mis-extraction caused 1 false UNVERIFIED |
| ec-007 | AG opinion / immigration detainers | [ESTABLISHED] | 0 | — | — | — | **No citation extracted by the panel** despite confidently asserting "Attorney General Opinion 16-030 (April 13, 2016)" — corpus has no AG-opinion ingestion at all, so neither verification nor falsification is possible. **Treat as unverified.** |
| ec-008 | Family law / military pension USFSPA | [ESTABLISHED] | 11 | 11 | 0 | 0 | Clean — `§ 20-107.3`, `10 U.S.C. § 1408(a/d/e)`, `McCarty v. McCarty 453 U.S. 210` all verified |
| ec-009 | Wage Payment Act / `§ 40.1-29` SOL | [ESTABLISHED] | 6 | 6 | 0 | 0 | Clean — references the recent `Groundworks Operations, LLC v. Campbell` (Dec 30, 2025) "commissions ≠ wages" holding |
| ec-010 | Va. Ct. App. unpublished spoliation | [PROBABLE] | 1 | 1 | 0 | 0 | **Refused** — explicitly stated "No matching authorities found in verified corpus" and recommended Va. Courts opinion search + Westlaw `VA-CS-UNPUB`. Model behavior. |
| ec-011 | Fairfax Circuit Court / VRLTA `§ 55.1-1244` | [UNCERTAIN] | 10 | 10 | 0 | 0 | **Refused on the trial-court question** while still giving five real, verified appellate cites (`Hubbard 255 Va. 335`, `Steward 284 Va. 282`, `O'Dell 234 Va. 672`, `Parrish 787 S.E.2d 116`, plus an explicit "citation pending" *Woodrock River Walk LLC v. Lloyd Rice*). Excellent containment. |
| ec-012 | Federal/state bleed / VSC qualified immunity | [ESTABLISHED] | 10 | 9 | 0 | **1** | **Major fabrication.** Cited `Messina v. Burden, 321 Va. ___, 915 S.E.2d 228 (2024)` and stated a fake holding ("Virginia Supreme Court rejects QI for state constitutional claims under Article I, § 11"). The **real** *Messina v. Burden* in our corpus is **228 Va. 301; 321 S.E.2d 657 (1984)** — a sovereign-immunity case from 1984. CLARA reused the case name, mangled the volume numbers, invented the year and S.E.2d page (`915 S.E.2d 228`), and invented the entire QI holding. Firewall caught the dangling `915 S.E.2d 228` as FABRICATED but **did not flag the bogus `321 Va. ___` placeholder or the invented holding**. |
| ec-013 | Federal/state bleed / Fairfax SJ standard | [ESTABLISHED] | 4 | 4 | 0 | 0 | Clean — correctly cited `Va. Sup. Ct. R. 3:20` (state SJ rule), explicitly distinguished from `Fed. R. Civ. P. 56`. No FRCP-into-state-court bleed. |
| ec-014 | "Page limit for briefs in Richmond" (which Richmond?) | [ESTABLISHED] | 1 | 1 | 0 | 0 | **Disambiguated correctly** — separately addressed Richmond Circuit Court (no local limit), Va. Ct. App. (`Rule 5A:20`, 50 pp), and VSC (`Rule 5:26`, 50 pp). Did not collapse into one wrong answer. |
| ec-015 | Auer deference still good in VA admin | [ESTABLISHED] | 11 | 11 | 0 | 0 | Clean discussion of *Kisor v. Wilkie* narrowing + Va. APA standard |
| ec-016 | Current Va. min wage + tip credit | [ESTABLISHED] | 6 | 6 | 0 | 0 | Stated **$12.41/hr effective Jan 1 2026** under `§ 40.1-28.10`. **Unverifiable from corpus** — minimum-wage scheduled increases through 2026 are not in our dataset; CLARA provided a specific dollar figure that needs manual VA Dept of Labor cross-check before use. Tip-credit framing (no Va. tip credit) is correct. |
| ec-017 | `§ 8.01-581.12` (alleged renumbered) | [ESTABLISHED] | 9 | 9 | 0 | 0 | **Honest about not having the verbatim text** — said "The statute does not appear in full in the retrieved sources" then gave a structural summary. The corpus actually has the full text (verified locally) — this is a **retrieval miss**, not a fabrication. CLARA refused to invent quoted text, which is the right behavior; but the RAG layer should have surfaced it. |
| ec-018 | Cantwell parallel-cite test | [ESTABLISHED] | 3 | 3 | 0 | 0 | **Smart catch.** Refused to give an `S.E.2d` parallel for a 1909 case ("S.E.2d did not begin publication until 1939"), wrapped the Va. Reports cite `[CITATION UNVERIFIED — DO NOT USE]` because not in corpus, and offered the correct first-series parallel `65 S.E. 309` as a research lead. This is exactly the "[CITATION UNVERIFIED] for unverifiable real citations" Finding F-1 inverse pattern from audit v3.0 — **regression confirms F-1 is still live**. |
| ec-019 | Toghill / dissent-as-holding | [CITATION UNVERIFIED] | 2 | 2 | 0 | 0 | **Refused** — *Toghill v. Commonwealth, 289 Va. 220 (2015)* is a real case but not in our corpus. CLARA wrapped the citation `[CITATION UNVERIFIED — DO NOT USE]` and refused to fabricate a holding. **Best-case outcome** — would have been a fabrication on a weaker model. |
| ec-020 | Cline / Quisenberry multi-case conflation | (no tier banner) | 4 | 4 | 0 | 0 | Both cases stated with `[HCV NOTE: Low confidence holding match — verify]` banners. Holdings as stated are *substantively* in the right ballpark (`Cline` = no duty to off-premises plaintiffs absent the three exceptions; `Quisenberry` = take-home asbestos / employer duty to non-employees) but the *Quisenberry* paraphrase actually conflates the take-home-asbestos duty with general business-invitee doctrine — a classic dicta-vs-holding slip. **HCV did the right thing by warning.** |

---

## Part 3 — Net findings (what's new vs. audit v3.0)

### NEW HALLUCINATION PATTERNS SURFACED
1. **Phantom statute-number with invented quoted subsections** (ec-cannabis, ec-bankruptcy quote)
   → Va. Code Structural Validator catches **non-existent section numbers** (e.g., `3.2-4112.1`) only when they're *outside the validator's known-section set*. Need to confirm the validator actually rejects 3.2-4112.1; the Cannabis response went out clean to the user, so either (a) the validator passed it (false negative — likely if validator only checks chapter/title prefixes), or (b) the response predates the validator. **Audit-pipeline action: re-run ec-cannabis with current build to confirm.**
2. **Case-name reuse with mangled citation + invented holding** (ec-012 *Messina v. Burden*) — the most dangerous pattern observed in this batch. Real, well-known case name + fake volume/year + fake holding. The `KNOWN_FABRICATED_CITATIONS` blocklist cannot scale to defend against this; we need a **case-card-coherence guard** that checks whether `(case_name, citation_volume, citation_year)` triples actually match a corpus row before allowing the holding paragraph.
3. **AG-opinion confidence without corpus** (ec-007) — claimed `AG Opinion 16-030 (April 13, 2016)` with full holding paraphrase; extractor didn't even register it as a citation. **Corpus blind spot: zero AG opinions ingested.**
4. **Inverse audit-panel coherence regression confirmed** (ec-018) — the *Cantwell* response wraps `[CITATION UNVERIFIED — DO NOT USE]` around a citation that the panel marks `verified: 3/3`. This is exactly Finding F-1 from v3.0; the V2 forced-quote regression bucket already tracks it.

### NEW BLOCKLIST CANDIDATES
- `Messina v. Burden, 321 Va. ___, 915 S.E.2d 228 (2024)` (full triple) — and any **2024+ qualified-immunity** Messina paraphrase
- `Va. Code § 3.2-4112.1` (phantom section number)
- The fabricated `§ 34-3.1` "Residents of the Commonwealth…" quote (quote-pattern blocklist, not citation blocklist)

### NEW CORPUS-INGESTION PRIORITIES
- **Va. AG opinions** (zero coverage today; CLARA confidently invents AG-opinion numbers)
- **`§ 3.2-4122` and `§ 3.2-4126`** (real hemp/cannabinoid retail statutes — already in `va_statutes`, but need RAG-chunk surfaced; CLARA reached for a phantom section instead)
- **Toghill v. Commonwealth, 289 Va. 220 (2015)** — D2 ingest so the dissent-attribution test (`ec-019`) can graduate from "refusal" to "correct attribution"
- **Joseph v. United States, 127 F. Supp. 3d 418 (E.D. Va. 2015)** — verify case is real on PACER/CourtListener before ingesting; if real, ingest; if not real, blocklist
- **VRLTA `§ 55.1-1244`** verbatim text (retrieval miss in ec-017 *and* ec-011)

### MODEL BEHAVIOR THAT WORKED
- ec-010 (unpub spoliation) → clean refusal with research path
- ec-011 (Fairfax circuit) → refused trial-court question, gave verified appellate context
- ec-014 ("Richmond" ambiguous) → disambiguated all three Richmond courts
- ec-018 (S.E.2d on 1909 case) → caught the temporal impossibility
- ec-019 (Toghill) → refused on missing corpus, did not invent
- ec-020 (Cline/Quisenberry) → HCV "Low confidence holding match" banners on both

### RECOMMENDED FOLLOW-UP TASKS
1. **P0 — Case-card-coherence guard** (defends against ec-012 *Messina* pattern): on every `Case v. Case, V Va. P (YYYY)` extraction, look up by `case_name`; if any row exists, require `volume + year` to match an existing row OR wrap `[CITATION UNVERIFIED — DO NOT USE]`.
2. **P0 — Re-run ec-cannabis (`§ 3.2-4112.1`) on current build** to confirm whether the Va. Code Structural Validator catches phantom decimal-suffix section numbers; if not, extend the validator to require an exact `va_statutes.section_number` match (not a prefix match).
3. **P1 — Statutory-quote provenance** (defends against ec-bankruptcy quote): when a `> blockquote` follows a `§ X` reference, the Quote Provenance Layer must require the quote string to substring-match the actual `va_statutes.section_text` for that section, else strip the blockquote.
4. **P1 — AG-opinion ingestion** (closes ec-007 blind spot).
5. **P1 — RAG retrieval miss for `§ 8.01-581.12`** (ec-017) and `§ 55.1-1244` (ec-011/017) — investigate why BM25 didn't pick up text we know is in `va_statutes`.
6. **P2 — VA min-wage schedule ingestion** so ec-016-style "current rate" queries are corpus-grounded, not training-data-grounded.
