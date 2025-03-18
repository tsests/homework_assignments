import pytest
from io import StringIO
import sys
import os
from unittest.mock import patch

# Добавляем путь до папки 5_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../5_prac')))

# Импортируем функции
from n_1 import analyze_text
from n_2 import int_to_roman
from n_3 import find_min_rate_bank
from n_4 import invert_dict
from n_5 import create_currency_dict
from n_6 import define_winner

@pytest.mark.parametrize(
    "text, expected_chars, expected_words",
    [
        ("hello word of word", {'h': 1, 'e': 1, 'l': 2, 'o': 4, 'w': 2, 'r': 2, 'd': 2, 'f': 1}, {'hello': 1, 'word': 2, 'of': 1}),
        ("test test test", {'t': 6, 'e': 3, 's': 3}, {'test': 3}),
        ("python python", {'p': 2, 'y': 2, 't': 2, 'h': 2, 'o': 2, 'n': 2}, {'python': 2}),
        ("", {}, {}),
        ("123 123 456", {'1': 2, '2': 2, '3': 2, '4': 1, '5': 1, '6': 1}, {'123': 2, '456': 1}),
        ("a b c a", {'a': 2, 'b': 1, 'c': 1}, {'a': 2, 'b': 1, 'c': 1}),
    ],
)
def test_analyze_text(text, expected_chars, expected_words):
    assert analyze_text(text) == (expected_chars, expected_words)

@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "I"),
        (4, "IV"),
        (6, "VI"),
        (9, "IX"),
        (13, "XIII"),
        (44, "XLIV"),
        (76, "LXXVI"),
        (90, "XC"),
        (3999, "MMMCMXCIX"),
        (1000, "M"),
        (500, "D"),
        (400, "CD"),
        (50, "L"),
        (10, "X"),
    ],
)
def test_int_to_roman(num, expected):
    assert int_to_roman(num) == expected


@pytest.mark.parametrize(
    "rates_dict, expected",
    [
        ({'Sberbank': 55.8, 'VTB24': 53.91, 'MyBank': 53.91, 'Name': 98.99}, {'VTB24': 53.91, 'MyBank': 53.91}),
        ({'BankA': 100, 'BankB': 200, 'BankC': 100}, {'BankA': 100, 'BankC': 100}),
        ({'Alpha': 10.5}, {'Alpha': 10.5}),  # Один банк
        ({}, set()),  # Пустой словарь
        ({'OnlyBank': 99.99}, {'OnlyBank': 99.99}),  # Один элемент
    ],
)
def test_find_min_rate_bank(rates_dict, expected):
    assert find_min_rate_bank(rates_dict) == expected

@pytest.mark.parametrize(
    "original_dict, expected",
    [
        ({'Petr': '546810', 'Katya': '241815'}, {'546810': 'Petr', '241815': 'Katya'}),
        ({'Alice': '12345', 'Bob': '67890'}, {'12345': 'Alice', '67890': 'Bob'}),
        ({'X': '1'}, {'1': 'X'}),  # Один элемент
        ({}, {}),  # Пустой словарь
        ({'A': 'X', 'B': 'Y', 'C': 'Z'}, {'X': 'A', 'Y': 'B', 'Z': 'C'}),  # Несколько элементов
    ],
)
def test_invert_dict(original_dict, expected):
    assert invert_dict(original_dict) == expected

@pytest.mark.parametrize(
    "dates, rates, expected",
    [
        (
            ['2017-03-01', '2017-03-02', '2017-03-03', '2017-03-04', '2017-03-05'], 
            [55.7, 55.2, 23.1, 54.5, 1.1], 
            {'2017-03-01': 55.7, '2017-03-02': 55.2, '2017-03-03': 23.1, '2017-03-04': 54.5, '2017-03-05': 1.1}
        ),
        ([], [], {}),  # Пустые списки
        (['2024-01-01'], [100.0], {'2024-01-01': 100.0}),  # Один элемент
        (['2023-12-31', '2024-01-01'], [99.9, 101.1], {'2023-12-31': 99.9, '2024-01-01': 101.1}),  # Два элемента
    ],
)
def test_create_currency_dict(dates, rates, expected):
    assert create_currency_dict(dates, rates) == expected

@pytest.mark.parametrize(
    "data, expected",
    [
        (["OOX", "XOO", "OXX"], "D"),  # Ничья
        (["XXX", "O.O", "O.."], "X"),  # Победа X по горизонтали
        (["O.O", "XXX", "O.."], "X"),  # Победа X по горизонтали
        (["O.O", "O..", "XXX"], "X"),  # Победа X по горизонтали
        (["XOO", "X..", "X.."], "X"),  # Победа X по вертикали
        (["OXO", "O.X", "O.X"], "O"),  # Победа O по вертикали
        (["X..", ".X.", "..X"], "X"),  # Победа X по диагонали
        (["..O", ".O.", "O.."], "O"),  # Победа O по диагонали
        (["...", "...", "..."], "D"),  # Пустое поле (ничья)
    ],
)
def test_define_winner(data, expected):
    assert define_winner(data) == expected


