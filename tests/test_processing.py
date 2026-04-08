import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2025-01-01"},
        {"id": 4, "state": "PENDING", "date": "2022-01-01"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
    ],
)
def test_filter_by_state(sample_data: list, state: str, expected_ids: list) -> None:
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_sort_by_date_desc(sample_data: list) -> None:
    result = sort_by_date(sample_data)
    dates = [item["date"] for item in result]
    assert dates == ["2025-01-01", "2024-01-01", "2023-01-01", "2022-01-01"]


def test_sort_by_date_asc(sample_data: list) -> None:
    result = sort_by_date(sample_data, descending=False)
    dates = [item["date"] for item in result]
    assert dates == ["2022-01-01", "2023-01-01", "2024-01-01", "2025-01-01"]
