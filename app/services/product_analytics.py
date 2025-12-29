import json
from collections import Counter

EVENTS_FILE = "data/events.jsonl"


def feature_usage():
    try:
        with open(EVENTS_FILE, "r") as f:
            events = [json.loads(line) for line in f]
    except FileNotFoundError:
        return {}

    return dict(Counter(e["event"] for e in events))