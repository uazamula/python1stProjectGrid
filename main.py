from movie import Movies
from shape import *

# mov1 = Movies('And so it begins', '', 'English', 'Robert Kingman', 2019)
# print(mov1)
# mov1.genre = 'Fantasy'
# mov1.genre = 'Romance'
# print(mov1)
# mov1.recommendMovie()
#
# print(Square(5))

from turtle import *
from my_grid import *
from math import *

ht()
step = 40
w = Geom()
w.grid(cells_num=10, shift_Oy=0, shift_Ox=0)

# point A

turtle.tracer(1)
turtle.down()
i = 0


def add_item():
    global i

    if i == 0:
        w.mpoint(5, 4)
    elif i == 1:
        w.mpoint(1, -2, 15, 0, 'O')
    elif i == 2:
        w.mline(5, 4, -3, -8, 0, -25, 'my_line', vector=True, lwidth=3)
    elif i == 3:
        w.mpoint(-3, -8, -15, 5, 'A\'')
    elif i == 4:
        w.mturtle(3, 7, )
    i += 1


turtle.onkeypress(add_item)
turtle.listen()

turtle.done()
