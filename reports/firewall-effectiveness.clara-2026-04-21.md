# CLARA Firewall-Effectiveness Scan

**Source:** `tests/hallucination-audit/results/clara/*.checked.jsonl`
**Run ID:** `clara-2026-04-21`  **Generated:** 2026-04-21T17:44:05.402Z

## Why this scan exists

The precheck-only metric (citation `NOT_FOUND` rate) systematically *understates*
CLARA's safety lift over a bare LLM, because the firewall delivers most of its
value through three post-generation channels that the bare-LLM arm has no
equivalent of:

1. **`firewall_block` SSE event** — pre-LLM hard refusal. The query never
   reaches generation; CLARA returns a structured refusal instead.
2. **`content_correction` SSE events** — post-LLM citation excision / rewrite.
   The model produced text, then the citation pipeline modified or removed
   suspect content before the user saw the response.
3. **`preCorrectionText` ≠ `responseText`** — *confirmed* audit-driven output
   modification, observed by directly comparing what the LLM emitted to what
   was returned downstream.

All three are CLARA-only by construction. The bare-LLM arm cannot produce them.

## Per-phase breakdown

| Phase | Rows | Firewall block | Content-correction rows | Output modified | Chars removed | Refusal language | `[MISSING_FACT]` |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 30 | 0 | 11 (36.7%) | 11 (36.7%) | 7,825 | 0 | 0 |
| phase2 | 120 | 0 | 50 (41.7%) | 50 (41.7%) | 48,319 | 1 | 3 |
| phase3 | 100 | 0 | 56 (56.0%) | 55 (55.0%) | 33,078 | 10 | 0 |
| phase4 | 50 | 0 | 31 (62.0%) | 31 (62.0%) | 21,775 | 8 | 0 |
| phase5 | 50 | 1 | 36 (72.0%) | 36 (72.0%) | 23,924 | 3 | 2 |
| edge_cases_v1 | 15 | 0 | 8 (53.3%) | 8 (53.3%) | 7,662 | 0 | 0 |
| edge_cases_v2_regression | 9 | 0 | 4 (44.4%) | 4 (44.4%) | 5,307 | 3 | 0 |
| **TOTAL** | **374** | **1** | **196 (52.4%)** | **195 (52.1%)** | **147,890** | **25** | **5** |

## Headline metrics

- **Output-modification rate** (audit changed something): **195/374 = 52.1%**.
  This is the cleanest measure of firewall *engagement*: the post-generation
  pipeline rewrote, excised, or annotated more than half of all CLARA responses.
- **Total characters removed** by content-correction across the run:
  **147,890**, an average of
  **758 chars per modified response**.
- **Pre-LLM hard blocks**: **1/374 = 0.27%**.
  The Malpractice Firewall hard-refuses rarely; most safety work is done
  *post*-generation, which is consistent with the documented "DRAFT WITH
  ADVISORY" architecture.
- **Embedded refusal language**: **25/374** responses contain
  uncertainty / refusal phrasing visible to the user (e.g. "cannot verify",
  "[UNCERTAIN]", "[VERIFY]"). This is CLARA voluntarily flagging uncertainty
  in-line — a behavior bare LLMs do not exhibit at meaningful rates.
- **`[MISSING_FACT:...]` placeholders**: **5/374** responses use the
  documented DRAFTING-mode placeholder convention.
- **Citation audit ran on 373/374** responses (the audit pipeline is
  effectively universal, not selective).

## How to read this against the bare-LLM precheck

The bare-LLM arm has 0 of each of these signals by construction. So the
comparison is asymmetric: bare-LLM's `NOT_FOUND` rate measures *what the LLM
emitted*, while CLARA's measures *what the LLM emitted minus what the firewall
removed*. To make the comparison apples-to-apples, the published report should
present **both**:

- Per-arm `NOT_FOUND` rate on **post-pipeline output** (the precheck numbers
  already in the database under the matched run_ids).
- CLARA's per-arm `NOT_FOUND` rate on **`preCorrectionText`** (what CLARA
  *would* have shown without the firewall). The delta between those two
  numbers *is* the firewall lift, measured in the same units as bare-LLM.

That second number is computable from this scan plus a re-run of the precheck
over `preCorrectionText` instead of `responseText`. That is the recommended
next step for a defensible architectural-lift claim.
