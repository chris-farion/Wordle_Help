from Wordle import *

def test_empty_list():
    assert is_list_sorted([]) == True


def test_singelton_list():
    assert is_list_sorted(['order']) == True

def test_unordered_list():
    assert is_list_sorted(['order','above']) == False

def test_ordered_list():
    assert is_list_sorted(['above','order']) == True

def test_split_list():
    list = ['above','order']
    first,second = split_list(list)
    assert first == ['above']
    assert second == ['order']



































