def count_words(text):
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def count_characters(text):
    """Return the number of characters in text, including whitespace."""
    return len(text)


def count_vowels(text):
    """Return the number of English vowels in text."""
    return sum(character.lower() in "aeiou" for character in text)


def reverse_text(text):
    """Return text with its characters in reverse order."""
    return text[::-1]
