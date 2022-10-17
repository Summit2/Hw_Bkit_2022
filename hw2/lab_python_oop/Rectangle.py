from  lab_python_oop.Figure import shape
from  lab_python_oop.Color import shape_color



class rectangle_figure(shape_color,shape):
    
    Figure_type='Прямоугольник'
    def __init__(self,cl,length,width):
        '''Конструктор класса Прямоугольник
        Принимает 3 параметра: цвет, длина и ширина'''
        self.length=length
        self.width=width
        self.fc=shape_color(cl)

    def Square(self):
        return self.length*self.width
    def __repr__(self):
        return ('{} {} цвета со сторонами {} и {}, и площадью {}'.format(self.Figure_type,self.fc.get_color(),self.length,self.width,self.Square()))

