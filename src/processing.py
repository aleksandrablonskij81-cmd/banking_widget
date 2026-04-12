from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по указанному статусу."""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по дате."""
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)
