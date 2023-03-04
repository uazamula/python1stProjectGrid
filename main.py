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
screen = Screen()
ht()
step = 40
w = Geom()
w.grid(max_val=10, shift_Oy=0, shift_Ox=0)

# point A

tracer(1)
down()
i = 0


def add_item():
    global i

    if i == 0:
        w.add_point(5, 4)
    elif i == 1:
        w.add_point(1, -2, 15, 0, 'O')
    elif i == 2:
        w.add_line(5, 4, -3, -8, vector=True)
    elif i == 3:
        w.add_point(-3, -8, -15, 5, 'A\'')
    i += 1


onkeypress(add_item)
listen()

done()