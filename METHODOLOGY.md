# Methodology — CLARA Five-Phase 374-Query Hallucination Audit

This document explains, in enough detail for a third party to reproduce, **how the audit was designed**, **how CLARA was queried**, **how the responses were hand-coded**, and **why the final number is what it is**. It is the companion to `RESULTS.md`, which reports the actual findings, and to `taxonomy/taxonomy.md`, which defines the codes a coder may apply.

The intent is to make the methodology auditable, not to defend the choices. Where we made a judgment call — including iterative remediation during the audit cycle — we say so on the page rather than buried in an appendix.

---

## 1. Audit design

### 1.1 Five phases plus two supplementary batches

The headline "five-phase 374-query audit" is precise about the phases but slightly imprecise about the count. The breakdown:

| Phase                              | Prompts | Purpose                                                                        |
|------------------------------------|--------:|--------------------------------------------------------------------------------|
| **Phase 1** — Anchored baseline    |      30 | Queries with known correct answers from verified `case_cards` rows. Sanity check. |
| **Phase 2** — Non-anchored         |     120 | Open-ended Virginia legal questions without predetermined answers.            |
| **Phase 3** — Adversarial          |     100 | Leading questions, fictional premises, edge cases designed to trigger hallucination. |
| **Phase 4** — Confirmation         |      50 | Re-test known failure modes; validate Fix #2 (drafting-mode bypass closure). |
| **Phase 5** — Full V2 + regression |  50 + 11 | 50-prompt fresh-discovery run + 11-prompt regression bucket against the post-Fix-5 build. |
| **Five-phase total**               | **361** | (351 unique + 11 regression overlap with Phase 5)                              |
| Edge-case supplement v1            |      15 | Off-cycle adversarial probes used during Phase 3 / 4 development.             |
| Edge-case supplement v2 regression |       9 | Targeted regression of v1 findings.                                           |
| **Bundle total (CSV row count)**   | **374** | All prompts captured in one consolidated CSV.                                  |

