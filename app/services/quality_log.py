import json
from datetime import datetime

FILE = "data/quality.jsonl"


def log_quality(metrics: dict):
    metrics["time"] = datetime.utcnow().isoformat()
    with open(FILE, "a") as f:
        f.write(json.dumps(metrics) + "\n")