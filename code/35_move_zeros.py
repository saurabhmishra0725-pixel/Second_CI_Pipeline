def move_zeros(numbers):
    """Return a new list with zeros last, preserving nonzero order."""
    return [number for number in numbers if number != 0] + [0] * numbers.count(0)
