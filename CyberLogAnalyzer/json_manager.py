import json
from pathlib import Path
from typing import List
from log import LogEntry

DEFAULT_PATH = Path(__file__).with_name("logs.json")


def load_logs(path: str | Path | None = None) -> List[LogEntry]:
    file_path = Path(path) if path else DEFAULT_PATH
    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as handle:
        records = json.load(handle)

    return [LogEntry.from_dict(item) for item in records]


def save_logs(logs: List[LogEntry], path: str | Path | None = None) -> None:
    file_path = Path(path) if path else DEFAULT_PATH
    data = [log.to_dict() for log in logs]
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=4)


def add_log(log: LogEntry, path: str | Path | None = None) -> None:
    logs = load_logs(path)
    logs.append(log)
    save_logs(logs, path)
