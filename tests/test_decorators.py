"""
Тесты для декоратора log.
"""

import os

import pytest

from src.decorators import log


@log()
def add_success(a: int, b: int) -> int:
    """Функция для тестирования успешного выполнения."""
    return a + b


@log()
def divide_error(a: int, b: int) -> float:
    """Функция для тестирования ошибки."""
    return a / b


@log(filename="test_log.txt")
def multiply_with_file(a: int, b: int) -> int:
    """Функция для тестирования записи в файл."""
    return a * b


def test_log_success_console(capsys: pytest.CaptureFixture) -> None:
    """Тест успешного выполнения и вывода в консоль."""
    result = add_success(3, 5)
    assert result == 8
    captured = capsys.readouterr()
    assert captured.out == "add_success ok\n"


def test_log_error_console(capsys: pytest.CaptureFixture) -> None:
    """Тест ошибки и вывода в консоль."""
    with pytest.raises(ZeroDivisionError):
        divide_error(10, 0)
    captured = capsys.readouterr()
    assert "divide_error error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


def test_log_success_to_file() -> None:
    """Тест успешного выполнения и записи в файл."""
    result = multiply_with_file(4, 5)
    assert result == 20
    assert os.path.exists("test_log.txt")
    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "multiply_with_file ok" in content
    os.remove("test_log.txt")


def test_log_error_to_file() -> None:
    """Тест ошибки и записи в файл."""

    @log(filename="test_error.txt")
    def bad_function(x: int) -> int:
        return x // 0

    with pytest.raises(ZeroDivisionError):
        bad_function(42)
    assert os.path.exists("test_error.txt")
    with open("test_error.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "bad_function error: ZeroDivisionError. Inputs: (42,), {}" in content
    os.remove("test_error.txt")
