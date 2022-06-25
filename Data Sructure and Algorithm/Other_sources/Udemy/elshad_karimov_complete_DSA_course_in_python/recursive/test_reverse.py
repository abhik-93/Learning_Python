from reverse import reverse


def test_reverse():
    assert reverse('Python') == 'nohtyP'
    assert reverse('abcba') == 'abcba'
