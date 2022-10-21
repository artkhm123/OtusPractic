import math
from src.Figure import Figure
"""
Класс для инициализации круга по по длинне радиуса,
подсчета его площади и периметра 
"""

class Circle(Figure):
    def __init__(self, R: int):
        super().__init__(type='Circle')
        if not (isinstance(R, int) or isinstance(R,float)):
            raise ValueError
        elif R <= 0:
              raise ValueError
        self.r = R


    @property
    def perimeter(self):
        return round((2 * math.pi * self.r),2)

    @property
    def area(self):
        return round((math.pi * self.r ** 2),2)