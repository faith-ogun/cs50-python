from bank import value

def test_upper_lower_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_mixed_case_hello():
    assert value("HelLo") == 0

def test_beginning_h_not_hello():
    assert value("hi") == 20
    assert value("Howdy") == 20

def test_sentence_beginning_h():
    assert value("Hi, Newman") == 20
    assert value("Hello, Newman") == 0

def test_numbers_and_symbols():
    assert value("CS50!") == 100
    assert value("H3ll0, W0rld!") == 20

def test_empty_string():
    assert value("") == 100

def test_spaces():
    assert value("hello world") == 0
    assert value("h e l l o") == 20
