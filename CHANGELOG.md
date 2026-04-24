# Changelog

All notable changes to the CLARA Five-Phase 374-Query Audit bundle are recorded here. The bundle follows semantic versioning at the bundle level (not at the level of individual files inside it).

The OSF registration freezes a specific tag. Cosmetic post-tag fixes (typos, broken links) are logged here without bumping the registered version. Any change to the dataset, the taxonomy, the methodology, or the results requires a new bundle version and a new OSF registration that cites the prior one.

## [Unreleased]

_Reserved for post-v1.0.0 typo / link fixes that do not require a new OSF registration._

## [1.0.0] — Pending OSF submission

Initial release for OSF archival registration of the completed five-phase audit.

### Added
- `README.md` — bundle overview and honest-framing disclosures.
- `ABSTRACT.md` — one-page summary for the OSF wiki.
- `METHODOLOGY.md` — phase design, three-arm structure, hand-coding procedure, threats to validity, iterative-remediation disclosure.
- `RESULTS.md` — canonical five-phase audit report (v3.0 corrected, supersedes v2.0 of April 20, 2026 AM and the draft of April 19, 2026).
- `taxonomy/taxonomy.md` — H1–H7 + OTHER definitions, severity weights, out-of-scope categories.
- `data/clara-audit-dataset-374queries.csv` — consolidated 374-prompt × 3-arm dataset (~11 MB; one row per prompt; CLARA post-fix, CLARA pre-correction, and bare-LLM baseline columns side by side).
- `build/build-dataset-csv.py` — Python consolidator that joins per-arm result JSONL into the canonical CSV.
- `prompts/*.jsonl` — per-phase prompt files (10 files, ~140 KB total) for replay against any pinned CLARA commit.
- `reports/` — per-phase reports, firewall-effectiveness analysis, per-bucket hand-coding sheets, supplementary edge-case reports, citation-coherence design doc, and Fix #5 design notes.
- `LICENSE-CODE` (MIT) and `LICENSE-DATA` (CC-BY-4.0).

### Audit summary at registration

- **Headline rate:** 0.43% per-citation (post-firewall, Phases 1–4); ~3.6% per-response (pre-redaction, Phases 1–3 baseline).
- **Phase totals:** P1 30 / P2 120 / P3 100 / P4 50 / P5 50 + 11 regression. Edge-case supplements: v1 15 / v2 regression 9. Bundle CSV: 374 rows.
- **Detections:** 11 confirmed fabrications across 2,576 evaluated citations.
- **Closures:** 5 real-case false positives ingested via the D2 protocol; ~14 net-new `KNOWN_FABRICATED_CITATIONS` entries; 5 architectural fixes shipped (Fix #1 – Fix #5).
- **Carry-forward:** Audit-panel single-verdict rewire (broader Fix #3 scope) deferred to post-beta with the V2 forced-emission canary bucket as the regression test.

### Not included in the bundle
- Raw per-arm `results/` directory (~44 MB of JSONL, biggest file 3.3 MB). The consolidated CSV in `data/` is derived from it; the raw JSONL is available on request via the OSF project's Files attachments or the GitHub repo's release assets if a reviewer needs to verify the CSV assembly.
