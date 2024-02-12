# Задача 4. «Зелена пляма» (30 балів)
# Ім’я вхідного файлу: input.txt
# Ім’я вихідного файлу: output.txt
# Максимальний час роботи на одному тесті: 1с
#
# Два прожектори трикутної форми утворюють на стiнi двi плями,
# одну - блакитного, а  другу - жовтого  кольору.
# Визначити площу плями зеленого кольору,
# яка  утвориться  при накладаннi двох плям - блакитної i жовтої, та  форму (
# кiлькiсть вершин) зеленої плями. Перший  рядок  файлу  мiстить цiлочисельнi
# координати однiєї плями: X1, Y1, X2, Y2, X3, Y3, а в другому рядку – такi ж
# координати вершин iншої плями. Всі числа по модулю менші 1000.

# Вихiдний файл  повинен мiстити у першому рядку – кiлькiсть її вершин,
# у другому – площу зеленої плями (з двома  знаками  пiсля  коми).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# point
p0 = Point(-1, 0)
# vertices of triangle
p11 = Point(-1, 2)
p12 = Point(0.5, -1)
p13 = Point(6, 0)

p21 = Point(1, 0)
p22 = Point(2, -2)


def sign(p1: Point, p2: Point, p3: Point):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)


def point_in_triangle(pt, v1, v2, v3):
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def intercept_point(p1, p2, p3, p4):
    ax = p2.x - p1.x
    ay = p2.y - p1.y
    bx = p4.x - p3.x
    by = p4.y - p3.y
    det = ay * bx - ax * by
    if det == 0:
        return None
    else:
        x = (ay * bx * p1.x + ax * bx * (p3.y-p1.y) - ax * by * p3.x) / det
        y = -(ax * by * p1.y + ay * by * (p3.x-p1.x) - ay * bx * p3.y) / det
        return (x, y)


print(point_in_triangle(p0, p11, p12, p13))
print(intercept_point(p11, p12, p21, p22))
