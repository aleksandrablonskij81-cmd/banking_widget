import pytest
from unittest.mock import patch, MagicMock
from src.file_operation import read_transactions_from_csv, read_transactions_from_excel


class TestReadTransactionsFromCSV:
    """Тесты для чтения CSV файлов"""

    @patch('pandas.read_csv')
    def test_read_csv_success(self, mock_read_csv):
        """Тест: успешное чтение CSV файла"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [
            {'id': 1, 'amount': 100, 'date': '2024-01-01'},
            {'id': 2, 'amount': 200, 'date': '2024-01-02'}
        ]
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv('fake.csv')

        assert len(result) == 2
        assert result[0]['amount'] == 100
        assert result[1]['amount'] == 200
        mock_read_csv.assert_called_once_with('fake.csv')

    @patch('pandas.read_csv')
    def test_read_csv_file_not_found(self, mock_read_csv):
        """Тест: CSV файл не найден"""
        mock_read_csv.side_effect = FileNotFoundError()

        with pytest.raises(FileNotFoundError):
            read_transactions_from_csv('not_exist.csv')

    @patch('pandas.read_csv')
    def test_read_csv_empty_file(self, mock_read_csv):
        """Тест: пустой CSV файл"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = []
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv('empty.csv')

        assert result == []


class TestReadTransactionsFromExcel:
    """Тесты для чтения Excel файлов"""

    @patch('pandas.read_excel')
    def test_read_excel_success(self, mock_read_excel):
        """Тест: успешное чтение Excel файла"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [
            {'id': 1, 'amount': 1000, 'category': 'food'},
            {'id': 2, 'amount': 500, 'category': 'transport'}
        ]
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel('fake.xlsx')

        assert len(result) == 2
        assert result[0]['amount'] == 1000
        assert result[1]['category'] == 'transport'
        mock_read_excel.assert_called_once_with('fake.xlsx', engine='openpyxl')

    @patch('pandas.read_excel')
    def test_read_excel_file_not_found(self, mock_read_excel):
        """Тест: Excel файл не найден"""
        mock_read_excel.side_effect = FileNotFoundError()

        with pytest.raises(FileNotFoundError):
            read_transactions_from_excel('not_exist.xlsx')

    @patch('pandas.read_excel')
    def test_read_excel_empty_file(self, mock_read_excel):
        """Тест: пустой Excel файл"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = []
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel('empty.xlsx')

        assert result == []
