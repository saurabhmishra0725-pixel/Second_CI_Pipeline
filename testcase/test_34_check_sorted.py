import importlib

import pytest

module = importlib.import_module("34_check_sorted")


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], True),
    ([1, 1, 2], True),
    ([-3, -1, 0], True),
    ([1, 3, 2], False),
    ([3, 2, 1], False),
    ([], True),
    ([5], True),
])
def test_is_sorted(numbers, expected):
    assert module.is_sorted(numbers) is expected
