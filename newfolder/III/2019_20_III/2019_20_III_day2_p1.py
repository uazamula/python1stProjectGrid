# A (117) Себек та рівняння
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2019-2020 н.р.
# https://uoi.eolymp.space/uk/problems/117
# http://3.66.171.105/wp-content/uploads/2020/02/tour-2.pdf - умова
# https://archive.uoi.ua/static/uoi-3-20-tutorials.pdf - розбір
# 100%

x, y, z, k = map(int, input().split())
a = -1
b = -1
c = -1
if x ** 3 + y ** 2 + z == k:
    a, b, c = x, y, z
if x ** 3 + z ** 2 + y == k:
    a, b, c = x, z, y
if y ** 3 + x ** 2 + z == k:
    a, b, c = y, x, z
if y ** 3 + z ** 2 + x == k:
    a, b, c = y, z, x
if z ** 3 + x ** 2 + y == k:
    a, b, c = z, x, y
if z ** 3 + y ** 2 + x == k:
    a, b, c = z, y, x

print(a, b, c)
