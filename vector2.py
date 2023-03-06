from turtle import *
from my_grid import *

ht()
w = Geom(my_step=80, shift_Ox=-3, shift_Oy=-2)
w.grid(cells_num=10)  # cells_num should be even

turtle.tracer(1)
turtle.down()
i = 0


def add_item():
    global i

    if i == 0:
        w.mlabel(2, 6, 'АB(2;5)')
    elif i == 1:
        w.mpoint(0, 0)
    elif i == 2:
        w.mline(0, 0, 2, 5, 0, -25, 'AB', vector=True, lwidth=3)
    elif i == 3:
        w.mpoint(3, 2)
    elif i == 4:
        w.mline(3, 2, 5, 7, 0, -25, 'AB', vector=True, lwidth=3)
    elif i == 5:
        w.mpoint(3, -1)
    elif i == 6:
        w.mline(3, -1, 5, 4, 0, -25, 'AB', vector=True, lwidth=3, color='black')

    i += 1


turtle.onkeypress(add_item)
turtle.listen()

turtle.done()
