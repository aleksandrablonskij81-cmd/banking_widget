from typing import Any, Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    try:
        df = pd.read_csv(file_path)
        result = df.to_dict(orient='records')
        return result  # type: ignore
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении CSV: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        result = df.to_dict(orient='records')
        return result  # type: ignore
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении Excel: {e}")
