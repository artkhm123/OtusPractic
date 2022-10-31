class Figure:
    """
    Базовый класс для геометрических фигур.
    С подсчетом суммы площадей двух фигур
    """
    def __init__(self,type='Figure'):
        self.type = type

    def add_area(self,obj):
        '''функция считает сумму площадей исходного экземпляра с другим экземпляром. получает на вход экземпляр
        геометрической фигуры и складывает его площадь с площадью текущего экземпляра'''
        if not (isinstance(obj, Figure)):
            raise ValueError
        return round((self.area + obj.area),2)