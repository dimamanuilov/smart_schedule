from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Assignment:
    employee_id: str
    shift_id: str
    day: str
    hours: int


@dataclass
class ScheduleResult:
    assignments: List[Assignment]
    workload: Dict[str, int]
    coverage_percent: int