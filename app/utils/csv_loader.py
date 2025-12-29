import pandas as pd
from app.domain.models import Employee, Shift


def to_minutes(value: str) -> int:
    h, m = value.split(":")
    return int(h) * 60 + int(m)


def load_employees(path: str) -> list[Employee]:
    df = pd.read_csv(path)
    return [
        Employee(
            id=row["id"],
            skills=row["skills"].split("|"),
            max_hours=int(row["max_hours"]),
            days=row["days"].split("|"),
        )
        for _, row in df.iterrows()
    ]


def load_shifts(path: str) -> list[Shift]:
    df = pd.read_csv(path)
    return [
        Shift(
            id=row["id"],
            day=row["day"],
            start=to_minutes(row["start"]),
            end=to_minutes(row["end"]),
            required_people=int(row["required_people"]),
            required_skills=row["required_skills"].split("|"),
        )
        for _, row in df.iterrows()
    ]