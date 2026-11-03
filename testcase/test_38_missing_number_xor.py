import importlib

import pytest

module = importlib.import_module("38_missing_number_xor")


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 4, 5], 3),
    ([2, 3, 4], 1),
    ([1, 2, 3], 4),
    ([5, 1, 4, 2], 3),
    ([1], 2),
    ([2], 1),
    ([], 1),
])
def test_missing_number_xor(numbers, expected):
    assert module.missing_number_xor(numbers) == expected
