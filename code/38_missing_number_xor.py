def missing_number_xor(numbers):
    """Find the missing value in 1..n, given n-1 distinct values from that range."""
    missing = len(numbers) + 1
    for expected, actual in enumerate(numbers, start=1):
        missing ^= expected ^ actual
    return missing
