from turtle import *
from math import *


class Geom:

    def __init__(self, my_step=40):
        self.step = my_step

    def grid(self, max_val=10,
             arrow_size=1.5,
             shift_Oy=0,
             shift_Ox=0):
        turtlesize(arrow_size)
        n = max_val
        step_pixel = self.step
        maxx = max_val * step_pixel
        maxy = maxx
        shift_Oy = step_pixel * shift_Oy
        shift_Ox = step_pixel * shift_Ox
        tracer(0)

        width(1)
        color('#d0d0d0')
        # vertical axes
        for i in range(0, 2 * n + 1):
            up()
            x = i * self.step
            goto(-maxx + x, -maxy)
            down()
            goto(-maxx + x, maxy)

        # horizontal axes
        for i in range(0, 2 * n + 1):
            up()
            y = i * self.step
            goto(-maxx, -maxy + y)
            down()
            goto(maxx, -maxy + y)

        # axis y
        color('black')
        up()
        width(2)
        setheading(90)
        goto(0 + shift_Oy, -maxy)
        down()
        goto(0 + shift_Oy, maxy)
        stamp()

        # axis x
        color('black')
        up()
        width(2)
        goto(-maxx, 0 + shift_Ox)
        down()
        goto(maxx, 0 + shift_Ox)
        setheading(0)
        stamp()

        update()

    def add_point(self, x, y, xlabel_delta=None, ylabel_delta=None,
                  point_name=None, dot_size=10):
        up()
        goto(x * self.step, y * self.step)
        dot(dot_size)
        if xlabel_delta is not None:
            if ylabel_delta is not None:
                if point_name is not None:
                    goto(xcor() + xlabel_delta, ycor() + ylabel_delta)
                    write(point_name, font=('Arial', 24, 'normal'))

    def add_line(self, x1, y1, x2, y2, vector=False):
        tracer(0)
        up()
        goto(x1 * self.step, y1 * self.step)
        down()
        goto(x2 * self.step, y2 * self.step)
        if vector:
            setheading(atan2((y2 - y1), (x2 - x1)) / pi * 180)
            stamp()
        update()
