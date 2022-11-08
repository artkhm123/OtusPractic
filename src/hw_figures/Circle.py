import math
from src.hw_figures.Figure import Figure
"""
Класс для инициализации круга по по длинне радиуса,
подсчета его площади и периметра 
"""

class Circle(Figure):
    def __init__(self, R: int):
        '''Инициализация круга по радиусу'''
        super().__init__(type='Circle')
        if not (isinstance(R, int) or isinstance(R,float)):
            raise ValueError
        elif R <= 0:
              raise ValueError
        self.r = R

    @property
    def perimeter(self):
        '''Подсчет периметра круга. Принимает радиус и возвращает значение периметра 2*pi*r'''
        return round((2 * math.pi * self.r),2)

    @property
    def area(self):
        '''Подсчет площади круга. Принимает радиус и возвращает значение площади pi*r*r'''
        return round((math.pi * self.r ** 2),2)