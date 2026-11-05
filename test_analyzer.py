from analyzer import count_characters, count_vowels, count_words, reverse_text


def test_count_words():
    assert count_words("Hello, world!") == 2


def test_count_characters():
    assert count_characters("hello world") == 11


def test_count_vowels():
    assert count_vowels("Hello, World!") == 3


def test_reverse_text():
    assert reverse_text("hello") == "olleh"
