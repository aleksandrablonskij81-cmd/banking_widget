"""
Модуль с декоратором логирования.
"""

import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функции в файл или консоль.

    Args:
        filename: Имя файла для записи логов. Если не указан, логи выводятся в консоль.

    Returns:
        Декоратор, оборачивающий функцию.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
