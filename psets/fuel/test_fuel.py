from fuel import convert, gauge
import pytest

# ----- Tests for convert() -----
def test_convert_normal_fraction():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25

def test_convert_zero():
    assert convert("0/4") == 0

def test_convert_full():
    assert convert("4/4") == 100

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat")

def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("1.5/4")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert_improper_fraction():
    # Should raise ValueError if x > y
    with pytest.raises(ValueError):
        convert("5/4")

# ----- Tests for gauge() -----
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
