from collections import defaultdict
from app.domain.schedule import Assignment, ScheduleResult
from app.core.solver import ScheduleSolver


class SchedulerService:
    def __init__(self):
        self.solver = ScheduleSolver()

    def run(self, employees, shifts) -> ScheduleResult:
        raw = self.solver.solve(employees, shifts)

        assignments = []
        workload = defaultdict(int)

        for emp_id, shift_id, day, hours in raw:
            assignments.append(
                Assignment(emp_id, shift_id, day, hours)
            )
            workload[emp_id] += hours

        coverage = int(len(assignments) / len(shifts) * 100)

        return ScheduleResult(
            assignments=assignments,
            workload=dict(workload),
            coverage_percent=coverage,
        )
