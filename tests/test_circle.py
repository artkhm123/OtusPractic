import pytest
from src.hw_figures.Circle import Circle

@pytest.mark.parametrize("value",[1.0,10.999])
def test_circle_creation_float_values(value):
    '''проверка создания экземпляра круга с float значением радиуса. должен создаться'''
    Circle(value)

@pytest.mark.parametrize("value",[1,10])
def test_circle_creation_int_values(value):
    '''проверка создания экземпляра круга с int значением радиуса. должен создаться'''
    Circle(value)

@pytest.mark.parametrize("value", ['string value'])
def test_circle_creation_string_values(value):
    '''проверка создания экземпляра круга с str значением радиуса. должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Circle(value)

@pytest.mark.parametrize("value", [-1,-0.5,-500])
def test_circle_creation_negative_values(value):
    '''проверка создания экземпляра круга с отрицательный значением радиуса. должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Circle(value)

def test_circle_creation_0_value():
    '''проверка создания экземпляра круга с нулевым значением радиуса. должно выкинуть исключение ValueError'''
    with pytest.raises(ValueError):
        Circle(0)

@pytest.mark.parametrize("value,expected", [(2.5,15.71), (5,31.42)])
def test_circle_perimeter_check_float_and_int_values(value, expected):
    '''проверка вычисления периметра круга по int и float значениям радиуса'''
    circle = Circle(value)
    assert circle.perimeter==expected

@pytest.mark.parametrize("value,expected", [(2.5,19.63), (5,78.54)])
def test_circle_area_check_float_and_int_values(value, expected):
    '''проверка вычисления площади круга по int и float значениям радиуса'''
    circle = Circle(value)
    assert circle.area==expected




