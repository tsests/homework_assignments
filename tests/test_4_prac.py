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




































