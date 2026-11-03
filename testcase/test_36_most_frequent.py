import importlib

import pytest

module = importlib.import_module("36_most_frequent")


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 2, 3, 2], 2),
    ([4, 2, 4, 2], 4),
    ([3, 2, 1], 3),
    ([-1, -1, 0], -1),
    (["apple", "pear", "apple"], "apple"),
    ([7], 7),
    ([], None),
])
def test_most_frequent(items, expected):
    assert module.most_frequent(items) == expected
