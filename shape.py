import math


# Shape class
class Shape:
    def __init__(self, pType, pArea):
        self.type = pType
        self.area = pArea

    def __str__(self):
        return '%s of area %4.2f units square' % (self.type,
                                                  self.area)


# Square subclass
class Square(Shape):
    def __init__(self, pLength):
        super().__init__('Square', 0)
        self.length = pLength
        self.area = self.length * self.length
        self.type='Rvcxbv'




# Triangle subclass
class Triangle(Shape):
    def __init__(self, pBase, pHeight):
        super().__init__('Triangle', 0)
        self.base = pBase
        self.height = pHeight
        self.area = 0.5 * self.base * self.height


# Circle subclass
class Circle(Shape):
    def __init__(self, pRadius):
        super().__init__('Circle', 0)
        self.radius = pRadius
        self.area = math.pi * self.radius * self.radius
