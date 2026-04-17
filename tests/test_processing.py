

from src.processing import count_operations_by_category, filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции filter_by_state"""

    def test_filter_by_state_executed(self):
        """Фильтрация по статусу EXECUTED"""
        transactions = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "CANCELED", "amount": 200},
            {"state": "EXECUTED", "amount": 300},
            {"state": "PENDING", "amount": 400},
        ]
        result = filter_by_state(transactions, "EXECUTED")
        assert len(result) == 2
        assert all(item["state"] == "EXECUTED" for item in result)

    def test_filter_by_state_canceled(self):
        """Фильтрация по статусу CANCELED"""
        transactions = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "CANCELED", "amount": 200},
            {"state": "CANCELED", "amount": 300},
        ]
        result = filter_by_state(transactions, "CANCELED")
        assert len(result) == 2
        assert all(item["state"] == "CANCELED" for item in result)

    def test_filter_by_state_no_matches(self):
        """Нет транзакций с указанным статусом"""
        transactions = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "CANCELED", "amount": 200},
        ]
        result = filter_by_state(transactions, "PENDING")
        assert result == []

    def test_filter_by_state_default_value(self):
        """Проверка значения по умолчанию (EXECUTED)"""
        transactions = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "CANCELED", "amount": 200},
        ]
        result = filter_by_state(transactions)
        assert len(result) == 1
        assert result[0]["state"] == "EXECUTED"

    def test_filter_by_state_empty_list(self):
        """Пустой список транзакций"""
        result = filter_by_state([], "EXECUTED")
        assert result == []


class TestSortByDate:
    """Тесты для функции sort_by_date"""

    def test_sort_by_date_descending(self):
        """Сортировка по убыванию (сначала новые)"""
        transactions = [
            {"date": "2024-01-10", "amount": 100},
            {"date": "2024-01-01", "amount": 200},
            {"date": "2024-01-15", "amount": 300},
        ]
        result = sort_by_date(transactions, descending=True)
        assert result[0]["date"] == "2024-01-15"
        assert result[1]["date"] == "2024-01-10"
        assert result[2]["date"] == "2024-01-01"

    def test_sort_by_date_ascending(self):
        """Сортировка по возрастанию (сначала старые)"""
        transactions = [
            {"date": "2024-01-10", "amount": 100},
            {"date": "2024-01-01", "amount": 200},
            {"date": "2024-01-15", "amount": 300},
        ]
        result = sort_by_date(transactions, descending=False)
        assert result[0]["date"] == "2024-01-01"
        assert result[1]["date"] == "2024-01-10"
        assert result[2]["date"] == "2024-01-15"

    def test_sort_by_date_default_value(self):
        """Проверка значения по умолчанию (descending=True)"""
        transactions = [
            {"date": "2024-01-01", "amount": 100},
            {"date": "2024-01-15", "amount": 200},
        ]
        result = sort_by_date(transactions)
        assert result[0]["date"] == "2024-01-15"
        assert result[1]["date"] == "2024-01-01"

    def test_sort_by_date_single_element(self):
        """Один элемент в списке"""
        transactions = [{"date": "2024-01-10", "amount": 100}]
        result = sort_by_date(transactions)
        assert len(result) == 1
        assert result[0]["date"] == "2024-01-10"

    def test_sort_by_date_empty_list(self):
        """Пустой список"""
        result = sort_by_date([])
        assert result == []


class TestCountOperationsByCategory:
    """Тесты для функции count_operations_by_category"""

    def test_count_operations_success(self):
        """Успешный подсчёт категорий"""
        transactions = [
            {"description": "Перевод на карту. Покупка продуктов"},
            {"description": "Оплата коммунальных услуг"},
            {"description": "Перевод другу. Продукты"},
            {"description": "Покупка билетов"},
            {"description": "Оплата услуг связи"},
        ]
        # Ищем основы слов, которые реально есть в описаниях
        categories = ["продукт", "услуг", "билетов"]

        result = count_operations_by_category(transactions, categories)

        assert result["продукт"] == 2
        assert result["услуг"] == 2
        assert result["билетов"] == 1

    def test_count_operations_case_insensitive(self):
        """Проверка регистронезависимости"""
        transactions = [
            {"description": "ПРОДУКТЫ и Еда"},
            {"description": "Продукты питания"},
            {"description": "продукты из магазина"},
        ]
        categories = ["продукты"]

        result = count_operations_by_category(transactions, categories)

        assert result["продукты"] == 3

    def test_count_operations_partial_match(self):
        """Частичное совпадение в описании"""
        transactions = [
            {"description": "Перевод на карту"},
            {"description": "Оплата услуг"},
        ]
        # Ищем основы слов
        categories = ["карт", "услуг"]

        result = count_operations_by_category(transactions, categories)

        assert result["карт"] == 1
        assert result["услуг"] == 1

    def test_count_operations_no_matches(self):
        """Нет совпадений с категориями"""
        transactions = [
            {"description": "Перевод другу"},
            {"description": "Покупка в магазине"},
        ]
        categories = ["услуги", "билеты"]

        result = count_operations_by_category(transactions, categories)

        assert result["услуги"] == 0
        assert result["билеты"] == 0

    def test_count_operations_empty_transactions(self):
        """Пустой список транзакций"""
        result = count_operations_by_category([], ["продукты", "услуги"])
        assert result == {"продукты": 0, "услуги": 0}

    def test_count_operations_empty_categories(self):
        """Пустой список категорий"""
        transactions = [{"description": "Покупка продуктов"}]
        result = count_operations_by_category(transactions, [])
        assert result == {}

    def test_count_operations_missing_description(self):
        """Транзакции без поля description"""
        transactions = [
            {"amount": 100},
            {"description": "Покупка продуктов"},
            {"amount": 200},
        ]
        categories = ["продукт"]

        result = count_operations_by_category(transactions, categories)

        assert result["продукт"] == 1
