import subprocess
import pytest

# 1. Тест для 1.py (Приветствие)
def test_1_prac_greeting(capsys):
    # Запуск скрипта и проверка вывода
    subprocess.run(["python3", "1_prac/1.py"])
    captured = capsys.readouterr()
    expected_output = "Hello Ivan Petrov! You just delved into Python. Great start!\n"
    assert captured.out == expected_output

# 2. Тест для 2.py (Заголовок)
def test_2_prac_title(capsys):
    # Запуск скрипта и проверка вывода
    subprocess.run(["python3", "1_prac/2.py"])
    captured = capsys.readouterr()
    expected_output = "Hello World\n"
    assert captured.out == expected_output

# 3. Тест для 3.py (Форматированная сумма)
def test_3_prac_currency(capsys):
    # Запуск скрипта и проверка вывода
    subprocess.run(["python3", "1_prac/3.py"])
    captured = capsys.readouterr()
    expected_output = "100,500.16\n"
    assert captured.out == expected_output
