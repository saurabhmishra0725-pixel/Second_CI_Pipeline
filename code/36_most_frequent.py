from collections import Counter


def most_frequent(items):
    """Return the most frequent item; ties use first appearance, empty uses None."""
    return Counter(items).most_common(1)[0][0] if items else None
