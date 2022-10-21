import pytest
from src.Square import Square


@pytest.mark.parametrize("value",[1.0,10.999])
def test_square_creation_float_values(value):
    square = Square(value)

@pytest.mark.parametrize("value",[1,10])
def test_square_creation_int_values(value):
    square = Square(value)

@pytest.mark.parametrize("value", ['string value'])
def test_square_creation_string_values(value):
    with pytest.raises(ValueError):
        square = Square(value)

@pytest.mark.parametrize("value", [-1,-0.5,-500])
def test_square_creation_negative_values(value):
    with pytest.raises(ValueError):
        square = Square(value)

def test_square_creation_0_value():
    with pytest.raises(ValueError):
        square = Square(0)

@pytest.mark.parametrize("value,expected", [(2.5,10), (5,20)])
def test_square_perimeter_check_float_and_int_values(value, expected):
    square = Square(value)
    assert square.perimeter==expected

@pytest.mark.parametrize("value,expected", [(2.5,6.25), (5,25)])
def test_square_area_check_float_and_int_values(value, expected):
    square = Square(value)
    assert square.area==expected