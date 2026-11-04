import importlib

import pytest

module = importlib.import_module("35_move_zeros")


@pytest.mark.parametrize("numbers, expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, -2, 0, 4, -1], [-2, 4, -1, 0, 0]),
    ([0, 0], [0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
])
def test_move_zeros(numbers, expected):
    original = numbers.copy()
    assert module.move_zeros(numbers) == expected
    assert numbers == original
