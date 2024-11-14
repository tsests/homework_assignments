import unittest
from io import StringIO
import sys

# Импорт функций из разных файлов
from fizz_buzz import fizz_buzz
from estimate_value import estimate_value
from sequence import generate_sequence
from secret_message import get_secret_message
from three_words import is_contain_three_words_in_a_row
from lefties import jokes


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fizz_buzz(9)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Fizz")

    def test_buzz(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fizz_buzz(10)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Buzz")

    def test_fizz_buzz(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fizz_buzz(15)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Fizz Buzz")

    def test_number(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fizz_buzz(7)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "7")


class TestEstimateValue(unittest.TestCase):
    def test_poor(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        estimate_value(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Плохо")

    def test_not_bad(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        estimate_value(4)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Неплохо")

    def test_so_so(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        estimate_value(10)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Так себе")

    def test_excellent(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        estimate_value(22)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Отлично")


class TestGenerateSequence(unittest.TestCase):
    def test_sequence(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_sequence(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "12345")


class TestSecretMessage(unittest.TestCase):
    def test_secret_message(self):
        expected_message = "IAMMYSTERYSECRETMESSAGEWAITINGTOBEUNLOCKED"
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
