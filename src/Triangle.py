from src.Figure import Figure
"""
Класс для инициализации треугольника по трем сторонам
подсчета его площади и периметра 
"""

class Triangle(Figure):
    def __init__(self,A:int,B:int,C:int):
        '''Инициализация треугольника по трем сторонам'''
        super().__init__(type='Triangle')
        if not (isinstance(A,int) or isinstance(A,float)) or not (isinstance(B,int) or isinstance(B,float)) \
            or not (isinstance(C,int) or isinstance(C,float)):
            raise ValueError
        elif (A+B<C) or (A+C<B) or (B+C<A) or (A<0 and B<0 and C<0):
              raise ValueError
        elif (A or B or C) <= 0:
              raise ValueError
        self.a = A
        self.b = B
        self.c = C

    @property
    def area(self):
        '''Подсчет площади треугольника. Принимает три стороны a,b и с. возвращает значение площади
        ((p*(p-a)*(p-b)*(p-c))**0.5)
        p = (a+b+c)/2'''
        p = (self.a + self.b + self.c) / 2
        area = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return round(area,2)

    @property
    def perimeter(self):
        '''Подсчет периметра треугольника. Принимает три стороны a,b и с. возвращает значение периметра (a+b+с)'''
        return round((self.a + self.b + self.c),2)