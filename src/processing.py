from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по указанному статусу.

    Args:
        transactions: Список словарей с данными о транзакциях. Каждый словарь должен содержать ключ 'state'.
        state: Значение статуса для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список транзакций, содержащий только словари с ключом 'state', равным указанному значению.
    """
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Args:
        transactions: Список словарей с данными о транзакциях. Каждый словарь должен содержать ключ 'date'.
        descending: Порядок сортировки. True — по убыванию (сначала новые), False — по возрастанию (сначала старые).

    Returns:
        Новый список транзакций, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)
