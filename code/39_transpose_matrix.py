def transpose_matrix(matrix):
    """Return the transpose of a rectangular matrix as a list of rows."""
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Matrix rows must have the same length")
    return [list(column) for column in zip(*matrix)]
