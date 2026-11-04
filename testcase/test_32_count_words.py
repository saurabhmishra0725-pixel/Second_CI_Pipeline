import importlib

import pytest

module = importlib.import_module("32_count_words")


@pytest.mark.parametrize("sentence, expected", [
    ("Python is easy to learn", 5),
    ("  hello   world  ", 2),
    ("one\ttwo\nthree", 3),
    ("Hello, world!", 2),
    ("", 0),
    (" \t\n ", 0),
])
def test_count_words(sentence, expected):
    assert module.count_words(sentence) == expected
