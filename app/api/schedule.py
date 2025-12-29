from fastapi import APIRouter
from app.utils.csv_loader import load_employees, load_shifts
from app.services.scheduler import SchedulerService
from app.services.events import log_event

router = APIRouter()
service = SchedulerService()


@router.post("/schedule/solve")
def solve():
    log_event("RUN_SOLVER")

    employees = load_employees("data/employees.csv")
    shifts = load_shifts("data/shifts.csv")

    result = service.run(employees, shifts)

    return result