# A (164) Рівняння
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2017-2018 н.р.
# https://uoi.eolymp.space/uk/problems/164

# 100%
a, b, c = map(int, input().split())


def res():
    if a + b == c:
        return f'{a}+{b}={c}'
    if a == b + c:
        return f'{a}={b}+{c}'
    if b > 0 and a // b == c:
        return f'{a}/{b}={c}'
    if c > 0 and a == b // c:
        return f'{a}={b}/{c}'
    if a - b == c:
        return f'{a}-{b}={c}'
    if a == b - c:
        return f'{a}={b}-{c}'
    if a * b == c:
        return f'{a}*{b}={c}'
    if a == b * c:
        return f'{a}={b}*{c}'


print(res())
