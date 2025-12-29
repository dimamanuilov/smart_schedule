from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    id: str
    skills: List[str]
    max_hours: int
    days: List[str]


@dataclass
class Shift:
    id: str
    day: str
    start: int
    end: int
    required_people: int
    required_skills: List[str]

    @property
    def hours(self) -> int:
        return (self.end - self.start) // 60
