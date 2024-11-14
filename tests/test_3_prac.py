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


def test_fizz_buzz_fizz():
    with patch('builtins.input', return_value='3'):  # Мокаем input
        with patch('builtins.print') as mock_print:  # Мокаем print
            fizz_buzz(abs(int(input())))
            mock_print.assert_called_with('Fizz')

def test_fizz_buzz_buzz():
    with patch('builtins.input', return_value='5'):
        with patch('builtins.print') as mock_print:
            fizz_buzz(abs(int(input())))
            mock_print.assert_called_with('Buzz')

def test_fizz_buzz_fizzbuzz():
    with patch('builtins.input', return_value='15'):
        with patch('builtins.print') as mock_print:
            fizz_buzz(abs(int(input())))
            mock_print.assert_called_with('Fizz Buzz')

def test_fizz_buzz_number():
    with patch('builtins.input', return_value='7'):
        with patch('builtins.print') as mock_print:
            fizz_buzz(abs(int(input())))
            mock_print.assert_called_with(7)
