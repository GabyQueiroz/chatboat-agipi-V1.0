import json
from pathlib import Path

STORAGE_DIR = Path.cwd() / "src" / "storage"


def save_session_log(
    session_id: str,
    user_name: str,
    interaction_id: str,
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
        "interaction_id": interaction_id,
        "request_timestamp": request_ts,
        "question": question,
        "response_timestamp": response_ts,
        "feedback": {
            "relevance": 0,
            "comment": "",
        }
    }
    if response is not None:
        record.update(response)
    if error is not None:
        record["error"] = error

    data["interactions"].append(record)

    with session_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_interaction_feedback(
    session_id: str,
    interaction_id: str,
    relevance: int,
    comment: str,
) -> dict:
    """Update feedback for a specific interaction.
    
    Args:
        session_id: The session ID to locate the session file
        interaction_id: The interaction ID to update
        relevance: Relevance score (-1, 0, 1)
        comment: User comment (will be truncated to 5000 chars)
    
    Returns:
        Updated feedback dictionary
    
    Raises:
        FileNotFoundError: If session file doesn't exist
        ValueError: If interaction not found in session
    """
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    session_file = STORAGE_DIR / f"{session_id}.json"
    
    if not session_file.exists():
        raise FileNotFoundError(f"Session {session_id} not found")
    
    with session_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Find the interaction
    interaction = None
    for record in data.get("interactions", []):
        if record.get("interaction_id") == interaction_id:
            interaction = record
            break
    
    if interaction is None:
        raise ValueError(f"Interaction {interaction_id} not found in session {session_id}")
    
    # Validate and update feedback
    if relevance not in (-1, 0, 1):
        raise ValueError(f"Invalid relevance value: {relevance}. Must be -1, 0, or 1")
    
    if not isinstance(comment, str):
        raise ValueError("Comment must be a string")
    
    # Truncate comment
    comment = comment[:5000]
    
    # Initialize feedback if not exists 
    if "feedback" not in interaction:
        interaction["feedback"] = {"relevance": 0, "comment": ""}
    
    # Update feedback
    interaction["feedback"]["relevance"] = relevance
    interaction["feedback"]["comment"] = comment
    
    # Write back to file
    with session_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return interaction["feedback"]
