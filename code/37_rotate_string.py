def rotate_string(text, k):
    """Rotate left by k positions; negative k rotates right."""
    if not text:
        return text
    k %= len(text)
    return text[k:] + text[:k]
