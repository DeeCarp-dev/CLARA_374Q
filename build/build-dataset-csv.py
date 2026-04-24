#!/usr/bin/env python3
"""
Build a single-file CSV dataset for OSF upload.

One row per prompt (374 total), with the prompt and parallel responses
from three arms (CLARA post-fix, CLARA pre-correction, bare-LLM baseline)
side-by-side as columns. Citation lists are JSON-encoded; long text
columns are kept verbatim. Opens in Excel, pandas, R, etc.

Output: tests/hallucination-audit/clara-audit-dataset-374queries.csv
"""
from __future__ import annotations
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
PROMPTS = ROOT / "prompts"

PHASES = [
    ("baseline", 30),
    ("edge_cases_v1", 15),
    ("edge_cases_v2_regression", 9),
    ("phase2", 120),
    ("phase3", 100),
    ("phase4", 50),
    ("phase5", 50),
]
EXPECTED_TOTAL = sum(n for _, n in PHASES)  # 374

OUT = ROOT / "clara-audit-dataset-374queries.csv"


def dedup_clean(path: Path) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        r = json.loads(ln)
        rid = r["id"]
        is_clean = not (r.get("errors") or [])
        existing = by_id.get(rid)
        if existing is None:
            by_id[rid] = r
            continue
        existing_clean = not (existing.get("errors") or [])
        if is_clean and not existing_clean:
            by_id[rid] = r
        elif is_clean and existing_clean:
            if (r.get("finishedAt") or "") > (existing.get("finishedAt") or ""):
                by_id[rid] = r
    return by_id


def jdump(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (str, int, float, bool)):
        return v if isinstance(v, str) else str(v)
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


COLUMNS = [
    # prompt
    "id", "phase", "prompt", "mode", "domain", "tags", "expected_authorities",
    # CLARA post-fix
    "clara_postfix_pre_correction_text",
    "clara_postfix_response_text",
    "clara_postfix_warnings",
    "clara_postfix_extracted_citations",
    "clara_postfix_extracted_citations_count",
    "clara_postfix_responsible_layers",
    "clara_postfix_findings",
    "clara_postfix_latency_ms",
    # CLARA pre-correction
    "clara_precorrection_pre_correction_text",
    "clara_precorrection_response_text",
    "clara_precorrection_warnings",
    "clara_precorrection_extracted_citations",
    "clara_precorrection_extracted_citations_count",
    "clara_precorrection_findings",
    "clara_precorrection_latency_ms",
    # baseline LLM
    "baseline_llm_model",
    "baseline_llm_temperature",
    "baseline_llm_response_text",
    "baseline_llm_extracted_citations",
    "baseline_llm_extracted_citations_count",
    "baseline_llm_input_tokens",
    "baseline_llm_output_tokens",
    "baseline_llm_latency_ms",
    # precheck (post-fix)
    "precheck_va_code_checked",
    "precheck_va_code_verified",
    "precheck_va_code_not_found",
    "precheck_case_checked",
    "precheck_case_verified",
    "precheck_case_not_found",
]


def main() -> int:
    rows_written = 0
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL)
        w.writerow(COLUMNS)

        for phase, expected_n in PHASES:
            prompts_path = PROMPTS / f"{phase}.jsonl"
            postfix_path = RESULTS / "clara" / f"{phase}.jsonl"
            postfix_chk = RESULTS / "clara" / f"{phase}.checked.jsonl"
            precorr_path = RESULTS / "clara-precorrection" / f"{phase}.jsonl"
            baseline_path = RESULTS / f"baseline-llm.{phase}.jsonl"

            prompts = {}
            for l in prompts_path.read_text().splitlines():
                l = l.strip()
                if not l or l.startswith("//"):
                    continue
                p = json.loads(l)
                prompts[p["id"]] = p
            postfix = dedup_clean(postfix_path)
            postfix_checked = dedup_clean(postfix_chk)
            precorr = dedup_clean(precorr_path)
            baseline = dedup_clean(baseline_path)

            for arm_name, arm in [("postfix", postfix), ("precorrection", precorr),
                                  ("baseline-llm", baseline)]:
                if len(arm) != expected_n:
                    print(f"WARN {phase}/{arm_name}: {len(arm)} rows (expected {expected_n})",
                          file=sys.stderr)

            for pid in sorted(prompts):
                p = prompts[pid]
                pf = postfix.get(pid, {})
                pfc = postfix_checked.get(pid, {})
                pc = precorr.get(pid, {})
                bl = baseline.get(pid, {})
                pcheck = pfc.get("precheck") or {}

                pf_cites = pf.get("extractedCitations") or []
                pc_cites = pc.get("extractedCitations") or []
                bl_cites = bl.get("extractedCitations") or []

                row = [
                    pid,
                    phase,
                    p.get("prompt", ""),
                    p.get("mode", ""),
                    p.get("domain", ""),
                    jdump(p.get("tags")),
                    jdump(p.get("expected_authorities")),
                    pf.get("preCorrectionText", ""),
                    pf.get("responseText", ""),
                    jdump(pf.get("warnings")),
                    jdump(pf_cites),
                    len(pf_cites),
                    jdump(pf.get("responsibleLayers")),
                    jdump(pf.get("findings")),
                    pf.get("latencyMs", ""),
                    pc.get("preCorrectionText", ""),
                    pc.get("responseText", ""),
                    jdump(pc.get("warnings")),
                    jdump(pc_cites),
                    len(pc_cites),
                    jdump(pc.get("findings")),
                    pc.get("latencyMs", ""),
                    bl.get("model", ""),
                    bl.get("temperature", ""),
                    bl.get("responseText", ""),
                    jdump(bl_cites),
                    len(bl_cites),
                    bl.get("inputTokens", ""),
                    bl.get("outputTokens", ""),
                    bl.get("latencyMs", ""),
                    pcheck.get("vaCodeChecked", ""),
                    pcheck.get("vaCodeVerified", ""),
                    pcheck.get("vaCodeNotFound", ""),
                    pcheck.get("caseChecked", ""),
                    pcheck.get("caseVerified", ""),
                    pcheck.get("caseNotFound", ""),
                ]
                w.writerow(row)
                rows_written += 1

    # PII sweep
    text = OUT.read_text(encoding="utf-8")
    for needle in ["attorney@aequuslaw.com", "CLARA_TEST_PASSWORD",
                   "CLARA_TEST_2FA_CODE", "ABSTRACT_API_KEY", "MAPBOX_ACCESS_TOKEN"]:
        if needle in text:
            print(f"ABORT: forbidden string '{needle}' present in CSV", file=sys.stderr)
            return 2

    if rows_written != EXPECTED_TOTAL:
        print(f"ABORT: wrote {rows_written} rows, expected {EXPECTED_TOTAL}", file=sys.stderr)
        return 3

    size_mb = OUT.stat().st_size / 1_048_576
    print(f"DONE: {rows_written} rows, {len(COLUMNS)} columns, {size_mb:.2f} MB")
    print(f"output: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
