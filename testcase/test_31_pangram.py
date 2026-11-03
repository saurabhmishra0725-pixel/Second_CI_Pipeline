import importlib

import pytest

module = importlib.import_module("31_pangram")


@pytest.mark.parametrize("text, expected", [
    ("The quick brown fox jumps over the lazy dog", True),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ! 123", True),
    ("Hello World", False),
    ("abcdefghijklmnopqrstuvwxy", False),
    ("", False),
])
def test_is_pangram(text, expected):
    assert module.is_pangram(text) is expected
