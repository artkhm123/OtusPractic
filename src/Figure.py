class Figure:
    """
    Базовый класс для геометрических фигур.
    С подсчетом суммы площадей двух фигур
    """
    def __init__(self,type='Figure'):
        self.type = type

    def add_area(self,obj):
        if not (isinstance(obj, Figure)):
            raise ValueError
        return round((self.area + obj.area),2)