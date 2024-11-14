import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Добавляем путь до папки 3_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../3_prac')))

# Импортируем функции
from prac1 import fizz_buzz
from prac2 import estimate_value
from prac3 import generate_sequence
from prac4 import get_secret_message
from prac5 import is_contain_three_words_in_a_row
from prac6 import jokes

class TestFizzBuzz(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_fizz(self, mock_stdout):
        fizz_buzz(3)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz")

    @patch('sys.stdout', new_callable=StringIO)
    def test_buzz(self, mock_stdout):
        fizz_buzz(5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Buzz")

    @patch('sys.stdout', new_callable=StringIO)
    def test_fizz_buzz(self, mock_stdout):
        fizz_buzz(15)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz Buzz")

    @patch('sys.stdout', new_callable=StringIO)
    def test_number(self, mock_stdout):
        fizz_buzz(7)
        self.assertEqual(mock_stdout.getvalue().strip(), "7")

    @patch('sys.stdout', new_callable=StringIO)
    def test_negative(self, mock_stdout):
        fizz_buzz(-3)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz")
        fizz_buzz(-5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Buzz")
        fizz_buzz(-15)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz Buzz")
        fizz_buzz(-7)
        self.assertEqual(mock_stdout.getvalue().strip(), "-7")

class TestEstimateValue(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_odd(self, mock_stdout, mock_input):
        estimate_value(3)
        self.assertEqual(mock_stdout.getvalue().strip(), "Плохо")

    @patch('builtins.input', return_value='4')
    @patch('sys.stdout', new_callable=StringIO)
    def test_not_bad(self, mock_stdout, mock_input):
        estimate_value(4)
        self.assertEqual(mock_stdout.getvalue().strip(), "Неплохо")

    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=StringIO)
    def test_so_so(self, mock_stdout, mock_input):
        estimate_value(10)
        self.assertEqual(mock_stdout.getvalue().strip(), "Так себе")

    @patch('builtins.input', return_value='22')
    @patch('sys.stdout', new_callable=StringIO)
    def test_excellent(self, mock_stdout, mock_input):
        estimate_value(22)
        self.assertEqual(mock_stdout.getvalue().strip(), "Отлично")

class TestGenerateSequence(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_minimal_value(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as output:
            generate_sequence()
            self.assertEqual(output.getvalue().strip(), "1")

    @patch("builtins.input", side_effect=["5"])
    def test_normal_value(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as output:
            generate_sequence()
            self.assertEqual(output.getvalue().strip(), "12345")

    @patch("builtins.input", side_effect=["0", "-1", "3"])
    def test_incorrect_initial_values(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as output:
            generate_sequence()
            self.assertEqual(output.getvalue().strip(), "123")

    @patch("builtins.input", side_effect=["100"])
    def test_large_value(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as output:
            generate_sequence()
            expected_output = "".join(str(i) for i in range(1, 101))
            self.assertEqual(output.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["text", "5"])
    def test_non_integer_input(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as output:
            with self.assertRaises(ValueError):
                generate_sequence()


class TestSecretMessage(unittest.TestCase):
    def test_secret_message(self):
        expected_message = "IAMSOTIREDPLEASESAVEME"
        self.assertEqual(get_secret_message(), expected_message)


class TestThreeWords(unittest.TestCase):
    def test_three_words_true(self):
        self.assertTrue(is_contain_three_words_in_a_row("Hello World hello"))

    def test_contains_number(self):
        self.assertFalse(is_contain_three_words_in_a_row("He is 123 man"))

    def test_only_numbers(self):
        self.assertFalse(is_contain_three_words_in_a_row("1 2 3 4"))

    def test_mixed_words_and_numbers(self):
        self.assertTrue(is_contain_three_words_in_a_row("start 5 one two three 7 end"))


class TestJokes(unittest.TestCase):
    def test_replace_right_with_left(self):
        self.assertEqual(jokes(["left", "right", "left", "stop"]), "left,left,left,stop")
        self.assertEqual(jokes(["bright aright", "ok"]), "bleft aleft,ok")
        self.assertEqual(jokes(["enough", "jokes"]), "enough,jokes")


if __name__ == '__main__':
    unittest.main()
