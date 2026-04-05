import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-01T00:00:00", "01.12.2025"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
