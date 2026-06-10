from .schemas import Evaluation, LabReport

def evaluate_report(report: LabReport) -> Evaluation:
    score = min(100, len(report.observations) * 10)
    return Evaluation(
        overall=score,
        scientific_core=score,
        evidence=score,
        protocol=score,
    )
