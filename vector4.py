from turtle import *
from my_grid import *
step=80
w = Geom(my_step=step, shift_Ox=-3, shift_Oy=-2)
w.grid(cells_num=10)  # cells_num should be even

turtle.tracer(1)
i = 0


def add_item():
    global i

    if i == 0:
        w.mpoint(1, 0, 0, -30, 'А')
    elif i == 1:
        w.mpoint(5, 4, 10, -10, 'B')
        w.mline(1, 0, 5, 4, -5, 30, 'AB', vector=True, lwidth=3)
    elif i == 2:
        w.mpoint(1, 4, 15, 0, 'C')
        w.mline(1, 0, 1, 4, 15, 0, 'AC', vector=True, lwidth=3)
    elif i == 3:
        w.mpoint(3, 2, 15, -20, 'D')
        w.mline(1, 0, 3, 2, 25, -15, 'AD', vector=True, lwidth=3, color='green')
    elif i == 4:
        w.mpoint(3, -1, 15, -20, 'E')
        w.mpoint(7, 3, 15, -20, 'F')
        w.mline(3, -1, 7, 3, 25, -15, 'EF', vector=True, lwidth=3)
    elif i == 5:
        w.mpoint(-3, 4, 15, -10, 'G')
        w.mline(1, 0, -3, 4, 5, 10, 'AG', vector=True, lwidth=3)
    elif i == 6:
        w.mpoint(6, 7, 15, -10, 'H')
        w.mpoint(4, 5, 25, -10, 'I')
        w.mline(6, 7, 4, 5, 5, 30, 'HI', vector=True, lwidth=3)
    elif i == 7:
        w.mlabel(1, 7, 'AB=EF')
    elif i == 8:
        w.mlabel(1, 6.5, 'AB↑↑AD')
    elif i == 9:
        w.mlabel(1, 6, 'AB↑↓HI   AD↑↓HI')
    elif i == 10:
        w.mlabel(1, 5.5, '|AD|=|HI|  |AB|=|AG|')


    i += 1


turtle.onkeypress(add_item)
turtle.listen()

turtle.done()
