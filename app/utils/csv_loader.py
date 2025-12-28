import pandas as pd
from app.utils.time_utils import hhmm_to_minutes


def load_employees(path: str):
    df = pd.read_csv(path)

    employees = []
    for _, row in df.iterrows():
        employees.append({
            "id": row["id"],
            "skills": row["skills"].split("|"),
            "max_hours": int(row["max_hours"]),
            "days": row["days"].split("|")
        })
    return employees


def load_shifts(path: str):
    df = pd.read_csv(path)

    shifts = []
    for _, row in df.iterrows():
        start = hhmm_to_minutes(row["start"])
        end = hhmm_to_minutes(row["end"])

        duration = end - start
        if duration < 0:
            duration += 24 * 60  # ночная смена

        shifts.append({
            "id": row["id"],
            "day": row["day"],
            "start": start,
            "end": end,
            "duration": duration,
            "required_people": int(row["required_people"]),
            "required_skills": row["required_skills"].split("|"),
            "night_shift": bool(row["night_shift"])
        })
    return shifts
