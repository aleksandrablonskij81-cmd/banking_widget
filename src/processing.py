"""
Модуль для обработки банковских транзакций.
Содержит функции фильтрации, сортировки и подсчёта категорий.
"""

from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по указанному статусу.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
        state (str): Статус для фильтрации. По умолчанию "EXECUTED".

    Возвращает:
        List[Dict[str, Any]]: Отфильтрованный список транзакций.
    """
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
        descending (bool): Если True — сортировка по убыванию (сначала новые),
                           если False — по возрастанию (сначала старые).

    Возвращает:
        List[Dict[str, Any]]: Отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой из указанных категорий на основе поля description.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
        categories (List[str]): Список категорий для подсчёта.

    Возвращает:
        Dict[str, int]: Словарь, где ключ — категория, значение — количество операций.
    """
    # Создаём словарь с нулями для всех категорий
    result = {}
    for category in categories:
        result[category] = 0

    # Если транзакций нет, возвращаем нули
    if not transactions:
        return result

    # Проходим по каждой транзакции
    for transaction in transactions:
        description = transaction.get('description', '')
        if not description:
            continue

        # Приводим к нижнему регистру
        desc_lower = description.lower()

        # Проверяем каждую категорию
        for category in categories:
            cat_lower = category.lower()
            # Ищем как часть слова (например, "продукт" найдёт "продукты", "продуктов")
            if cat_lower in desc_lower:
                result[category] += 1

    return result
