import subprocess
import pytest

def test_multiply_numbers_in_int(capsys):
    # Тест для числа 0
    result = subprocess.run(["python3", "2_prac/1.py"], capture_output=True, text=True)
    captured_output = result.stdout  # Получаем вывод программы
    expected_output = "Произведение цифр числа 0 = 0\n"
    assert captured_output == expected_output  # Проверяем вывод

def test_average_of_three_random_numbers(capsys):
    result = subprocess.run(["python3", "2_prac/2.py"], capture_output=True, text=True)
    captured_output = result.stdout  # Получаем вывод программы
    # Проверим, что в выводе есть "Среднее значение для трех случайных чисел"
    assert "Среднее значение для трех случайных чисел" in captured_output

def test_integer_division_and_modulus(capsys):
    result = subprocess.run(["python3", "2_prac/3.py"], capture_output=True, text=True)
    captured_output = result.stdout  # Получаем вывод программы
    # Проверим, что вывод начинается с "x ="
    assert "x = " in captured_output


def test_rounding(capsys):
    result = subprocess.run(["python3", "2_prac/4.py"], capture_output=True, text=True)
    captured_output = result.stdout
    # Проверяем, что вывод содержит все три ожидаемых формата
    assert "1. 14.72" in captured_output
    assert "2. 15" in captured_output
    assert "3. 000000014.721" in captured_output


def test_reverse_number(capsys):
    result = subprocess.run(["python3", "2_prac/5.py"], capture_output=True, text=True)
    captured_output = result.stdout  # Получаем вывод программы
    assert captured_output.strip() == "-523"  # Число -325 должно стать -523 после разворота

def test_reverse_and_overflow(capsys):
    result = subprocess.run(["python3", "2_prac/6.py"], capture_output=True, text=True)
    captured_output = result.stdout  # Получаем вывод программы
    assert captured_output.strip() == "0"

