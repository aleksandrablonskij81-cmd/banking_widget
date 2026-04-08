# Banking Widget

Проект для маскировки банковских карт и счетов, а также фильтрации и сортировки операций.

## Цель проекта

Учебный проект для отработки навыков работы с Git, GitHub, ветками, pull request, а также написания чистого кода на Python с использованием линтеров.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aleksandrablonskij81-cmd/banking_widget.git
   cd banking_widget
   ```

2. Установите зависимости через Poetry:
   ```bash
   poetry install
   ```

## Использование

### Модуль `processing`

```python
from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01'},
]

# Фильтрация по статусу
filtered = filter_by_state(data, 'EXECUTED')

# Сортировка по дате
sorted_data = sort_by_date(data)
```

## Технологии

- Python 3.9+
- Poetry
- Git
- Flake8, black, isort, mypy


## Тестирование

Для запуска тестов и проверки покрытия выполните:

```bash
poetry run pytest --cov=src --cov-report=html```
python
## Генераторы (модуль `generators`)

### Фильтрация транзакций по валюте

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
Получение описаний транзакций

python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
Генерация номеров банковских карт

from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
## Декоратор логирования (модуль `decorators`)

Декоратор `log` автоматически логирует вызовы функций:

- В консоль: `@log()`
- В файл: `@log(filename="mylog.txt")`

Пример:

```python
from src.decorators import log

@log(filename="log.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)


## Работа с JSON и внешним API

### Модуль `src/utils.py`

Функция `read_json_file(file_path: str) -> List[Dict[str, Any]]` читает JSON-файл с транзакциями и возвращает список словарей. Если файл не найден, пустой или содержит не список — возвращает пустой список.

Пример использования:

```python
from src.utils import read_json_file

transactions = read_json_file("data/operations.json")
print(len(transactions))
Модуль src/external_api.py

Функция convert_currency(transaction: Dict[str, Any]) -> float конвертирует сумму транзакции в рубли, если валюта USD или EUR. Для конвертации используется внешнее API (Exchange Rates Data API).

Пример использования:

python
from src.external_api import convert_currency

transaction = {
    "operationAmount": {
        "amount": "100",
        "currency": {"code": "USD"}
    }
}
rub_amount = convert_currency(transaction)
print(rub_amount)
Переменные окружения

Для работы с API необходимо получить ключ на apilayer.com и сохранить его в файл .env:

text
API_KEY=ваш_ключ
Шаблон файла .env с указанием необходимых переменных находится в .env.example.

Тестирование

bash
poetry run pytest --cov=src --cov-report=html
Отчёт о покрытии сохраняется в папке htmlcov/.