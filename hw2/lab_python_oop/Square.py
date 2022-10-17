from lab_python_oop.Rectangle import rectangle_figure


class square_figure(rectangle_figure):

    Figure_type='Квадрат'

    def __init__(self,cl,length):
        self.length=length
        super().__init__(cl,self.length,self.length)


    def __repr__(self):
        return ("{} {} цвета со стороной {}, площадью {}"
        .format(self.Figure_type, self.fc.get_color(), self.length,self.Square()))

