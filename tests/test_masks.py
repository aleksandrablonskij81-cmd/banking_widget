import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return {
        "valid": "7000792289606361",
        "short": "1234",
        "long": "12345678901234567890",
    }


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short(card_numbers: dict) -> None:
    assert get_mask_card_number(card_numbers["short"]) == "1234 ** **** 1234"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678", "**5678"),
        ("0000", "**0000"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
