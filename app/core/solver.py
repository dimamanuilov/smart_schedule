from ortools.sat.python import cp_model


def solve_schedule(employees, shifts):
    model = cp_model.CpModel()
    x = {}

    for e in employees:
        for s in shifts:
            x[e["id"], s["id"]] = model.NewBoolVar(
                f"x_{e['id']}_{s['id']}"
            )

    # Каждая смена должна быть покрыта
    for s in shifts:
        model.Add(
            sum(x[e["id"], s["id"]] for e in employees)
            == s["required_people"]
        )

    # Ограничение по часам
    for e in employees:
        model.Add(
            sum(
                x[e["id"], s["id"]] * s["duration"]
                for s in shifts
            ) <= e["max_hours"] * 60
        )

    # Навыки и дни
    for e in employees:
        for s in shifts:
            if not set(s["required_skills"]).issubset(e["skills"]):
                model.Add(x[e["id"], s["id"]] == 0)

            if s["day"] not in e["days"]:
                model.Add(x[e["id"], s["id"]] == 0)

    # Минимизируем ночные смены
    model.Minimize(
        sum(
            x[e["id"], s["id"]] * (3 if s["night_shift"] else 0)
            for e in employees
            for s in shifts
        )
    )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 5

    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return []

    assignments = []
    for e in employees:
        for s in shifts:
            if solver.Value(x[e["id"], s["id"]]) == 1:
                assignments.append({
                    "employee": e["id"],
                    "shift": s["id"]
                })

    return assignments
