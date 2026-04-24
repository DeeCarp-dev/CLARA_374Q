# CLARA Hallucination Audit — Five-Phase 374-Query Study

**A registered report of completed work**

This repository accompanies an OSF.io archival registration of CLARA's five-phase hallucination audit, conducted April 2026. The dataset, the per-phase reports, the consolidated 374-query CSV, the prompt files for replay, and the hand-coding rubric are all frozen here so that a third party can inspect the methodology, replicate the analysis, and re-run the audit against any pinned CLARA commit.

## What this is

A **registered report of completed work**. The audit was designed in advance, executed in five sequential phases (with two supplementary edge-case batches) between April 19 and April 20, 2026, and produced same-cycle architectural fixes and corpus closures. We are publishing the dataset, the methodology, and the full results — in their final form — on a timestamped surface so that the design and the numbers are immutable from this point forward.

## What this is *not*

- **Not** a preregistration. Results are already known and published in `RESULTS.md`. For a methodology-first preregistration, see the companion v2 200-query bundle.
- **Not** a head-to-head benchmark. The Stanford HAI/RegLab 2024 comparison appears in `RESULTS.md` with explicit methodology caveats; CLARA is Virginia-specific while the Stanford benchmark is national.
- **Not** automated. Verdicts were produced by attorney coders against the published rubric in `taxonomy/taxonomy.md`. No LLM-as-judge.
- **Not** a single-arm study. Three arms were run side by side: CLARA post-fix, CLARA pre-correction, and a bare-LLM baseline. The 374-query CSV preserves all three response columns per prompt for any reader who wants to do their own analysis.

## What's in the bundle

```
clara-audit-374/
├── README.md                          # this file
├── ABSTRACT.md                        # one-page summary for OSF wiki
├── METHODOLOGY.md                     # phase design, run protocol, three-arm structure, hand-coding
├── RESULTS.md                         # the canonical five-phase report (v3.0 corrected)
├── CHANGELOG.md                       # version history
├── LICENSE-CODE                       # MIT — covers build/
├── LICENSE-DATA                       # CC-BY-4.0 — covers data/, prompts/, reports/, taxonomy/, docs
├── taxonomy/
│   └── taxonomy.md                    # H1–H7 + OTHER definitions and severity weights
├── data/
│   └── clara-audit-dataset-374queries.csv   # 374 prompts × 3 arms in one CSV (~11 MB)
├── prompts/
│   ├── baseline.jsonl                 # 30 prompts — Phase 1 anchored baseline
│   ├── phase2.jsonl                   # 120 prompts — Phase 2 non-anchored
│   ├── phase3.jsonl                   # 100 prompts — Phase 3 adversarial
│   ├── phase4.jsonl                   # 50  prompts — Phase 4 confirmation
│   ├── phase5.jsonl                   # 50  prompts — Phase 5 V2 full run
│   ├── phase5_regression_only.jsonl   # 11  prompts — Phase 5 regression-bucket subset
│   ├── edge_cases_v1.jsonl            # 15  prompts — supplementary edge-case batch v1
│   ├── edge_cases_v2_regression.jsonl # 9   prompts — supplementary edge-case regression
│   ├── ec-007.jsonl                   # focused edge-case probe
│   └── fix2-verify.jsonl              # Fix #2 verification probe
├── build/
│   └── build-dataset-csv.py           # consolidator: prompts/ + results/ → CSV
└── reports/
    ├── CLARA_Five_Phase_Hallucination_Audit_Report_CORRECTED.md   # same as RESULTS.md
    ├── three-phase-audit-final.md                                  # Appendix A — Phases 1–3
    ├── phase4-confirmation.md                                      # Appendix B — Phase 4
    ├── phase5-confirmation.md                                      # Appendix C — Phase 5 V1
    ├── phase5-v2-supplement.md                                     # Appendix D — Phase 5 V2
    ├── citation-coherence-design.md                                # Appendix E — Fix #5 design
    ├── EDGE_CASES_V1_REPORT.md                                     # supplementary
    ├── EDGE_CASES_V2_REGRESSION.md                                 # supplementary
    ├── handcoding.*.md                                             # per-bucket coding sheets
    ├── firewall-effectiveness.clara-2026-04-21.md                  # firewall layer attribution
    ├── firewall-effectiveness.clara-2026-04-21.per-row.csv         # per-row firewall verdicts
    ├── postfix-verification.clara-2026-04-21.md                    # post-fix verification
    ├── cite-survival.clara-2026-04-21.md                           # citation survival analysis
    ├── phase2.shortlist.md                                         # phase 2 manual review shortlist
    ├── phase3.shortlist.md                                         # phase 3 manual review shortlist
    └── BUG.va-code-not-found-redaction-gap.md                      # bug report from the audit
```

