"""
Модуль для чтения финансовых операций из CSV и Excel файлов.
"""

from typing import Any, Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Аргументы:
        file_path (str): Путь к CSV-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список словарей с транзакциями.
    """
    try:
        # Используем delimiter=';' потому что файл использует точку с запятой как разделитель
        df = pd.read_csv(file_path, delimiter=';')
        return df.to_dict(orient='records')
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении CSV: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Аргументы:
        file_path (str): Путь к Excel-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict(orient='records')
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении Excel: {e}")
