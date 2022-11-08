from src.hw_figures.Circle import Circle
from src.hw_figures.Rectangle import Rectangle
from src.hw_figures.Square import Square
from src.hw_figures.Triangle import Triangle

def test_add_area_test():
    '''проверка функции сложения площадей двух экземпляров'''
    square = Square(5)
    triangle = Triangle(3,4,5)
    rectangle = Rectangle(3,5)
    cirle = Circle(5)
    assert square.add_area(triangle) == 31
    assert square.add_area(rectangle) == 40
    assert square.add_area(cirle) == 103.54