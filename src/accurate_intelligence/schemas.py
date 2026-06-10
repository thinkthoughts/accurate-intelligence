from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Claim:
    text: str
    evidence: List[str] = field(default_factory=list)
    figure_ids: List[str] = field(default_factory=list)

@dataclass
class Evidence:
    text: str
    source: str = ""

@dataclass
class Figure:
    identifier: str
    caption: str = ""

@dataclass
class Paper:
    title: str
    authors: List[str] = field(default_factory=list)
    abstract: str = ""
    sections: Dict[str, str] = field(default_factory=dict)

@dataclass
class Evaluation:
    overall: float = 0.0
    scientific_core: float = 0.0
    evidence: float = 0.0
    protocol: float = 0.0

@dataclass
class LabReport:
    context: str = ""
    observations: List[str] = field(default_factory=list)
    prescriptions: List[str] = field(default_factory=list)
