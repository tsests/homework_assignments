import pytest
from io import StringIO
import sys
import os
from unittest.mock import patch

# Добавляем путь до папки 3_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../3_prac')))

# Импортируем функции
from prac1 import fizz_buzz
from prac2 import estimate_value
#from prac3 import generate_sequence
#from prac4 import get_secret_message
#from prac5 import is_contain_three_words_in_a_row
#from prac6 import jokes

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ('3', 'Fizz'),
        ('5', 'Buzz'),
        ('15', 'Fizz Buzz'),
        ('7', 7),
        ('0', 'Fizz Buzz'),
        ('45', 'Fizz Buzz')
    ]
)
def test_fizz_buzz(input_value, expected_output):
    # Мокаем input и print
    with patch('builtins.input', return_value=input_value), patch('builtins.print') as mock_print:
        fizz_buzz(abs(int(input_value)))  # Вызываем функцию с преобразованием
        mock_print.assert_called_with(expected_output)

# Тесты для функции estimate_value
@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ('1', 'Плохо'),          # Нечетное число
        ('2', 'Неплохо'),        # Число от 2 до 5
        ('5', 'Плохо'),        # Нечетное
        ('6', 'Так себе'),       # Число от 6 до 20
        ('10', 'Так себе'),      # Число от 6 до 20
        ('20', 'Так себе'),      # Число от 6 до 20
        ('21', 'Плохо'),
        ('22', 'Отлично'),
        ('100', 'Отлично'),      # Число больше 20
        ('4', 'Неплохо'),        # 0 — четное и в диапазоне от 2 до 5
    ]
)
def test_estimate_value(input_value, expected_output):
    with patch('builtins.input', return_value=input_value), patch('builtins.print') as mock_print:
        estimate_value(int(input_value))  # вызываем функцию
        mock_print.assert_called_with(expected_output)




