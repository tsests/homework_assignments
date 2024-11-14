import pytest
from io import StringIO
import sys
import os
from unittest.mock import patch

# Добавляем путь до папки 3_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../3_prac')))

# Импортируем функции
from prac1 import fizz_buzz
#from prac2 import estimate_value
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
        ('7', '7'),
        ('0', 'Fizz Buzz'),
        ('45', 'Fizz Buzz')
    ]
)
def test_fizz_buzz(input_value, expected_output):
    # Мокаем input и print
    with patch('builtins.input', return_value=input_value), patch('builtins.print') as mock_print:
        fizz_buzz(abs(int(input_value)))  # Вызываем функцию с преобразованием
        mock_print.assert_called_with(expected_output)
