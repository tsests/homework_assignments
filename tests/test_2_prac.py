import subprocess
import pytest

def test_multiply_numbers_in_int(capsys):
    # Тест для числа 0
    subprocess.run(["python3", "2_prac/1.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    expected_output = "Произведение цифр числа 0 = 0\n"
    assert captured_output == expected_output

    # Тест для числа, например 123
    subprocess.run(["python3", "2_prac/1.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    expected_output = "Произведение цифр числа 123 = 6\n"  # 1 * 2 * 3 = 6
    assert captured_output == expected_output

    # Тест для числа, например 505
    subprocess.run(["python3", "2_prac/1.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    expected_output = "Произведение цифр числа 505 = 25\n"  # 5 * 5 = 25 (0 игнорируется)
    assert captured_output == expected_output

def test_average_of_three_random_numbers(capsys):
    subprocess.run(["python3", "2_prac/2.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    
    # Проверим, что в выводе есть "Среднее значение для трех случайных чисел"
    assert "Среднее значение для трех случайных чисел" in captured_output

    # Проверим, что вывод выглядит как вещественное число с точностью до 2 знаков
    parts = captured_output.split(" = ")
    average_value = float(parts[1].strip())
    assert isinstance(average_value, float)  # Убедимся, что это вещественное число

def test_integer_division_and_modulus(capsys):
    subprocess.run(["python3", "2_prac/3.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out

    # Проверим, что вывод начинается с "x ="
    assert "x = " in captured_output
    assert ", " in captured_output  # Разделение между целочисленным делением и остатком
    
    # Разделим вывод и проверим целочисленное деление и остаток
    parts = captured_output.split(", ")
    division_result = int(parts[0].split("=")[1].strip())  # Получаем результат деления
    modulus_result = int(parts[1].strip())  # Получаем остаток

    # Примерный тест для случайных чисел
    assert isinstance(division_result, int)
    assert isinstance(modulus_result, int)

def test_rounding(capsys):
    subprocess.run(["python3", "2_prac/4.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    
    # Проверяем, что вывод содержит все три ожидаемых формата
    assert "1. 14.72" in captured_output
    assert "2. 15" in captured_output
    assert "3. 000000014.721" in captured_output


def test_reverse_number(capsys):
    subprocess.run(["python3", "2_prac/5.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    assert captured_output.strip() == "-523"  # Число -325 должно стать -523 после разворота

def test_reverse_and_overflow(capsys):
    subprocess.run(["python3", "2_prac/6.py"], capture_output=True, text=True)
    captured_output = capsys.readouterr().out
    assert captured_output.strip() == "-2147483647" 
