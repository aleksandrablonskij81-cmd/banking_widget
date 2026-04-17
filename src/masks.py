"""
Модуль для маскировки номеров карт и счетов.
"""

import logging
from pathlib import Path

# --- Настройка логера для masks ---
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger_masks = logging.getLogger("masks")
logger_masks.setLevel(logging.DEBUG)

file_handler_masks = logging.FileHandler(log_dir / "masks.log", mode='w', encoding='utf-8')
file_handler_masks.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler_masks.setFormatter(file_formatter)
logger_masks.addHandler(file_handler_masks)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Args:
        card_number: Номер карты в виде строки

    Returns:
        str: Замаскированный номер карты в формате "XXXX XX** **** XXXX"

    Example:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    logger_masks.debug(f"Вызвана функция get_mask_card_number с номером: {card_number}")

    try:
        if len(card_number) < 16:
            logger_masks.warning(f"Номер карты слишком короткий: {len(card_number)} символов")
        elif len(card_number) > 16:
            logger_masks.warning(f"Номер карты слишком длинный: {len(card_number)} символов")

        result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger_masks.info(f"Успешно замаскирован номер карты: {result}")
        return result

    except Exception as e:
        logger_masks.error(f"Ошибка при маскировке карты: {e}", exc_info=True)
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Args:
        account_number: Номер счета в виде строки

    Returns:
        str: Замаскированный номер счета в формате "**XXXX"

    Example:
        >>> get_mask_account("73654108430135874305")
        '**4305'
    """
    logger_masks.debug(f"Вызвана функция get_mask_account с номером: {account_number}")

    try:
        if len(account_number) < 4:
            logger_masks.warning(f"Номер счета слишком короткий: {len(account_number)} символов")

        result = f"**{account_number[-4:]}"
        logger_masks.info(f"Успешно замаскирован номер счета: {result}")
        return result

    except Exception as e:
        logger_masks.error(f"Ошибка при маскировке счета: {e}", exc_info=True)
        raise
