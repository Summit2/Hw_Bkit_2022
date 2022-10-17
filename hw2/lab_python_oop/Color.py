

class shape_color:
    def __init__(self,color) -> None:
        '''Конструктор Класса "Цвет"
           На вход подается переменная color,которая принимает цвет
        '''
        
        self.__color=color
    def get_color(self):
        return self.__color