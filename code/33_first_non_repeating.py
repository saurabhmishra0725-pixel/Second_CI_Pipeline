from collections import Counter


def first_non_repeating(text):
    """Return the first unique character, or None if none exists."""
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)
