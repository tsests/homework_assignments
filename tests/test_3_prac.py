import sys
import os
import unittest
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
    @patch('builtins.input', return_value='9')
    @patch('sys.stdout', new_callable=StringIO)
    def test_fizz(self, mock_stdout, mock_input):
        fizz_buzz(9)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz")

    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=StringIO)
    def test_buzz(self, mock_stdout, mock_input):
        fizz_buzz(10)
        self.assertEqual(mock_stdout.getvalue().strip(), "Buzz")

    @patch('builtins.input', return_value='15')
    @patch('sys.stdout', new_callable=StringIO)
    def test_fizz_buzz(self, mock_stdout, mock_input):
        fizz_buzz(15)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fizz Buzz")

    @patch('builtins.input', return_value='7')
    @patch('sys.stdout', new_callable=StringIO)
    def test_number(self, mock_stdout, mock_input):
        fizz_buzz(7)
        self.assertEqual(mock_stdout.getvalue().strip(), "7")

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
    def test_sequence(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_sequence(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "12345")


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
