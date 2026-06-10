from pathlib import Path
from .schemas import LabReport

def build_markdown(report: LabReport) -> str:
    lines = ["# Lab Report", "", "## Context", report.context, ""]
    lines += ["## Observations"]
    lines += [f"- {o}" for o in report.observations]
    lines += ["", "## Prescriptions"]
    lines += [f"- {p}" for p in report.prescriptions]
    return "\n".join(lines)

def save_markdown_report(report: LabReport, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(build_markdown(report), encoding="utf-8")
