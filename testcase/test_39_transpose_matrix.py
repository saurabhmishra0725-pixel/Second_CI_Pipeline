import importlib

import pytest

module = importlib.import_module("39_transpose_matrix")


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1, 2, 3]], [[1], [2], [3]]),
    ([[1], [2], [3]], [[1, 2, 3]]),
    ([], []),
    ([[], []], []),
])
def test_transpose_matrix(matrix, expected):
    original = [row.copy() for row in matrix]
    assert module.transpose_matrix(matrix) == expected
    assert matrix == original


def test_transpose_rejects_unequal_row_lengths():
    with pytest.raises(ValueError, match="same length"):
        module.transpose_matrix([[1, 2], [3]])
