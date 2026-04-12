import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма в рублях (float). Если валюта RUB — возвращает исходную сумму.
        Если конвертация не удалась — возвращает 0.0.
    """
    amount_str = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not amount_str or not currency:
        return 0.0

    amount = float(amount_str)

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        return 0.0

    api_key = os.getenv("API_KEY")
    if not api_key:
        return 0.0

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        rate = data.get("rates", {}).get("RUB")
        if isinstance(rate, (int, float)):
            return round(amount * rate, 2)
        return 0.0
    except (requests.RequestException, KeyError, ValueError):
        return 0.0
