from capitalizeFirst import capitalizeFirst


def test_capitalizeFirst():
    assert capitalizeFirst(['cat', 'meao', 'dog', 'bark']) == ['Cat', 'Meao', 'Dog', 'Bark']
