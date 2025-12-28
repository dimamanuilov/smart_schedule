from fastapi import APIRouter
from app.utils.csv_loader import load_employees, load_shifts
from app.core.solver import solve_schedule
from app.core.metrics import calculate_metrics
import pandas as pd

router = APIRouter()


@router.post("/schedule/solve")
def solve():
    employees = load_employees("data/employees.csv")
    shifts = load_shifts("data/shifts.csv")

    assignments = solve_schedule(employees, shifts)

    if not assignments:
        return {"error": "No feasible schedule"}

    metrics = calculate_metrics(assignments, shifts)

    pd.DataFrame(assignments).to_csv(
        "data/output_schedule.csv", index=False
    )

    return {
        "assignments": assignments,
        "metrics": metrics
    }
