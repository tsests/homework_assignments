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
from prac3 import main
from prac4 import secret_message
from prac5 import is_contain_three_words_in_a_row
from prac6 import jokes

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

@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        # Ввод 0, программа должна запросить повторно и ввести 3
        (['0', '3'], '123'),  # Ввод: сначала 0, потом 3, вывод: 1 2 3
        
        # Ввод 1, сразу выводим 1
        (['1'], '1'),  # Ввод: 1, вывод: 1
        
        # Ввод 5, выводим числа от 1 до 5
        (['5'], '12345'),  # Ввод: 5, вывод: 1 2 3 4 5
        
        # Ввод отрицательного числа, например -3, и потом 3
        (['-3', '3'], '123'),  # Ввод: -3, потом 3, вывод: 1 2 3
    ]
)
def test_generate_sequence(input_values, expected_output):
    # Мокаем input
    with patch('builtins.input', side_effect=input_values), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Запускаем программу
        main()

        # Проверяем вывод
        output = mock_stdout.getvalue().strip()  # Убираем лишние пробелы
        assert output == expected_output

def test_secret_message():
    expected_output = "IAMSOTIREDPLEASESAVEME"
    
    # Мокаем стандартный вывод
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        secret_message()  # Запускаем программу

        # Получаем вывод
        output = mock_stdout.getvalue().strip()  # Убираем лишние пробелы

        # Проверяем, что вывод совпадает с ожидаемым результатом
        assert output == expected_output

def test_is_contain_three_words_in_a_row():
    # Тесты для разных вариантов входных данных
    
    # Простой случай, где есть 3 слова подряд
    assert is_contain_three_words_in_a_row("Hello World hello") == True
    
    # Есть 2 слова подряд, затем число, то результат False
    assert is_contain_three_words_in_a_row("He is 123 man") == False
    
    # Весь текст состоит из чисел, три последовательных слова отсутствуют
    assert is_contain_three_words_in_a_row("1 2 3 4") == False
    
    # Смешанный случай с числами, но есть три слова подряд
    assert is_contain_three_words_in_a_row("start 5 one two three 7 end") == True
    
    # Пустая строка, нет слов вообще
    assert is_contain_three_words_in_a_row("") == False
    
    # Только одно слово
    assert is_contain_three_words_in_a_row("Hello") == False
    
    # Три слова подряд, но с числами, которые сбивают счетчик
    assert is_contain_three_words_in_a_row("start 5 one two 3 three") == False
    
    # Строка, содержащая три последовательных слова без чисел в середине
    assert is_contain_three_words_in_a_row("this is a test") == True

    # Тест на строку, где слова разделены несколькими пробелами
    assert is_contain_three_words_in_a_row("this   is    a test") == True

    assert is_contain_three_words_in_a_row("beginning of sentence test 123") == True

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (["left", "right", "left", "stop"], "left,left,left,stop"),  # Проверка замены "right" на "left"
        (["bright aright", "ok"], "bleft arleft,ok"),  # Проверка частичных слов с "right"
        (["enough", "jokes"], "enough,jokes"),  # Проверка отсутствия "right" в данных
        (["right", "right", "right"], "left,left,left"),  # Проверка только с "right"
        ([], ""),  # Проверка на пустой список
        (["right now", "we're right here", "turn right"], "left now,we're left here,turn left"),  # Проверка нескольких вхождений "right" в строках
        (["   right    ", "  is right here   "], "   left    ,  is left here   "),  # Проверка строк с пробелами и форматированием
        (["brighter", "sight", "right side"], "blefter,sight,left side"),  # Смешанные случаи: "right" внутри слов и отдельные слова
        (["123right", "right!"], "123left,left!"),  # Проверка строк с числами и символами

    ]
)
def test_jokes(input_value, expected_output):
    result = jokes(input_value)
    assert result == expected_output  # Проверяем, что результат функции совпадает с ожидаемым







