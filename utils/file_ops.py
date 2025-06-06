from typing import List, Any
import json


def read_json(file_path: str) -> List[Any]:
    try:
        with open(file_path, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def write_json(file_path: str, data: List[Any]):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, default=str)
