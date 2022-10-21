import pytest
from src.Triangle import Triangle


def test_triangle_area_int_values():
    triangle=Triangle(13,14,15)
    assert triangle.area == 84

def test_triangle_area__float_values():
    triangle = Triangle(0.13, 0.14, 0.15)
    assert triangle.area == 0.01

def test_triangle_perimeter_int_values():
    triangle1=Triangle(13,14,15)
    assert triangle1.perimeter == (13+14+15)

def test_triangle_perimeter_float_values():
    triangle1 = Triangle(0.13, 0.14, 0.15)
    assert triangle1.perimeter == round((0.13 + 0.14 + 0.15),2)

def test_triangle_creation_str_values():
    with pytest.raises(ValueError):
        triangle=Triangle(13,'str',15)

def test_triangle_creation_math_existance_negativ_AplusC_is_less_thanB():
    with pytest.raises(ValueError):
        triangle=Triangle(13,140,15)

def test_triangle_creation_math_existance_negativ_BplusC_is_less_thanA():
    with pytest.raises(ValueError):
        triangle=Triangle(130,14,15)
