import pytest
import examples

def test_area_calculation():
    assert examples.rectangle_area(10,2) == 20

def test_stopwords():
    sentence = "the quick brown fox jumped over the lazy dog"
    stopwords = ['the', 'an', 'a', 'of', 'to']
    assert examples.strip_stopwords(sentence, stopwords) == 'quick brown fox jumped over lazy dog'


# def test_area_type_handling():
#     with pytest.raises(TypeError):
#         examples.rectangle_area(5,'testing')
