

from src.utils import read_json_file


def test_read_json_file_success(tmp_path):
    """Тест успешного чтения JSON-файла."""
    test_file = tmp_path / "test.json"
    test_file.write_text('[{"id": 1, "amount": 100}]', encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == [{"id": 1, "amount": 100}]


def test_read_json_file_not_found():
    """Тест отсутствующего файла."""
    data = read_json_file("not_found.json")
    assert data == []


def test_read_json_file_invalid_json(tmp_path):
    """Тест некорректного JSON."""
    test_file = tmp_path / "invalid.json"
    test_file.write_text("not a json", encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == []


def test_read_json_file_not_list(tmp_path):
    """Тест, когда JSON — не список."""
    test_file = tmp_path / "not_list.json"
    test_file.write_text('{"key": "value"}', encoding="utf-8")
    data = read_json_file(str(test_file))
    assert data == []
