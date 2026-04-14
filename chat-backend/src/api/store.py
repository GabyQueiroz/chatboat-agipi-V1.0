import json
from pathlib import Path

STORAGE_DIR = Path.cwd() / "src" / "storage"


def save_session_log(
    session_id: str,
    user_name: str,
    request_ts: str,
    question: str,
    response_ts: str,
    response: dict | None = None,
    error: str | None = None,
) -> None:
    """Append one interaction record to storage/<session_id>.json."""
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    session_file = STORAGE_DIR / f"{session_id}.json"

    if session_file.exists():
        with session_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"session_id": session_id, "user_name": user_name, "interactions": []}

    record: dict = {
        "request_timestamp": request_ts,
        "question": question,
        "response_timestamp": response_ts,
    }
    if response is not None:
        record.update(response)
    if error is not None:
        record["error"] = error

    data["interactions"].append(record)

    with session_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
