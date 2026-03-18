"""
Модуль для маскировки номеров карт и счетов.
"""


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
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


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
    return f"**{account_number[-4:]}"