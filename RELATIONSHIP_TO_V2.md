# Relationship to the v2 200-Query Preregistration

This bundle (the **five-phase 374-query registered report**) is one of two CLARA hallucination-audit deposits on OSF. The other is the **v2 200-query preregistration** (`clara-audit-v2-200`). They are **complementary, not redundant**, and a reviewer who reads only one is missing half the picture.

This document explains how the two studies relate, what each one is designed to do that the other cannot, and why both are necessary.

---

## At a glance

| Dimension                       | This bundle (374-query)                                                       | v2 200-query bundle                                                     |
|---------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Type**                        | Registered report (post-hoc archival of completed work)                       | Preregistration (methodology-first)                                     |
| **Status**                      | Methodology and results both frozen                                           | Methodology frozen; results to come                                     |
| **Question answered**           | "What rate did CLARA produce during a five-phase find-and-fix cycle?"        | "What rate does CLARA produce on a frozen, single-shot stress test?"   |
| **Run model**                   | Iterative: fixes shipped between phases (Fix #1 – Fix #5)                     | Single shot, one CLARA commit, no remediation mid-run                   |
| **Hand-coding bar**             | Attorney coding with senior-attorney adjudication; κ not formally computed   | Two coders blind + adjudicator; pre-stated Cohen's κ ≥ 0.70 threshold  |
| **Independence**                | Coding team overlaps with build team (disclosed)                              | Adjudicator external to the build team                                  |
| **Bias mitigation**             | Three-arm comparison (CLARA post-fix / pre-correction / bare-LLM baseline)   | Hypotheses and thresholds locked in writing **before** the run          |
| **Headline metric**             | Per-citation 0.43% (post-firewall) and per-response ~3.6% (pre-redaction)    | Per-query hallucination rate, post-firewall, hand-coded                 |
| **Comparable to Stanford 2024?**| No headline-to-headline; the per-response number (~3.6%) is the closer comparison | No (single-jurisdiction, hand-coded against a custom rubric)        |

---

## What each study can do that the other cannot

### What this bundle (374-query) does that the v2 bundle cannot

- **Reports actual CLARA performance on a substantial query set with a published headline number** (0.43% per-citation, ~3.6% per-response). v2 has no published number yet by design.
- **Provides three-arm side-by-side data** — every prompt has CLARA post-fix, CLARA pre-correction, and bare-LLM baseline responses captured in one CSV. A reader can re-derive any rate they want from the raw data. v2 is single-arm.
- **Documents the find-and-fix cycle** — five architectural fixes, ~14 net-new blocklist entries, and five real-case false-positive corpus closures, all shipped during the audit window. This is what an internal QA pass looks like; it is not what an independent benchmark looks like.
- **Provides the per-firewall-layer accountability table** — `reports/firewall-effectiveness.clara-2026-04-21.md` lists, for each of the ~10 firewall layers, what fraction of fabrication attempts that layer caught. This is the public remediation backlog.
- **Records the two-sided audit outcome** — five real-case false positives detected and closed via D2 ingestion. v2 will probably not surface false positives at the same rate because v2 is single-shot.

### What the v2 bundle does that this one cannot

- **Locks the methodology before the results exist.** The hypotheses (H-A through H-E), the κ ≥ 0.70 acceptance threshold, the substitution rule (no query may be added/removed/edited after registration), and the analysis plan are all timestamped on OSF before any v2 query is run. Nothing can be retro-fit.
- **Pre-commits to publishing whatever the data shows.** §8 of v2's `prereg/preregistration.md` is a written commitment to publish disconfirming results. This 374-query audit is also published warts-and-all (Finding F-1, the inverse-coherence canary failures, etc.), but it was not pre-committed in writing.
- **Names an external adjudicator.** §9 of the v2 preregistration commits the third-reviewer adjudicator to be external to the CLARA build team. This 374-query audit's adjudication was internal — disclosed openly in `METHODOLOGY.md` §3.5.
- **Pre-stated κ threshold.** If pre-adjudication κ falls below 0.70, the v2 headline rate is **not** published. This is the single strongest credibility lever in either bundle and is the answer to "your coders work for you — how do we know they were consistent?"

---

## Why we need both

A skeptical reader can attack each study from the opposite direction:

- This audit has a favorable headline (0.43%) but is not preregistered, the coders work for the build team, and the methodology bundles the find-and-fix cycle into the headline number. A skeptic can reasonably ask: "Would a fresh prompt set, scored by neutral coders, produce the same number?"
- The v2 200-query preregistration answers exactly that question, but **only after it runs**. A skeptic reading v2 alone, before the results land, sees only a methodology document — no number to anchor against.

Together they answer both halves:

1. This 374-query audit shows what a real five-phase find-and-fix cycle produces, with all three arms preserved so any rate can be recomputed.
2. The v2 200-query preregistration commits, in writing and on a timestamped surface, to a single-shot, externally-adjudicated, κ-gated re-measurement on a fresh prompt set — and to publishing the result regardless of which way it cuts.

If you read only this bundle, you are looking at internal QA. If you read only the v2 bundle, you are looking at a methodology document with no data. Reading both is the audit.

---

## Pointers

- **v2 200-query bundle, OSF DOI:** _to be added once issued_
- **v2 200-query bundle, GitHub:** _to be added once published_
- **v2 200-query bundle, headline documents:** `prereg/preregistration.md` (hypotheses + thresholds + κ rule) and `METHODOLOGY.md` (run protocol + coding procedure)
- **v2 200-query bundle, dataset:** `data/clara_v2_audit_queries_200.csv` (200 queries, frozen at registration)

---

**Both bundles use the same eight-code taxonomy** (`taxonomy/taxonomy.md`, identical across the two bundles). Hits in v2 will be coded against the same definitions used in this 374-query audit, so when v2 results publish they can be set side-by-side with this audit's per-citation rate without any taxonomy translation.