`RESULTS.md` reports the headline against the **350 main-phase queries** that were the basis of the per-citation rate calculation (Phases 1–4 = 300 plus 50 of Phase 5; the regression bucket and edge cases are reported separately because they're not unique discovery prompts). The CSV in `data/` includes all 374 rows so a reader can do their own arithmetic on any subset.

### 1.2 Why iterative remediation was part of the design

This is the design choice most likely to be misread, so it needs a paragraph in plain English.

The audit was not run as a single-shot benchmark. It was run as a five-phase **find-and-fix cycle**: each phase's findings (fabrications, false positives, regex gaps, pipeline bugs) fed remediation that shipped before the next phase ran. Five architectural fixes (Fix #1 through Fix #5) and approximately 14 net-new `KNOWN_FABRICATED_CITATIONS` blocklist entries were added during the audit window. Five real-case false positives were closed via the D2 ingestion protocol the same cycle.

The 0.43% per-citation rate reported in `RESULTS.md` is therefore CLARA **as fixed during the cycle**, not CLARA as it stood when Phase 1 began. This was the design's intent — surface failure modes and close them — but it has two consequences a reader should understand:

1. The number is **not** comparable to a single-shot benchmark like Stanford HAI/RegLab 2024 without saying so explicitly. `RESULTS.md` says so explicitly.
2. The number is **reproducible** only against the post-fix CLARA commit, not against CLARA at the start of the audit. A re-run against any older commit will produce a higher number, and that is correct.

The companion v2 200-query bundle is preregistered specifically as a **single-shot, no-remediation** run on a pinned commit, to provide the comparable number this audit cannot.

### 1.3 Three arms

For every one of the 374 prompts, three responses were captured:

| Arm                    | What it is                                                                 |
|------------------------|----------------------------------------------------------------------------|
| `clara_postfix`        | CLARA at the post-Fix-5 commit. The full firewall stack is active. This is the production behavior the headline rate is computed against. |
| `clara_precorrection`  | CLARA at the same commit, but with the inline-redaction layer disabled. The pre-correction text is captured so we can see what the LLM **wanted** to say before the firewall intervened. This drives the per-response rate. |
| `baseline_llm`         | A bare LLM (Claude Sonnet 4.5 at temperature 1.0, no firewall, no Virginia anchoring) answering the same prompt. This is the reference floor — what a generic legal AI without CLARA's stack produces on the same questions. |

All three response columns, both pre- and post-correction CLARA texts, all extracted citations, and the firewall verdict streams are preserved in the consolidated CSV under the schema documented in §1.5.

### 1.4 Source and authorship of prompts

All 374 prompts were authored by the CLARA team specifically for this audit. They were written to probe Virginia-specific failure modes the team already suspected existed in the pipeline (caption-confusion fabrications, ghost statute sections, dead-law amendments, plea colloquy / contributory negligence / sovereign immunity anchored doctrine), and to provide a baseline of common doctrinal queries against which to measure normal behavior.

Bias disclosure: **the queries are ours.** They are biased toward Virginia practice and toward known CLARA failure modes. This is on purpose — a Virginia-specific assistant should be evaluated on Virginia-specific queries — but it means the headline rate from this audit should be read as "rate on this stress test," not as an open-domain LLM hallucination rate.

### 1.5 CSV schema

`data/clara-audit-dataset-374queries.csv` has 374 rows and 36 columns. Every prompt is one row; every arm is a column-group:

| column group           | columns                                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Identity               | `id`, `phase`, `prompt`, `mode`, `domain`, `tags`, `expected_authorities`                                                |
| CLARA post-fix arm     | `clara_postfix_pre_correction_text`, `clara_postfix_response_text`, `clara_postfix_warnings`, `clara_postfix_extracted_citations`, `clara_postfix_extracted_citations_count`, `clara_postfix_responsible_layers`, `clara_postfix_findings`, `clara_postfix_latency_ms` |
| CLARA pre-correction   | `clara_precorrection_pre_correction_text`, `clara_precorrection_response_text`, `clara_precorrection_warnings`, `clara_precorrection_extracted_citations`, `clara_precorrection_extracted_citations_count`, `clara_precorrection_findings`, `clara_precorrection_latency_ms` |
| Bare-LLM baseline      | `baseline_llm_model`, `baseline_llm_temperature`, `baseline_llm_response_text`, `baseline_llm_extracted_citations`, `baseline_llm_extracted_citations_count`, `baseline_llm_input_tokens`, `baseline_llm_output_tokens`, `baseline_llm_latency_ms` |
| Pre-check              | `precheck_va_code_checked`, `precheck_va_code_verified`, `precheck_va_code_not_found`, `precheck_case_checked`, `precheck_case_verified`, `precheck_case_not_found` |

Citation lists, tags, expected authorities, warnings, and findings are JSON-encoded inside their CSV cells (single-line JSON arrays/objects). A reader using pandas / R can `json.loads(...)` each cell to get back the structured form. `RESULTS.md` does not require the CSV — every reported number is summarized in the prose — but the CSV is the source of truth if anyone wants to re-derive the numbers themselves.

---

## 2. Run protocol

### 2.1 System under test

- **Project:** CLARA (Virginia-specific legal AI assistant), Aequus Law Software LLC
- **Audit run window:** April 19–20, 2026 (with Phase 5 V2 re-run on April 20 PM)
- **Final headline-rate run:** Post-Fix-5 commit on April 20, 2026
- **Model under the hood:** Claude Sonnet 4.5 (CLARA's primary path)
- **Mode:** `chat`, default jurisdiction Virginia, all firewall layers at production defaults

### 2.2 Firewall layers active during the audit

Documented in `RESULTS.md` §"Verification Architecture." Reproduced here at headline level:

| Tier  | Layer                                                                                              |
|------:|----------------------------------------------------------------------------------------------------|
| 0     | RULE 33 Blocklist (`KNOWN_FABRICATED_CITATIONS`, ~48 entries post-cycle)                           |
| 0.5   | Reporter Volume Validator                                                                          |
| 0.7   | Reporter Jurisdiction Validator                                                                    |
| 1     | Caption-Mismatch Detector (`AssertedCanonicalDetector`)                                            |
| 2     | Holding Coherence Validator (HCV)                                                                  |
| 3     | Quote Provenance Layer (QPL)                                                                       |
| 4     | Citation Grounding Handshake (CGH) — wrapped by Fix #5 guards (pre-CGH filter + post-CGH revert)   |
| 5     | Va. Code Structural Validator (32,216+ section paths)                                              |
| 6     | Discovery Sanctions Firewall                                                                       |
| 7     | Negative Treatment Service (Shadow Mode — logs CourtListener V4 negative-treatment scans without gating) |

### 2.3 Per-prompt protocol

For each prompt in `prompts/<phase>.jsonl`, in file order:

1. Send to the post-fix CLARA arm in a fresh chat session.
2. Send to the pre-correction CLARA arm in a fresh chat session.
3. Send to the bare-LLM baseline arm in a single API call.
4. Capture: full response text (pre- and post-correction for CLARA), all firewall verdicts emitted by the post-generation pipeline, latency, the model identifier, extracted citations, and warnings.
5. Persist a JSON record per arm under `results/<arm>/<phase>.jsonl`. The `.checked.jsonl` suffix marks the post-precheck variant where Va. Code structural validation has been run and recorded.

No retries within a phase. If a prompt errored, the error was captured in the JSONL record and the prompt was re-run by hand before the phase closed.

### 2.4 Iterative remediation between phases

Between phases, the following remediation actions were permitted and were performed:

- Adding entries to `KNOWN_FABRICATED_CITATIONS` for any phantom citation observed in the previous phase, with regex pattern + canonical caption + reason.
- Closing any real-case false positives via the D2 ingestion protocol (case_card update + verbatim opinion passage + miscitation guard).
- Shipping architectural fixes when the post-mortem of a leak required pipeline-level changes (Fixes #1–#5).
- Adjusting prompts in **subsequent** phases to probe newly-surfaced failure modes. **No** retroactive editing of prior-phase prompts.

This is the iterative-remediation design called out in §1.2. It is what produces the 0.43% per-citation post-firewall rate; it is also what makes the audit non-comparable to a single-shot benchmark without the methodology caveat in `RESULTS.md`.

---

## 3. Hand-coding procedure

### 3.1 Coders

Coding was performed by Virginia-licensed attorneys (or attorney-supervised analysts) on the CLARA team. Per-bucket coding sheets are in `reports/handcoding.*.md`. The coders' role was to:

1. Read each CLARA response.
2. Identify any citation in the response.
3. Verify each citation against four criteria (see §3.2).
4. Mark `FABRICATED` if the citation failed any criterion.
5. Record the responsible firewall layer(s) for each fabrication.

### 3.2 Hit definitions

A citation was marked `FABRICATED` if it failed **any** of:

1. **Citation Existence** — Does the case exist at the stated reporter / volume / page? Verified against CourtListener V4 cluster lookups, Westlaw / Lexis search, and the local `case_cards` table.
2. **Caption Accuracy** — Does the party name match the canonical caption at that citation?
3. **Holding Coherence** — Does the stated holding match the actual holding of the case?
4. **Temporal Validity** — Is the case still good law (not overruled or superseded)?

These four criteria correspond to the eight-code taxonomy in `taxonomy/taxonomy.md` as follows: criterion 1 → `H1_FAB_CITE`; criterion 2 → `H1_FAB_CITE` (caption variant) or `H7_FORM_ERR` depending on severity; criterion 3 → `H2_FAB_HOLD`; criterion 4 → `H4_NEG_TREAT`. The taxonomy adds `H3_WRONG_JX`, `H5_QUOTE_PROV`, `H6_DEAD_LAW`, and `OTHER` for failure modes that the four criteria do not cleanly separate.

### 3.3 Two-sided coding

Unique to this audit: coders also flagged **false positives** — real cases that the firewall incorrectly wrapped with `[CITATION UNVERIFIED — DO NOT USE]` markers. Five such cases were identified in the Phase 5 V2 50-prompt run. Each was verified against CourtListener and corpus-closed via the D2 ingestion protocol within the same cycle.

This two-sided design is a deliberate departure from one-sided benchmarks. A defense-in-depth firewall risks over-firing; an audit that does not look for over-firing tells you only half the story. The five FPs are listed in `RESULTS.md` and detailed in `reports/phase5-v2-supplement.md`.

### 3.4 Out-of-scope (not hallucinations)

Per `taxonomy/taxonomy.md`, the following are **not** scored as hallucinations:

- Tone or stylistic disagreements
- Strategic disagreements ("I would have argued X")
- Correct refusals
- `[CITATION UNVERIFIED — DO NOT USE]` blocks — these are **successful** firewall catches
- `[MISSING_FACT: …]` placeholders in DRAFT mode — correct behavior

### 3.5 Adjudication

Disagreements between coders were resolved by senior-attorney review with the verification artifact (CourtListener URL, Westlaw screenshot, statute text) attached. Inter-rater reliability was not formally computed for this audit; it is a registered open item for the v2 200-query preregistration, where Cohen's κ ≥ 0.70 is the pre-stated acceptance threshold. We acknowledge this as a methodological limitation of the 374-query study and address it in the v2 design.

---

## 4. Reported numbers

`RESULTS.md` is the canonical numbers document. At a glance:

- **Per-citation post-firewall rate** = `total_fabrications / total_citations_evaluated` across Phases 1–4 = `11 / 2,576 = 0.43%`.
- **Per-response pre-redaction rate** (Phases 1–3 baseline) = `9 / 250 = 3.6%`. This is the right number to compare to per-response benchmarks.
- **Phase 5 V2 forced-emission regression bucket:** 11/11 emission, 9/9 phantom guards fired correctly, 2/2 canary failures (real cases incorrectly redacted under forced-quote prompts) — the latter producing **Finding F-1**, the inverse-coherence failure that motivates the deferred broader Fix #3.
- **False-positive closures:** 5 real Virginia Supreme Court opinions corpus-closed via D2 (Rascher, Schafer, Yeatts, Muhammad, J.B. Moore Electrical Contractor).
- **Architectural fixes:** Fix #1 (Kensington regex), Fix #2 (drafting-mode bypass), Fix #3 (single-verdict canonical normalizer — partial; broader rewire deferred), Fix #4 (blocklist regex ordering), Fix #5 (CGH self-attestation bypass; 30/30 unit tests green).

A per-firewall-layer accountability table is in `reports/firewall-effectiveness.clara-2026-04-21.md` with the per-row CSV in the same directory.

---

## 5. Threats to validity (acknowledged up front)

1. **Construct validity.** Per-citation, post-firewall is a generous denominator. Per-response, pre-redaction is a stricter one. We report both. A reader who uses only the headline number is reading the audit selectively.
2. **Selection bias.** Queries were authored by the CLARA build team. Mitigation here is partial: trap-style adversarial coverage is heavy in Phases 3 and 5, the per-phase coding sheets are public in `reports/`, and a methodology-first preregistration (the v2 200-query bundle) is available as a complementary check. **The audit is not blind.**
3. **Iterative remediation.** As discussed in §1.2 and §2.4, fixes shipped between phases. The 0.43% number is CLARA-as-fixed, not CLARA-as-of-Phase-1. A single-shot rerun on a frozen commit is the v2 200-query bundle's job.
4. **Coder bias.** Coders were CLARA team members or attorney-supervised. Inter-rater reliability was not formally computed. This is the principal limitation of the audit's independence and we surface it here, not in an appendix.
5. **Generalization.** Results from this dataset do not generalize beyond Virginia practice and beyond the failure modes we chose to probe. The Stanford HAI/RegLab comparison in `RESULTS.md` is informative but **not** apples-to-apples; the methodology comparison table there flags every dimension that differs.
6. **Pipeline drift.** CLARA is under active development. The post-fix commit pinned for the headline rate is recorded in `RESULTS.md` and in the bundle's `CHANGELOG.md`. Re-runs against later commits are different studies.

---

## 6. Versioning

This methodology is `v1.0.0`, frozen at OSF registration. Any change after registration requires:

1. A new bundle version with a new SHA-256 on the CSV.
2. A new OSF registration that cites this one.
3. A clear statement in the new bundle of what changed and why.

Cosmetic fixes (typos, broken links) are tracked in `CHANGELOG.md` without bumping the version.
