import turtle
from math import *


class Geom:

    def __init__(self, my_step=40, shift_Ox=0,
                 shift_Oy=0):
        self.step = my_step
        self.shift_Ox = shift_Ox * my_step
        self.shift_Oy = shift_Oy * my_step

    def grid(self, cells_num=20,
             arrow_size=1.5,
             ):
        turtle.shape('classic')
        turtle.turtlesize(arrow_size)
        n = cells_num//2
        maxx = n * self.step
        maxy = maxx
        turtle.tracer(0)

        turtle.width(1)
        turtle.color('#d0d0d0')
        # vertical axes
        for i in range(0, 2 * n + 1):
            turtle.up()
            x = i * self.step
            turtle.goto(-maxx + x, -maxy)
            turtle.down()
            turtle.goto(-maxx + x, maxy)

        # horizontal axes
        for i in range(0, 2 * n + 1):
            turtle.up()
            y = i * self.step
            turtle.goto(-maxx, -maxy + y)
            turtle.down()
            turtle.goto(maxx, -maxy + y)

        # axis y
        turtle.color('black')
        turtle.up()
        turtle.width(2)
        turtle.setheading(90)
        turtle.goto(0 + self.shift_Oy, -maxy)
        turtle.down()
        turtle.goto(0 + self.shift_Oy, maxy)
        turtle.stamp()

        # axis x
        turtle.color('black')
        turtle.up()
        turtle.width(2)
        turtle.goto(-maxx, 0 + self.shift_Ox)
        turtle.down()
        turtle.goto(maxx, 0 + self.shift_Ox)
        turtle.setheading(0)
        turtle.stamp()

        turtle.update()

    def mpoint(self, x, y, xlabel_d=None, ylabel_d=None,
               point_name=None, dot_size=10, launched=None):
        turtle.ht()
        turtle.up()
        turtle.color('black')

        turtle.goto(x * self.step + self.shift_Oy,
                    y * self.step + self.shift_Ox)
        turtle.dot(dot_size)
        if xlabel_d is not None:
            if ylabel_d is not None:
                if point_name is not None:
                    turtle.goto(turtle.xcor() + xlabel_d,
                                turtle.ycor() + ylabel_d)
                    turtle.write(point_name, font=('Arial', 24, 'normal'))

    def mlabel(self, x, y, name):
        turtle.ht()
        turtle.up()
        turtle.color('black')
        turtle.goto(x * self.step + self.shift_Oy,
                    y * self.step + self.shift_Ox)
        turtle.write(name, font=('Arial', 24, 'normal'))

    def mturtle(self, x, y, shape=None, size=None):
        turtle.ht()
        turtle.up()
        turtle.color('black')

        turtle.goto(x * self.step + self.shift_Oy,
                    y * self.step + self.shift_Ox)
        turtle.turtlesize(1)
        if shape is None:
            turtle.shape('turtle')
        else:
            turtle.shape(shape)
        turtle.stamp()

    def mline(self, x1, y1, x2, y2, xlabel_d=None, ylabel_d=None, label=None,
              vector=False, lwidth=2, color=None):
        turtle.ht()
        turtle.width(lwidth)
        turtle.turtlesize(1.5)
        turtle.color('black') if color is None else turtle.color(color)
        turtle.shape('classic')
        turtle.tracer(0)
        turtle.up()
        turtle.goto(x1 * self.step + self.shift_Oy,
                    y1 * self.step + self.shift_Ox)
        turtle.down()
        turtle.goto(x2 * self.step + self.shift_Oy,
                    y2 * self.step + self.shift_Ox)
        if vector:
            turtle.setheading(atan2((y2 - y1), (x2 - x1)) / pi * 180)
            turtle.stamp()
        if xlabel_d is not None:
            if ylabel_d is not None:
                if label is not None:
                    turtle.up()
                    turtle.goto(
                        (x1 + x2) / 2 * self.step + xlabel_d + self.shift_Oy,
                        (y1 + y2) / 2 * self.step + ylabel_d + self.shift_Ox)
                    turtle.write(label, font=('Arial', 24, 'normal'))
        turtle.update()
