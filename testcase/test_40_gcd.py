import importlib

import pytest

module = importlib.import_module("40_gcd")


@pytest.mark.parametrize("a, b, expected", [
    (48, 18, 6),
    (17, 13, 1),
    (12, 12, 12),
    (-48, 18, 6),
    (48, -18, 6),
    (-48, -18, 6),
    (0, 5, 5),
    (5, 0, 5),
    (0, 0, 0),
])
def test_gcd(a, b, expected):
    assert module.gcd(a, b) == expected
