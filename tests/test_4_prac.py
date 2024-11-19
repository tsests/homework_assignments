import pytest
from io import StringIO
import sys
import os
from unittest.mock import patch

# Добавляем путь до папки 4_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../4_prac')))

# Импортируем функции
from n_1 import multiply_last_with_even
from n_2 import calculate_difference_max_min
from n_3 import sort_abs_elements
from n_4 import calculate_list_median
from n_5 import count_number_of_striped_words

# Параметризованный тест
@pytest.mark.parametrize(
    "elements, expected_result",
    [
        ([], 0),  # Пустой список
        ([5], 25),  # Один элемент: 5 * 5
        ([2, 3], 6),  # Два элемента: 2 * 3
        ([0, 1, 2, 3, 4, 5], 30),  # Пример из задания
        ([1, 3, 5], 30),  # Пример из задания
        ([2, 4, 6, 8], 64),  # Только четные
        ([10**6, 1, 10**6, 2, 10**6, 3], 9000000),  # Большие числа
        ([-2, -3, -4, -5, -6], 72),  # Отрицательные числа
        ([-1, -1, -1, -1], 2),  # Отрицательные числа, короткий список
        ([-1, 2, 3, -4, 5], 35),  # Смешанные знаки
        ([0, 0, 0, 0, 0], 0),  # Только нули
        ([0, 1, 2, 3, 4], 24),  # Нули с другими числами
    ],
)

def test_multiply_last_with_even(elements, expected_result):
    assert multiply_last_with_even(elements) == expected_result

# Параметризованный тест для второго задания
@pytest.mark.parametrize(
    "elements, expected_result",
    [
        ([], 0),  # Пустой список
        ([1], 0),  # Один элемент
        ([1, 2, 3], 2),  # Простой случай: 3 - 1
        ([5, -5], 10),  # Отрицательные числа
        ([10.2, -2.2, 0, 1.1, 0.5], 12.4),  # Пример из задания с float
        ([-1.5, -3.5, -2.5], 2.0),  # Отрицательные float
        ([0, 0, 0], 0),  # Только нули
        ([1.0001, 1.0002], 0.0),  # Пограничный случай с float
        ([10**6, -10**6], 2 * 10**6),  # Большие числа
        ([1e-9, -1e-9], 0.0),  # Очень маленькие числа
        ([1, 2.5, 3.7, -0.1], 3.8),  # Смешанные типы int и float
    ],
)
def test_calculate_difference_max_min(elements, expected_result):
    assert pytest.approx(calculate_difference_max_min(elements), 0.001) == expected_result

# Тест для третьего задания
@pytest.mark.parametrize(
    "elements, expected_result",
    [
        ((), ()),  # Пустой кортеж
        ((0,), [0]),  # Один элемент
        ((-20, -5, 10, 15), [-5, 10, 15, -20]),  # Пример из задания
        ((1, 2, 3, 0), [0, 1, 2, 3]),  # Пример из задания
        ((-1, -2, -3, 0), [0, -1, -2, -3]),  # Пример из задания
        ((10, -10, 5, -5, 0), [0, 5, -5, 10, -10]),  # Смешанные значения
        ((-2.5, 1.5, -1.5, 2.5), [1.5, -1.5, -2.5, 2.5]),  # Float
        ((100, -100, 50, -50, 0), [0, 50, -50, 100, -100]),  # Положительные и отрицательные
        ((1e6, -1e6, 2e-6, -1e-6), [-1e-6, 2e-6, 1e6, -1e6]),  # Маленькие и большие числа
        ((1, 1, 1, 1, 1), [1, 1, 1, 1, 1]),
    ],
)
def test_sort_abs_elements(elements, expected_result):
    assert sort_abs_elements(elements) == expected_result

@pytest.mark.parametrize(
    "elements, expected_result",
    [
        ([1, 2, 3, 4, 5], 3),  # Нечётное количество элементов, упорядоченный массив
        ([3, 1, 2, 5, 3], 3),  # Нечётное количество, неупорядоченный массив
        ([1, 300, 2, 200, 1], 2),  # Нечётное количество, разный диапазон
        ([3, 6, 20, 99, 10, 15], 12.5),  # Чётное количество элементов
        ((1, 2, 3, 4, 5), 3),  # Входные данные — кортеж
        ((3, 6, 20, 99, 10, 15), 12.5),  # Кортеж с чётным количеством
        ([10], 10),  # Единственный элемент
        ((1, 1, 1, 1), 1),  # Все элементы одинаковы
        ([1, 2], 1.5),  # Минимально возможное чётное количество
        ([1, 2, 2, 1], 1.5),  # Чётное количество с повторяющимися числами
        ([1, 2, 3, 4, 1000], 3),  # Смешанный диапазон значений
        ([0, 0, 0, 0], 0),  # Только нули
    ],
)
def test_calculate_list_median(elements, expected_result):
    assert calculate_list_median(elements) == expected_result

@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("My name is ...", 3),  # Пример из задания
        ("Hello world", 0),  # Пример из задания
        ("A quantity of striped words.", 1),  # Пример из задания
        ("Dog,cat,mouse,bird.Human.", 3),  # Пример из задания
        ("", 0),  # Пустая строка
        ("a", 0),  # Однобуквенное слово
        ("ab", 1),  # Два символа: полосатое
        ("abc", 0),  # Три символа: не полосатое
        ("Aa Bb Cc", 0),  # Каждое слово не полосатое
        ("eXample tEset", 1),  # Смешанный регистр, одно полосатое
        ("123 456", 0),  # Только числа
        ("Word1 Word2", 0),  # Смешанные слова
        ("VowelA ConsonantC", 1),  # Одно полосатое
        ("ABABAB ABABABA", 2),  # Чередующиеся длинные слова
        ("M1M Nn! Uo, Yi.", 0),  # Пунктуация и цифры
    ],
)
def test_count_number_of_striped_words(text, expected_result):
    assert count_number_of_striped_words(text) == expected_result




































