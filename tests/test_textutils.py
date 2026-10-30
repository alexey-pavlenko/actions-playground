from textutils import is_palindrome, word_count


def test_word_count():
    assert word_count("hello big world") == 3


def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("github actions")
