import logging
import json
from pathlib import Path
from typing import Any, Dict, List

# --- Настройка логера для utils ---
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger_utils = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)

file_handler_utils = logging.FileHandler(log_dir / "utils.log", mode='w', encoding='utf-8')
file_handler_utils.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler_utils.setFormatter(file_formatter)
logger_utils.addHandler(file_handler_utils)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    logger_utils.debug(f"Попытка чтения файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger_utils.info(f"Файл {file_path} успешно прочитан. Найдено {len(data)} транзакций.")
                return data
            else:
                logger_utils.warning(f"Файл {file_path} не содержит список транзакций. Получен тип: {type(data)}")
                return []
    except FileNotFoundError as e:
        logger_utils.error(f"Файл не найден: {file_path}. Ошибка: {e}", exc_info=True)
        return []
    except json.JSONDecodeError as e:
        logger_utils.error(f"Ошибка декодирования JSON в файле {file_path}. Ошибка: {e}", exc_info=True)
        return []
    except TypeError as e:
        logger_utils.error(f"Ошибка типа при чтении файла {file_path}. Ошибка: {e}", exc_info=True)
        return []
