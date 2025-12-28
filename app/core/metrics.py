def calculate_metrics(assignments, shifts):
    required = sum(s["required_people"] for s in shifts)
    return {
        "coverage_percent": round(len(assignments) / required * 100, 2)
        if required else 0,
        "assigned_shifts": len(assignments)
    }
