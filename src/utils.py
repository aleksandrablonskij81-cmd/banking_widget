import json
from typing import Any, Dict, List


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return []
