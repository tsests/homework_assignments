import pytest
from io import StringIO
import sys
import os
from unittest.mock import patch

# Добавляем путь до папки 5_prac
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../5_prac')))

# Импортируем функции
from n_1 import analyze_text

@pytest.mark.parametrize(
    "text, expected_chars, expected_words",
    [
        ("hello, word of word", {'h': 1, 'e': 1, 'l': 2, 'o': 4, 'w': 2, 'r': 2, 'd': 2, 'f': 1}, {'hello': 1, 'word': 2, 'of': 1}),
        ("test test test", {'t': 6, 'e': 3, 's': 3}, {'test': 3}),
        ("Python! Python?", {'p': 2, 'y': 2, 't': 2, 'h': 2, 'o': 2, 'n': 2}, {'python': 2}),
        ("", {}, {}),
        ("123 123 456", {'1': 2, '2': 2, '3': 2, '4': 1, '5': 1, '6': 1}, {'123': 2, '456': 1}),
        ("A B C A", {'a': 2, 'b': 1, 'c': 1}, {'a': 2, 'b': 1, 'c': 1}),
    ],
)
def test_analyze_text(text, expected_chars, expected_words):
    assert analyze_text(text) == (expected_chars, expected_words)

