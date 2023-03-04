import turtle
from math import *


class Geom:

    def __init__(self, my_step=40):
        self.step = my_step

    def grid(self, max_val=10,
             arrow_size=1.5,
             shift_Oy=0,
             shift_Ox=0):
        turtle.turtlesize(arrow_size)
        n = max_val
        step_pixel = self.step
        maxx = max_val * step_pixel
        maxy = maxx
        shift_Oy = step_pixel * shift_Oy
        shift_Ox = step_pixel * shift_Ox
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
        turtle.goto(0 + shift_Oy, -maxy)
        turtle.down()
        turtle.goto(0 + shift_Oy, maxy)
        turtle.stamp()

        # axis x
        turtle.color('black')
        turtle.up()
        turtle.width(2)
        turtle.goto(-maxx, 0 + shift_Ox)
        turtle.down()
        turtle.goto(maxx, 0 + shift_Ox)
        turtle.setheading(0)
        turtle.stamp()

        turtle.update()

    def add_point(self, x, y, xlabel_delta=None, ylabel_delta=None,
                  point_name=None, dot_size=10):
        turtle.up()
        turtle.goto(x * self.step, y * self.step)
        turtle.dot(dot_size)
        if xlabel_delta is not None:
            if ylabel_delta is not None:
                if point_name is not None:
                    turtle.goto(turtle.xcor() + xlabel_delta, turtle.ycor() + ylabel_delta)
                    turtle.write(point_name, font=('Arial', 24, 'normal'))

    def add_line(self, x1, y1, x2, y2, vector=False):
        turtle.tracer(0)
        turtle.up()
        turtle.goto(x1 * self.step, y1 * self.step)
        turtle.down()
        turtle.goto(x2 * self.step, y2 * self.step)
        if vector:
            turtle.setheading(atan2((y2 - y1), (x2 - x1)) / pi * 180)
            turtle.stamp()
        turtle.update()
