
"""
Тесты для модуля utils.
"""


from src.utils import read_json_file, search_transactions_by_description

# ==================== ТЕСТЫ ДЛЯ read_json_file ====================


def test_read_json_file_success(tmp_path):
    """Тест успешного чтения JSON-файла."""
    test_file = tmp_path / "test.json"
    test_file.write_text('[{"id": 1, "amount": 100}]', encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == [{"id": 1, "amount": 100}]


def test_read_json_file_not_found():
    """Тест отсутствующего файла."""
    data = read_json_file("not_found.json")
    assert data == []


def test_read_json_file_invalid_json(tmp_path):
    """Тест некорректного JSON."""
    test_file = tmp_path / "invalid.json"
    test_file.write_text("not a json", encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == []


def test_read_json_file_not_list(tmp_path):
    """Тест, когда JSON — не список."""
    test_file = tmp_path / "not_list.json"
    test_file.write_text('{"key": "value"}', encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == []


# ==================== ТЕСТЫ ДЛЯ search_transactions_by_description ====================

def test_search_success():
    """Успешный поиск по описанию"""
    transactions = [
        {"description": "Перевод на карту. Покупка продуктов"},
        {"description": "Оплата коммунальных услуг"},
        {"description": "Перевод другу. Продукты"},
    ]
    result = search_transactions_by_description(transactions, "продукт")
    assert len(result) == 2


def test_search_no_matches():
    """Нет совпадений"""
    transactions = [
        {"description": "Перевод на карту"},
        {"description": "Оплата услуг"},
    ]
    result = search_transactions_by_description(transactions, "билеты")
    assert result == []


def test_search_case_insensitive():
    """Регистронезависимый поиск"""
    transactions = [
        {"description": "ПЕРЕВОД на карту"},
        {"description": "перевод другу"},
    ]
    result = search_transactions_by_description(transactions, "Перевод")
    assert len(result) == 2


def test_search_empty_string():
    """Пустая строка поиска"""
    transactions = [{"description": "Перевод"}]
    result = search_transactions_by_description(transactions, "")
    assert result == transactions


def test_search_empty_transactions():
    """Пустой список транзакций"""
    result = search_transactions_by_description([], "поиск")
    assert result == []


def test_search_partial_word():
    """Поиск по части слова"""
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Продуктовый магазин"},
        {"description": "Оплата услуг"},
    ]
    result = search_transactions_by_description(transactions, "продукт")
    assert len(result) == 2


def test_search_with_special_chars():
    """Поиск с специальными символами"""
    transactions = [
        {"description": "Перевод (срочный)"},
        {"description": "Оплата [услуг]"},
    ]
    result = search_transactions_by_description(transactions, "(срочный)")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод (срочный)"
