from math import pi

from lab_python_oop.Color import shape_color
from  lab_python_oop.Figure import shape


class circle_figure(shape_color,shape):
    Figure_type='Круг'
    def __init__(self,cl,radius):
        self.__radius=radius
        self.fc=shape_color(cl)
    def Square(self):
        return (self.__radius**2)*pi
    def __repr__(self):
        return ("{} {} цвета радиуса {}, площадью {}".format(self.Figure_type,self.fc.get_color(),self.__radius,self.Square()))

