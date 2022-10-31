from src.Rectangle import Rectangle
"""
Класс для инициализации квадрата по длинне стороны,
"""

class Square(Rectangle):
    def __init__(self,A:int):
        '''Инициализация квадрата по стороне'''
        super().__init__(A,A)
        if not (isinstance(A, int) or isinstance(A,float)):
            raise ValueError
        elif (A <= 0):
              raise ValueError