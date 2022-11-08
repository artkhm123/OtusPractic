from src.hw_figures.Figure import Figure
"""
Класс для инициализации прямоугольника по двум сторонам,
подсчета его площади и периметра 
"""

class Rectangle(Figure):
    '''Инициализация прямоугольника по двум сторонам'''
    def __init__(self, A:int, B:int):
        if not (isinstance(A,int) or isinstance(A,float)) or not (isinstance(B,int) or isinstance(B,float)):
            raise ValueError
        elif A <= 0:
              raise ValueError
        elif B <= 0:
              raise ValueError
        if (B==A):
            super().__init__('Sqare')
        else:
            super().__init__('Rectangle')
        self.a = A
        self.b = B

    @property
    def perimeter(self):
        '''Подсчет периметра прямоугольника. Принимает две стороны a и b. возвращает значение периметра (a+b)*2'''
        return round(((self.a +self.b) * 2),2)

    @property
    def area(self):
        '''Подсчет площади прямоугольника. Принимает две стороны a и b. возвращает значение площади (a*b)'''
        return round((self.a * self.b),2)


