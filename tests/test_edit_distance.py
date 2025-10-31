from algo import edit_distance


def test_edit_distance_example():
    word1 = "kitten"
    word2 = "sitting"
    assert edit_distance(word1, word2) == 3

def test_edit_distance_insert_at_start():
    word1 = "abc"
    word2 = "dabc"
    assert edit_distance(word1, word2) == 1
