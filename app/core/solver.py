from ortools.sat.python import cp_model
from app.domain.models import Employee, Shift


class ScheduleSolver:
    def solve(self, employees: list[Employee], shifts: list[Shift]):
        model = cp_model.CpModel()
        x = {}

        for e in employees:
            for s in shifts:
                x[e.id, s.id] = model.NewBoolVar(f"x_{e.id}_{s.id}")

        # покрытие смен
        for s in shifts:
            model.Add(
                sum(x[e.id, s.id] for e in employees) == s.required_people
            )

        # часы
        for e in employees:
            model.Add(
                sum(x[e.id, s.id] * s.hours for s in shifts)
                <= e.max_hours
            )

        # навыки и доступность
        for e in employees:
            for s in shifts:
                if not set(s.required_skills).issubset(e.skills):
                    model.Add(x[e.id, s.id] == 0)
                if s.day not in e.days:
                    model.Add(x[e.id, s.id] == 0)

        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 5
        status = solver.Solve(model)

        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return []

        return [
            (e.id, s.id, s.day, s.hours)
            for e in employees
            for s in shifts
            if solver.Value(x[e.id, s.id]) == 1
        ]
