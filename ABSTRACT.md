# CLARA Hallucination Audit — Five-Phase 374-Query Study

**A registered report of completed work**

---

## Project at a glance

CLARA is a Virginia-specific legal AI assistant built around a multi-layer hallucination firewall. This project archives a five-phase find-and-fix audit conducted April 19–20, 2026, in which 350 main-phase prompts (plus 24 supplementary edge-case probes, for 374 total bundle rows) were run against three arms in parallel — CLARA post-fix, CLARA pre-correction, and a bare-LLM baseline — with attorney coders verifying every emitted citation against four criteria (existence, caption accuracy, holding coherence, temporal validity). The bundle freezes the consolidated dataset, the per-phase reports, the prompt files for replay, the hand-coding rubric, and the architectural-fix log on a timestamped surface.

The intent is a registered report of completed work: the methodology and the numbers are immutable from this point forward. For the methodology-first companion (200 queries, single-shot, pre-stated κ ≥ 0.70 threshold, no remediation), see the v2 bundle.

---

## Headline result

| Metric                                                                | Value     |
|-----------------------------------------------------------------------|----------:|
| Total prompts in bundle (5 phases + 2 supplementary batches)          | 374       |
| Main-phase prompts driving the headline rate                          | 350       |
| Total citations evaluated (Phases 1–4)                                | 2,576     |
| Confirmed fabrications (Phases 1–4)                                   | 11        |
| **Per-citation hallucination rate (post-firewall)**                   | **0.43%** |
| Per-response rate (initial emission, pre-redaction, Phases 1–3)       | ~3.6%     |
| Phase 5 V2 forced-emission regression bucket                          | 11/11 emission; 9/9 phantom guards fired correctly |
| Real-case false positives detected and corpus-closed same-cycle       | 5         |
| Architectural fixes shipped this cycle                                | 5         |
| `KNOWN_FABRICATED_CITATIONS` total entries (post-cycle)               | ~48       |
| Unit-test coverage on the new CGH Blocklist Guard (Fix #5)            | 30/30 green |

`RESULTS.md` is the canonical numbers document. Anything in this abstract that disagrees with `RESULTS.md` is in error.

---

## Methodology in one paragraph

Five sequential phases — Phase 1 anchored baseline (30 queries), Phase 2 non-anchored (120), Phase 3 adversarial (100), Phase 4 confirmation (50), Phase 5 V2 full run plus regression bucket (50 + 11) — with two supplementary edge-case batches (15 + 9). Three arms per prompt: CLARA at the post-Fix-5 commit, CLARA with the inline-redaction layer disabled, and a bare LLM baseline (Claude Sonnet 4.5, temperature 1.0, no firewall). Attorney coders verified every emitted citation against existence, caption accuracy, holding coherence, and temporal validity, using the eight-code taxonomy in `taxonomy/taxonomy.md`. Iterative remediation between phases — blocklist additions, regex fixes, corpus closures, and architectural fixes — is part of the design and disclosed in `METHODOLOGY.md` §1.2 and §2.4. The full firewall layer-by-layer accountability is in `reports/firewall-effectiveness.clara-2026-04-21.md`.

---

## What this audit is *not*

- **Not** a preregistration. Results are already known and published in `RESULTS.md`. The companion v2 200-query bundle is the methodology-first preregistration.
- **Not** a single-shot benchmark. Five architectural fixes (Fix #1 – Fix #5) and ~14 net-new blocklist regex patterns shipped during the audit window. The 0.43% number is CLARA *as fixed during the cycle*; a re-run against an older commit will produce a higher number.
- **Not** apples-to-apples comparable to Stanford HAI/RegLab 2024 without the per-citation vs. per-response caveat that `RESULTS.md` makes explicit. Both studies are valid; the methodology axis differs and we say so on the page.
- **Not** automated. Verdicts are human; no LLM-as-judge.
- **Not** blind. Coders are CLARA team attorneys or attorney-supervised analysts. The audit is a step toward fully independent third-party evaluation, not the destination.

---

## Two-sided audit outcome

A defense-in-depth firewall risks over-firing on real cases. The Phase 5 V2 50-prompt run intentionally inspected for this and surfaced **five real-case false positives** that the firewall was incorrectly wrapping with `[CITATION UNVERIFIED — DO NOT USE]` markers due to corpus gaps. All five were verified against CourtListener V4, ingested via the D2 protocol with verbatim opinion passages and miscitation guards, and closed in the same cycle:

- *Rascher v. Friend*, 279 Va. 370 (2010) — contributory negligence / proper lookout
- *W.J. Schafer Associates, Inc. v. Cordant, Inc.*, 254 Va. 514 (1997) — UCC teaming agreement
- *Yeatts v. Commonwealth*, 242 Va. 121 (1991) — capital murder / future-dangerousness
- *Muhammad v. Commonwealth*, 269 Va. 451 (2005) — DC sniper convictions affirmed
- *J.B. Moore Electrical Contractor, Inc. v. Westinghouse Electric Supply Co.*, 221 Va. 745 (1981) — UCC battle-of-forms

The fact that the audit caught and closed errors in **both directions** — phantom under-blocking and real-case over-blocking — is itself an outcome of the audit's two-sided design and is reported as such.

---

## Open carry-forward (post-beta)

- **Audit-panel single-verdict rewire** (broader Fix #3 scope). The Phase 5 V2 forced-emission regression bucket reproduces the inverse-coherence failure (Finding F-1) on real, fully-corpus-verified cases. Fix #5 closed the dangerous half (phantom verified in panel); the broader rewire closes the UX-confusing half (real case redacted in body while panel says VERIFIED). Three-day focused refactor, with the V2 canary bucket as the regression test. Empirically validated as next required work.
- **Cohen's κ inter-rater reliability** for hand-coding was not formally computed for this 374-query audit. It is the registered acceptance threshold (κ ≥ 0.70) for the v2 200-query preregistration.
- **Re-run at temperature 0 and temperature 0.7** to bracket the LLM-noise component of 0.43%. Open. Strengthens defensibility against academic scrutiny.
- **Engage Stanford RegLab or comparable group** for a third-party benchmark on the 2024 prompt set. Open.

---

## Where to find what

| Artifact                                                          | Location |
|-------------------------------------------------------------------|---|
| Canonical results (v3.0 corrected report)                         | `RESULTS.md` |
| Phase design, three-arm structure, coding procedure, threats      | `METHODOLOGY.md` |
| Hit-code definitions and severity weights                         | `taxonomy/taxonomy.md` |
| Frozen 374-prompt × 3-arm CSV                                     | `data/clara-audit-dataset-374queries.csv` |
| Per-phase prompt files (replay against any pinned CLARA commit)   | `prompts/*.jsonl` |
| Consolidator that built the CSV                                    | `build/build-dataset-csv.py` |
| Per-phase reports, firewall-effectiveness analysis, coding sheets | `reports/` |
| Live mirror                                                       | _GitHub repo URL — added at registration_ |

---

**Bundle version:** 1.0.0 · **Audit closure date:** April 20, 2026 · **License:** MIT (code) + CC-BY-4.0 (data, prompts, reports, taxonomy, docs)
