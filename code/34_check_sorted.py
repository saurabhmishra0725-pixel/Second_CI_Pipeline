def is_sorted(numbers):
    """Return whether numbers are in ascending order, allowing equal values."""
    return all(left <= right for left, right in zip(numbers, numbers[1:]))
