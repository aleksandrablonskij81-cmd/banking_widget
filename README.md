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