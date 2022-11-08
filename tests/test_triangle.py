import pytest
from src.hw_figures.Triangle import Triangle

def test_triangle_area_int_values():
    '''проверка вычисления площади треугольника по int значениям сторон'''
    triangle=Triangle(13,14,15)
    assert triangle.area == 84

def test_triangle_area_float_values():
    '''проверка вычисления площади треугольника по float значениям сторон'''
    triangle = Triangle(0.13, 0.14, 0.15)
    assert triangle.area == 0.01

def test_triangle_perimeter_int_values():
    '''проверка вычисления периметра треугольника по int значениям сторон'''
    triangle1=Triangle(13,14,15)
    assert triangle1.perimeter == (13+14+15)

def test_triangle_perimeter_float_values():
    '''проверка вычисления периметра треугольника по float значениям сторон'''
    triangle1 = Triangle(0.13, 0.14, 0.15)
    assert triangle1.perimeter == round((0.13 + 0.14 + 0.15),2)

def test_triangle_creation_int_values():
    '''проверка создания экземпляра треугольника с int значением сторон.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(13,14,15)
def test_triangle_creation_float_values():
    '''проверка создания экземпляра треугольника с float значением сторон.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(0.13, 0.14, 0.15)
def test_triangle_creation_str_values():
    '''проверка создания экземпляра треугольника с str значением сторон.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(13,'str',15)

def test_triangle_creation_math_existance_negativ_AplusC_is_less_thanB():
    '''проверка создания экземпляра треугольника с значением сторон A+C<B.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(13,140,15)

def test_triangle_creation_math_existance_negativ_BplusC_is_less_thanA():
    '''проверка создания экземпляра треугольника с значением сторон B+C<A.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(130,14,15)

def test_triangle_creation_math_existance_negativ_AplusB_is_less_thanC():
    '''проверка создания экземпляра треугольника с значением сторон A+C<B.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Triangle(13,14,150)
