"""
Модуль для маскировки счетов и карт.
"""


from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Args:
        info: Строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером

    Примеры:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    # Разделяем строку на части
    parts = info.split()

    # Если есть слово "Счет" — это счет
    if parts[0].lower() == "счет":
        account_number = parts[-1]
        masked = get_mask_account(account_number)
        return f"Счет {masked}"
    else:
        # Это карта — всё кроме последнего слова — название, последнее слово — номер
        card_name = " ".join(parts[:-1])
        card_number = parts[-1]
        masked = get_mask_card_number(card_number)
        return f"{card_name} {masked}"

if __name__ == "__main__":
        print(mask_account_card("Visa Platinum 7000792289606361"))
        print(mask_account_card("Счет 73654108430135874305"))
        print(mask_account_card("Maestro 1596837868705199"))

