import subprocess
import pytest

# 1. Тест для 1.py (Приветствие)
def test_1_prac_greeting(capsys):
    result = subprocess.run(["python3", "1_prac/1.py"], capture_output=True, text=True)  # Захватываем вывод
    captured_output = result.stdout  # Получаем вывод программы
    expected_output = "Hello Ivan Petrov! You just delved into Python. Great start!\n"
    assert captured_output == expected_output  # Проверяем вывод

# 2. Тест для 2.py (Заголовок)
def test_2_prac_title(capsys):
    result = subprocess.run(["python3", "1_prac/2.py"], capture_output=True, text=True)  # Захватываем вывод
    captured_output = result.stdout  # Получаем вывод программы
    expected_output = "Hello World\n"
    assert captured_output == expected_output  # Проверяем вывод

# 3. Тест для 3.py (Форматированная сумма)
def test_3_prac_currency(capsys):
    result = subprocess.run(["python3", "1_prac/3.py"], capture_output=True, text=True)  # Захватываем вывод
    captured_output = result.stdout  # Получаем вывод программы
    expected_output = "100,500.16\n"
    assert captured_output == expected_output  # Проверяем вывод
