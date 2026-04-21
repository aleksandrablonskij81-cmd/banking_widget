"""
Основной модуль программы.
Содержит пользовательский интерфейс для работы с транзакциями.
"""

import json

from src.file_operation import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import search_transactions_by_description


def load_transactions() -> list:
    """
    Загружает транзакции из выбранного пользователем источника.

    Returns:
        list: Список транзакций или пустой список при ошибке.
    """
    print("\nВыберите источник данных:")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. XLSX-файл")

    choice = input("Ваш выбор (1/2/3): ").strip()

    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ").strip()
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    print(f"Загружено {len(data)} транзакций из JSON")
                    return data
                else:
                    print("Ошибка: JSON-файл должен содержать список транзакций")
                    return []
        except FileNotFoundError:
            print(f"Ошибка: Файл {file_path} не найден")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка: Файл {file_path} содержит некорректный JSON")
            return []

    elif choice == "2":
        file_path = input("Введите путь к CSV-файлу: ").strip()
        try:
            data = read_transactions_from_csv(file_path)
            print(f"Загружено {len(data)} транзакций из CSV")
            return data
        except Exception as e:
            print(f"Ошибка при чтении CSV: {e}")
            return []

    elif choice == "3":
        file_path = input("Введите путь к XLSX-файлу: ").strip()
        try:
            data = read_transactions_from_excel(file_path)
            print(f"Загружено {len(data)} транзакций из XLSX")
            return data
        except Exception as e:
            print(f"Ошибка при чтении XLSX: {e}")
            return []

    else:
        print("Неверный выбор. Загрузка отменена.")
        return []


def filter_by_status_menu(transactions: list) -> list:
    """
    Меню фильтрации транзакций по статусу.

    Args:
        transactions: Список транзакций.

    Returns:
        list: Отфильтрованный список транзакций.
    """
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nДоступные статусы: EXECUTED, CANCELED, PENDING")
        status = input("Введите статус для фильтрации (или 'пропустить'): ").strip().upper()

        if status == "ПРОПУСТИТЬ" or status == "SKIP":
            print("Фильтрация по статусу пропущена")
            return transactions

        if status in valid_statuses:
            filtered = filter_by_state(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            print(f"Найдено {len(filtered)} транзакций из {len(transactions)}")
            return filtered
        else:
            print(f'Статус операции "{status}" недоступен. Попробуйте снова.')


def sort_by_date_menu(transactions: list) -> list:
    """
    Меню сортировки транзакций по дате.

    Args:
        transactions: Список транзакций.

    Returns:
        list: Отсортированный список транзакций.
    """
    choice = input("\nОтсортировать операции по дате? (да/нет): ").strip().lower()

    if choice in ["да", "yes", "y", "д"]:
        order = input("По возрастанию или по убыванию? (возрастание/убывание): ").strip().lower()
        descending = order in ["убывание", "desc", "убыв", "убыванию"]
        transactions = sort_by_date(transactions, descending)
        print(f"Транзакции отсортированы по {'убыванию' if descending else 'возрастанию'} даты")

    return transactions


def search_by_description_menu(transactions: list) -> list:
    """
    Меню поиска транзакций по описанию.

    Args:
        transactions: Список транзакций.

    Returns:
        list: Отфильтрованный список транзакций.
    """
    choice = input("\nОтфильтровать список транзакций по определенному слову в описании? (да/нет): ").strip().lower()

    if choice in ["да", "yes", "y", "д"]:
        search_word = input("Введите слово для поиска: ").strip()
        if search_word:
            filtered = search_transactions_by_description(transactions, search_word)
            print(f"Найдено {len(filtered)} транзакций по слову '{search_word}'")
            return filtered
        else:
            print("Слово не введено, поиск пропущен")

    return transactions


def print_transactions(transactions: list):
    """
    Выводит транзакции в отформатированном виде.

    Args:
        transactions: Список транзакций.
    """
    print("\n" + "=" * 60)
    print(f"ВСЕГО БАНКОВСКИХ ОПЕРАЦИЙ В ВЫБОРКЕ: {len(transactions)}")
    print("=" * 60)

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    for i, tx in enumerate(transactions[:20], 1):
        date = tx.get("date", "Нет даты")[:10] if tx.get("date") else "Нет даты"
        description = tx.get("description", "Нет описания")
        amount = tx.get("amount", 0)
        currency = tx.get("currency_name", "руб.")

        print(f"{i}. {date} - {description}")
        print(f"   Сумма: {amount} {currency}")
        print()

    if len(transactions) > 20:
        print(f"... и ещё {len(transactions) - 20} транзакций")


def main():
    """Основная функция программы."""
    print("\n" + "=" * 60)
    print("ПРИВЕТ! ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ РАБОТЫ С БАНКОВСКИМИ ТРАНЗАКЦИЯМИ.")
    print("=" * 60)

    transactions = load_transactions()
    if not transactions:
        print("Не удалось загрузить транзакции. Завершение работы.")
        return

    transactions = filter_by_status_menu(transactions)
    if not transactions:
        print("После фильтрации не осталось транзакций.")
        return

    transactions = sort_by_date_menu(transactions)
    transactions = search_by_description_menu(transactions)
    print_transactions(transactions)


if __name__ == "__main__":
    main()
