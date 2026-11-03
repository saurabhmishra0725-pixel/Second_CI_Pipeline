import importlib

import pytest

module = importlib.import_module("33_first_non_repeating")


@pytest.mark.parametrize("text, expected", [
    ("swiss", "w"),
    ("aabbcdd", "c"),
    ("aabb", None),
    ("", None),
    ("Aa", "A"),
    ("a a", " "),
])
def test_first_non_repeating(text, expected):
    assert module.first_non_repeating(text) == expected
