from unittest.mock import Mock, patch

from src.external_api import convert_currency


@patch("src.external_api.requests.get")
def test_convert_currency_usd(mock_get):
    """Тест конвертации USD → RUB."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 90.5}}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 9050.0


@patch("src.external_api.requests.get")
def test_convert_currency_eur(mock_get):
    """Тест конвертации EUR → RUB."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 95.0}}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}}
    result = convert_currency(transaction)
    assert result == 4750.0


def test_convert_currency_rub():
    """Тест: RUB не требует конвертации."""
    transaction = {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}
    result = convert_currency(transaction)
    assert result == 500.0


def test_convert_currency_missing_amount():
    """Тест: отсутствует сумма."""
    transaction = {"operationAmount": {"currency": {"code": "USD"}}}
    assert convert_currency(transaction) == 0.0


def test_convert_currency_unsupported_currency():
    """Тест: неподдерживаемая валюта."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "GBP"}}}
    assert convert_currency(transaction) == 0.0
