import importlib

import pytest

module = importlib.import_module("37_rotate_string")


@pytest.mark.parametrize("text, k, expected", [
    ("abcdef", 2, "cdefab"),
    ("abcdef", 0, "abcdef"),
    ("abcdef", 6, "abcdef"),
    ("abcdef", 8, "cdefab"),
    ("abcdef", -2, "efabcd"),
    ("", 3, ""),
    ("a", 9, "a"),
])
def test_rotate_string(text, k, expected):
    assert module.rotate_string(text, k) == expected
