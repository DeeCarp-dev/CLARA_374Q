# Post-fix Verification — Va. Code UNVERIFIED Advisory Surfacing

**Date:** 2026-04-21
**Fix under test:** `BUG.va-code-not-found-redaction-gap.md` — Phase 2.6
`unverified` bucket converted from console-log-only to user-visible
"UNVERIFIED STATUTE" advisory appended to `processedText`.
**Subset:** Phase 5 (50 prompts) + edge_cases_v2_regression (9 prompts) =
**59 fresh post-fix runs**, compared against the precorrection backup
(152 + 27 = 179 rows from prior accumulated runs).
**Backup files:**
`phase5.precorrection-backup.20260421-220000.jsonl`,
`edge_cases_v2_regression.precorrection-backup.20260421-220000.jsonl`.
**Wall time:** phase5 = 53min (50 q × 63.6s avg), ec_v2 = 6.5min (9 q × 43.7s
avg). Both phases parallel with 30s login stagger; 0 errors in phase5,
0 errors in ec_v2 (1 warning on phase5 q49, unrelated).

## Results

### Per-phase

| Phase | Subset | Rows | UNVERIFIED present | NONEXISTENT present | Citation Notice |
|---|---|---:|---:|---:|---:|
| Phase 5 | pre-fix | 152 | **0 (0.0%)** | 0 (0.0%) | 1 (0.7%) |
| Phase 5 | post-fix | 50 | **0 (0.0%)** | 0 (0.0%) | 2 (4.0%) |
| ec_v2_regression | pre-fix | 27 | **0 (0.0%)** | 1 (3.7%) | 0 (0.0%) |
| ec_v2_regression | post-fix | 9 | **1 (11.1%)** | 1 (11.1%) | 1 (11.1%) |

### Combined

| Bucket | UNVERIFIED present | NONEXISTENT present |
|---|---:|---:|
| Pre-fix (179 rows) | **0 (0.0%)** | 1 (0.6%) |
| Post-fix (59 rows) | **1 (1.7%)** | 1 (1.7%) |

## Verified-fix evidence

### Acceptance criterion 1 — Va. Code NOT_FOUND advisory rate moves off zero

✅ **Met.** Combined post-fix: **1/59 (1.7%) UNVERIFIED-STATUTE advisories**
in real CLARA responses, versus **0/179 (0.0%)** in the precorrection
backup. The advisory rate moved from `0` to `>0` exactly as predicted by
the BUG report's root-cause analysis.

### Acceptance criterion 2 — advisories appear in real responses, not just smoke tests

✅ **Met.** Concrete production-verified instance:

- **Prompt:** `ecv2-002` (edge_cases_v2_regression)
- **Detected unverified section:** `Va. Code § 4.1-1301`
- **Behaviour:** Title `4.1-` exists in the corpus (real Title 4.1, Alcoholic
  Beverage Control Act), but section `4.1-1301` was not present in the
  32,216-row `va_statutes` corpus. The new advisory correctly classified
  this as UNVERIFIED (not NONEXISTENT) — the soft-language path designed
  for "title valid, section possibly fabricated/repealed/unindexed."
- **Pre-fix on the same prompt id (in backup, multi-run):** zero UNVERIFIED
  advisories across all 27 prior runs.

### Acceptance criterion 3 — no regression on existing NONEXISTENT path

✅ **Met.** `ecv2-004` continues to surface the existing **NONEXISTENT
STATUTE WARNING** on `Va. Code § 3.2-4112.1` (Title 3.2 prefix without a
matching base section under the phantom-decimal-suffix path). Behaviour
unchanged pre vs post.

### Acceptance criterion 4 — no spam, no collateral damage

✅ **Met.**
- 50/50 phase5 prompts produced **0 spurious UNVERIFIED advisories**
  (phase5's prompts predominantly cite verified Va. Code or no statutes,
  so the fix correctly stays silent).
- 0 errors / 1 unrelated warning across 59 fresh post-fix runs.
- The MAX_UNVERIFIED=8 cap was never tripped on this subset (max
  observed was 1 distinct unverified section per prompt).

## Honest caveats

1. **Low advisory base-rate.** Combined 1/59 (1.7%) is a thin signal. The
   per-cite survival analysis showed 34 NOT_FOUND Va. Code cites across
   1,304 total pre-firewall cites in the original 195-prompt audit (~2.6%
   of prompts had at least one). 1/59 is consistent with that prior — not
   a richer signal because Phase 5 + ec_v2_regression were not designed to
   probe the unverified-section pattern specifically.
2. **Phase 5 is uninformative for this fix in isolation.** The fix's
   non-zero rate is entirely carried by ec_v2_regression (1/9 = 11.1%)
   where edge-case prompts are more likely to elicit the
   real-title-fake-section pattern. Phase 5's 0/50 is correct null behaviour
   — it neither confirms nor refutes the fix; it confirms no spam.
3. **The strongest functional confirmation remains the engineered smoke
   test** (verified earlier, both NONEXISTENT and UNVERIFIED advisories
   firing on crafted input with a real-title-fake-section). This audit-
   subset run confirms (a) the fix path also fires in real production
   responses, (b) no regression on existing functionality, (c) no spam.
4. **Sample-id mismatch in pre-fix backup.** The pre-fix backup files
   contain accumulated rows from prior runs (152 + 27 = 179) rather than
   matched single-run datasets. The pre-vs-post comparison is therefore
   denominator-asymmetric. This is acceptable because the pre-fix rate is
   `0` (not "low" — literally zero), which is robust to denominator
   choice; the post-fix rate is positive on a fresh single run.

## Decision

The fix is functionally validated. Three independent confirmations:

1. **Engineered smoke** — UNVERIFIED + NONEXISTENT both fire on crafted
   input.
2. **Production audit subset** — Va. Code NOT_FOUND advisory rate moved
   from `0/179` to `1/59` on real CLARA responses.
3. **No regression** — NONEXISTENT path unchanged; no errors; no spurious
   advisories on 50 unrelated phase5 prompts.

Recommended next step (per architect review, not blocking publication):

- Add a focused regression unit test against `validateAllStatuteCitations`
  with engineered text covering all four buckets (valid / phantom-decimal
  / nonexistent-title / unverified-section), asserting both the bucket
  classification and the downstream advisory text.
- Add a short-term telemetry counter for `unverifiedStatuteWarnings`
  emissions per response so we can detect if corpus incompleteness
  produces excessive advisory rates in production once user traffic
  resumes.

## Files

- Post-fix results:
  `tests/hallucination-audit/results/clara/phase5.jsonl`,
  `tests/hallucination-audit/results/clara/edge_cases_v2_regression.jsonl`
- Pre-fix backup:
  `tests/hallucination-audit/results/clara/phase5.precorrection-backup.20260421-220000.jsonl`,
  `tests/hallucination-audit/results/clara/edge_cases_v2_regression.precorrection-backup.20260421-220000.jsonl`
- Runner script:
  `tests/hallucination-audit/run-postfix-verification.sh`
- Master log:
  `tests/hallucination-audit/results/clara/postfix.master.log`
