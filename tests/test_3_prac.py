import pytest
from io import StringIO
import sys

# Добавляем путь до папки 3_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../3_prac')))

# Импортируем функции
from prac1 import fizz_buzz
from prac2 import estimate_value
from prac3 import generate_sequence
from prac4 import get_secret_message
from prac5 import is_contain_three_words_in_a_row
from prac6 import jokes

def test_fizz(capsys):
    # Проверяем, что выводится "Fizz" для чисел, кратных 3, но не 5
    fizz_buzz(3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz"
    
    fizz_buzz(6)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz"

    fizz_buzz(9)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz"

def test_buzz(capsys):
    # Проверяем, что выводится "Buzz" для чисел, кратных 5, но не 3
    fizz_buzz(5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Buzz"

    fizz_buzz(10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Buzz"

    fizz_buzz(20)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Buzz"

def test_fizz_buzz(capsys):
    # Проверяем, что выводится "Fizz Buzz" для чисел, кратных 3 и 5
    fizz_buzz(15)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz Buzz"

    fizz_buzz(30)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz Buzz"

    fizz_buzz(45)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz Buzz"

def test_other_numbers(capsys):
    # Проверяем, что выводится число как строка для чисел, не кратных 3 и 5
    fizz_buzz(1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1"
    
    fizz_buzz(2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "2"

    fizz_buzz(7)
    captured = capsys.readouterr()
    assert captured.out.strip() == "7"

    fizz_buzz(8)
    captured = capsys.readouterr()
    assert captured.out.strip() == "8"
