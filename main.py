from src.masks import get_mask_card_number, get_mask_account


def main():
    """Основная функция для демонстрации работы маскировки."""
    card_number = "7000792289606361"  # теперь строка
    account_number = "73654108430135874305"  # теперь строка

    print(f"Номер карты: {card_number}")
    print(f"Замаскированная карта: {get_mask_card_number(card_number)}")
    print(f"Номер счета: {account_number}")
    print(f"Замаскированный счет: {get_mask_account(account_number)}")


if __name__ == "__main__":
    main()
