import json
from datetime import datetime

EVENTS_FILE = "data/events.jsonl"


def log_event(event: str, meta: dict | None = None):
    record = {
        "time": datetime.utcnow().isoformat(),
        "event": event,
        "meta": meta or {},
    }
    with open(EVENTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
