from twttr import shorten

def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("RHYTHM") == "RHYTHM"

def test_mixed_case():
    assert shorten("Twitter") == "Twttr"
    assert shorten("ApPlE") == "pPl"

def test_numbers_and_symbols():
    assert shorten("CS50!") == "CS50!"
    assert shorten("H3ll0, W0rld!") == "H3ll0, W0rld!"

def test_empty_string():
    assert shorten("") == ""

def test_spaces():
    assert shorten("hello world") == "hll wrld"
    assert shorten("A E I O U") == "    "

def test_preserve_case():
    assert shorten("Hello") == "Hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello") == "hll"

def test_full_sentence():
    assert shorten("This is CS50, and it is fun!") == "Ths s CS50, nd t s fn!"
