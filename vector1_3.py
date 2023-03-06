from turtle import *
from my_grid import *

ht()
w = Geom(my_step=100, shift_Ox=-3, shift_Oy=-2)
w.grid(cells_num=8) # cells_num should be even

turtle.tracer(1)
turtle.down()
i = 0


def add_item():
    global i

    if i == 0:
        w.mturtle(5, 4, shape='turtle')
    elif i == 1:
        w.mpoint(1, 1)
    elif i == 2:
        w.mpoint(1, 1, 25, -20, 'А (ми)')
    elif i == 3:
        w.mpoint(5, 4, 20, 5, 'В (черепашка)')
    elif i == 4:
        w.mline(1, 1, 5, 4, 0, -25, 'шлях до черепашки', vector=True, lwidth=3, color='red')
    elif i == 5:
        w.mline(1, 1, 1, 4)
    elif i == 6:
        w.mline(1, 4, 5, 4)
    elif i == 7:
        w.mlabel(2, 5, 'АB(4;3)')
    elif i == 8:
        w.mlabel(4, 5, '|АB|=5 (клітинок)')
    i += 1


turtle.onkeypress(add_item)
turtle.listen()

turtle.done()
