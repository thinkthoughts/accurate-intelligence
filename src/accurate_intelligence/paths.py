from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent.parent.parent

FIGURES = PROJECT_ROOT / "figures"
RESULTS = PROJECT_ROOT / "results"
REPORTS = PROJECT_ROOT / "reports"
SITE = PROJECT_ROOT / "site"
