from ispalindrome import isPalindrome


def test_isPalindrome():
    assert isPalindrome('') is True
    assert isPalindrome('abcdedcba') is True
    assert isPalindrome('python') is False
