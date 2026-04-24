# CLARA Per-Cite Survival Analysis

**Scope:** 195 CLARA prompts where preCorrectionText ≠ responseText
**Generated:** 2026-04-21T18:44:56.233Z

## Method

For every prompt where the firewall modified the response, every
pre-firewall citation is matched against the post-firewall citation list
by `(kind, normalized_form)`. A pre-cite is **survived** if the same
`(kind, normalized_form)` pair appears at least once in the post-cite
list; otherwise it is **dropped**. The verification status assigned by
precheck is preserved, so we can answer: *of the cites the firewall
chose to drop, what verification status did they have?*

## Survival rate by (kind × verification_status)

| Kind | Verification status | Pre cites | Dropped | Survived | Drop rate |
|---|---|---:|---:|---:|---:|
| case | NOT_FOUND | 389 | 62 | 327 | 15.9% |
| case | VERIFIED_CASE | 105 | 11 | 94 | 10.5% |
| rule | UNCHECKED | 387 | 0 | 387 | 0.0% |
| va_code | NOT_FOUND | 34 | 0 | 34 | 0.0% |
| va_code | VERIFIED_STATUTE | 389 | 14 | 375 | 3.6% |
| **TOTAL** | — | **1304** | **87** | **1217** | **6.7%** |

## How to read this

- A firewall designed to *preferentially drop hallucinated cites* should
  show a **higher drop rate for NOT_FOUND than for VERIFIED_** rows.
- A firewall that *drops content indiscriminately* should show roughly
  equal drop rates across statuses.
- A firewall with *collateral damage* should show drop rates for
  VERIFIED_ rows that are non-trivial (>10%).

### Key derived ratios
- **Cases**: NOT_FOUND drop rate = 15.9%, VERIFIED drop rate = 10.5%
- **Va. Code**: NOT_FOUND drop rate = 0.0%, VERIFIED drop rate = 3.6%

## Sample of dropped citations (first 30)

| Prompt | Kind | Normalized | Status |
|---|---|---|---|
| base-005 | case | 269 Va. 383 | NOT_FOUND |
| base-015 | case | 221 Va. 43 | NOT_FOUND |
| base-015 | case | 221 Va. 43 | NOT_FOUND |
| base-015 | case | 221 Va. 43 | NOT_FOUND |
| base-015 | case | 228 Va. 301 | VERIFIED_CASE |
| base-015 | case | 228 Va. 301 | VERIFIED_CASE |
| base-015 | case | 228 Va. 301 | VERIFIED_CASE |
| base-016 | case | 263 Va. 555 | VERIFIED_CASE |
| p2-020 | case | 273 Va. 458 | NOT_FOUND |
| p2-023 | case | 273 Va. 458 | NOT_FOUND |
| p2-032 | case | 269 Va. 383 | NOT_FOUND |
| p2-063 | case | 294 Va. 544 | NOT_FOUND |
| p2-063 | case | 294 Va. 544 | NOT_FOUND |
| p2-071 | case | 265 Va. 127 | NOT_FOUND |
| p2-071 | case | 290 Va. 83 | NOT_FOUND |
| p2-072 | case | 290 Va. 83 | NOT_FOUND |
| p2-077 | case | 265 Va. 127 | NOT_FOUND |
| p2-077 | case | 290 Va. 83 | NOT_FOUND |
| p2-079 | case | 265 Va. 127 | NOT_FOUND |
| p2-081 | case | 290 Va. 83 | NOT_FOUND |
| p2-082 | case | 290 Va. 83 | NOT_FOUND |
| p2-084 | case | 265 Va. 127 | NOT_FOUND |
| p2-084 | case | 290 Va. 83 | NOT_FOUND |
| p2-102 | case | 218 Va. 670 | NOT_FOUND |
| p2-102 | case | 278 Va. 624 | NOT_FOUND |
| p2-103 | case | 240 Va. 78 | NOT_FOUND |
| p2-103 | case | 251 Va. 442 | VERIFIED_CASE |
| p2-110 | case | 279 Va. 175 | VERIFIED_CASE |
| p2-111 | case | 259 Va. 356 | NOT_FOUND |
| p2-114 | case | 52 Va. App. 637 | NOT_FOUND |
