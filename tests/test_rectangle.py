import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize("value1,value2",[(1.2,3.9999), (0.07,100.99)])
def test_rectangle_creation_float_values(value1,value2):
    '''проверка создания экземпляра прямоугольника с float значением сторон. должен создаться'''
    Rectangle(value1,value2)

@pytest.mark.parametrize("value1,value2",[(1,3), (50,1000)])
def test_rectangle_creation_int_values(value1,value2):
    '''проверка создания экземпляра прямоугольника с int значением сторон. должен создаться'''
    Rectangle(value1,value2)

@pytest.mark.parametrize("value1,value2", [(-1,'str'), ('str2',-100)])
def test_rectangle_creation_string_values(value1,value2):
    '''проверка создания экземпляра прямоугольника с str значением одной из сторон.
    должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Rectangle(value1,value2)

@pytest.mark.parametrize("value1,value2", [(-1,3.5), (5,-100)])
def test_rectangle_creation_negative_values(value1,value2):
    '''проверка создания экземпляра прямоугольника с отрицательными значением одной из сторон.
    должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Rectangle(value1,value2)

@pytest.mark.parametrize("value1,value2", [(0,3.5),(5,0)])
def test_rectangle_creation_a0b0_value(value1,value2):
    '''проверка создания экземпляра прямоугольника с нулевым значением одной из сторон.
        должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Rectangle(value1,value2)

@pytest.mark.parametrize("value1,value2,expected", [(2.5, 3.5, 12), (5,10,30)])
def test_rectangle_perimeter_check_float_and_int_values(value1,value2, expected):
    '''проверка вычисления периметра прямоугольника по int и float значениям сторон'''
    rectangle = Rectangle(value1,value2)
    assert rectangle.perimeter==expected

@pytest.mark.parametrize("value1, value2, expected", [(2.5,3.5,8.75), (5,6,30)])
def test_rectangle_area_check_float_and_int_values(value1,value2, expected):
    '''проверка вычисления площади прямоугольника по int и float значениям сторон'''
    rectangle = Rectangle(value1,value2)
    assert rectangle.area==expected