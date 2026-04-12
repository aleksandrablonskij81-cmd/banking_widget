"""
Модуль с генераторами для работы с транзакциями.
"""

from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список словарей с данными о транзакциях.
        currency_code: Код валюты для фильтрации (например, 'USD').

    Returns:
        Итератор, выдающий транзакции с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список словарей с данными о транзакциях.

    Returns:
        Итератор строк с описаниями транзакций.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальное значение диапазона.
        stop: Конечное значение диапазона.

    Returns:
        Итератор строк с номерами карт в формате "XXXX XXXX XXXX XXXX".
    """
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = " ".join(card_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted
