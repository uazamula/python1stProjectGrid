from my_grid import *

# Задача з підручника Геометрія 9 клас Єршова с.147 (2022 р.)

step = 80
w = Geom(my_step=step, shift_Ox=-2, shift_Oy=-2)
w.grid(cells_num=10)  # cells_num should be even

turtle.tracer(1)
i = 0


def add_item():
    global i

    if i == 0:
        w.mpoint(-2, 1, 15, -10, 'А')
    elif i == 1:
        w.mpoint(0, 4, 15, -10, 'B')
    elif i == 2:
        w.mpoint(4, 1, 15, 0, 'C')
    elif i == 3:
        w.mline(-2, 1, 0, 4)
    elif i == 4:
        w.mline(0, 4, 4, 1)
    elif i == 5:
        w.mline(-2, 1, 0, 4, 25, -15, 'AB', vector=True, lwidth=4)
    elif i == 6:
        w.mlabel(1, 6, 'AB(2;3)  DC=AB')
    elif i == 7:
        w.mlabel(1, 5, 'DC(2;3)  C(4;1)  D(4-2=2; 1-3=-2)')
    elif i == 8:
        w.mlabel(1, 4, 'D(2;-2)')
    elif i == 9:
        w.mpoint(2, -2, 25, 0, 'D')
    elif i == 10:
        w.mline(2, -2, 4, 1, 20, -10, 'DC', vector=True, lwidth=4)
        w.mline(-2, 1, 2, -2)

    i += 1


turtle.onkeypress(add_item)
turtle.listen()

turtle.done()
