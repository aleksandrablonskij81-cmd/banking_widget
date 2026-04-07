"""
Тесты для модуля generators.
"""

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        },
    ]


# ==================== filter_by_currency ====================

def test_filter_by_currency_usd(sample_transactions):
    """Проверяет фильтрацию по USD."""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub(sample_transactions):
    """Проверяет фильтрацию по RUB."""
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_no_match(sample_transactions):
    """Проверяет фильтрацию при отсутствии транзакций с указанной валютой."""
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    """Проверяет фильтрацию при пустом списке транзакций."""
    result = list(filter_by_currency([], "USD"))
    assert result == []


# ==================== transaction_descriptions ====================

def test_transaction_descriptions(sample_transactions):
    """Проверяет корректность генерации описаний."""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]
    assert descriptions == expected


def test_transaction_descriptions_empty():
    """Проверяет обработку пустого списка."""
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_missing_description():
    """Проверяет, что отсутствующее описание заменяется пустой строкой."""
    transactions = [{"id": 1}, {"id": 2, "description": "Есть описание"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["", "Есть описание"]


# ==================== card_number_generator ====================

@pytest.mark.parametrize("start, stop, expected_first, expected_last", [
    (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0005"),
    (9999, 10001, "0000 0000 0000 9999", "0000 0000 0001 0001"),
])
def test_card_number_generator_range(start, stop, expected_first, expected_last):
    """Параметризованный тест диапазонов генерации номеров карт."""
    result = list(card_number_generator(start, stop))
    assert result[0] == expected_first
    assert result[-1] == expected_last


def test_card_number_generator_single():
    """Проверяет генерацию одного номера."""
    result = list(card_number_generator(42, 42))
    assert result == ["0000 0000 0000 0042"]


def test_card_number_generator_format():
    """Проверяет правильность форматирования номеров карт."""
    result = list(card_number_generator(1, 3))
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected
