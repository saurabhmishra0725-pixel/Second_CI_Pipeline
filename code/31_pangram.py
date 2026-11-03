def is_pangram(text):
    """Return whether text contains all 26 English letters, ignoring case."""
    return set("abcdefghijklmnopqrstuvwxyz").issubset(text.lower())
