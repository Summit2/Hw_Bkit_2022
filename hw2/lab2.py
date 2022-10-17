
from lab_python_oop.Figure import shape
from lab_python_oop.Circle import circle_figure
from lab_python_oop.Rectangle import rectangle_figure
from lab_python_oop.Square import square_figure
from lab_python_oop.Figure import shape


def main():
    

    rect=rectangle_figure("бежевого",4,5)
    print(rect)
    sq=square_figure("синего",3)
    print(sq)
    circ=circle_figure("красного",12)
    print(circ)
    



if __name__ == "__main__":
    main()