## Headline result (from `RESULTS.md`)

- **Per-citation hallucination rate (post-firewall, Phases 1–4):** **0.43%** (11 confirmed fabrications across 2,576 citations).
- **Per-response rate (initial emission, pre-redaction, Phases 1–3 baseline):** ~3.6%.
- **Phase 5 regression bucket:** 11/11 phantom guards fired correctly end-to-end on forced-emission V2 prompts.
- **Two-sided audit outcome:** 11 fabrications detected and blocklisted same-cycle; 5 real-case false positives detected and corpus-closed via the D2 ingestion protocol same-cycle.
- **Architectural fixes shipped this cycle:** 5 (Fix #1 – Fix #5).
- **Post-beta carry-forward:** broader audit-panel single-verdict rewire (deferred Fix #3 scope), with the V2 forced-emission canary bucket as the regression test.

`RESULTS.md` is the canonical document. The numbers above are pulled from it; if any number disagrees with `RESULTS.md`, `RESULTS.md` is correct.

## Honest framing

Three pre-emptive disclosures that belong on the front page of any reading of this audit:

1. **Per-citation, post-firewall is the headline.** That number (0.43%) is the rate an attorney sees on the page after the redaction layer has run. The per-response, pre-redaction rate is roughly an order of magnitude higher (~3.6% on the Phases 1–3 baseline) and is the right number to compare to the Stanford HAI/RegLab 2024 numbers, which are per-response. We report both. Anyone using only one of the two numbers is reading the audit selectively.
2. **The audit is iterative, not single-shot.** Each phase fed remediation into the next: blocklist additions, regex fixes, corpus closures, and architectural fixes (Fix #1 through Fix #5) shipped during the audit window. This is intentional — the audit was designed to surface failure modes and close them — but it means the 0.43% number reflects CLARA *as fixed during the audit cycle*, not CLARA at the start. Anyone re-running the audit against an older commit will get a different number, and that is the point.
3. **The remediation team and the build team overlap.** Coding was performed by attorneys; the build team designed the queries and shipped the fixes. This is disclosed in `METHODOLOGY.md`. The audit is a step toward fully independent third-party evaluation, not the destination. The companion v2 200-query bundle is preregistered specifically to address this independence gap.

## Reproducing the analysis

The consolidated CSV is the canonical artifact. Anyone with access to the underlying per-arm result files (`results/` in the source repo, ~44 MB of raw JSONL not included in this bundle to keep it under common filesize thresholds — available on request or via OSF Storage attachment) can re-derive the CSV byte-for-byte:

```
python3 build/build-dataset-csv.py
sha256sum data/clara-audit-dataset-374queries.csv
```

Anyone with API access to CLARA can re-run the audit against any pinned commit by feeding `prompts/*.jsonl` through the runner under `tests/hallucination-audit/`. The raw 44 MB `results/` directory is not bundled here by default; if a reviewer needs the per-query JSONL with full firewall verdict streams and three-arm responses, request it via the OSF project's Files attachments or the GitHub repo's release assets.

## License

- **Code** (`build/`): MIT — see `LICENSE-CODE`.
- **Data, prompts, reports, taxonomy, docs**: CC-BY-4.0 — see `LICENSE-DATA`. Reuse with attribution.

## Citation

If you use this dataset or cite the audit, please cite the OSF DOI (added once issued) and the GitHub release tag (`v1.0.0`).
