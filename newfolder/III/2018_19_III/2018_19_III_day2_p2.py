# B (138) Мафія у Потоколяндії
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2018-2019 н.р.
# https://uoi.eolymp.space/uk/problems/138
#  - умова
# http://3.66.171.105/wp-content/uploads/2019/02/uoi-reg-2019-2-ed.pdf - розбір
# 100%
n, a, b = map(int, input().split())


def res():
    if b == 0:
        x = n // a
        return x if a * x == n else (x + 1)

    d = (a - b) ** 2 + 4 * b * n
    x1 = (b - a + d ** 0.5) / (2 * b)
    x2 = (b - a - d ** 0.5) / (2 * b)
    if x2 > 0:
        return x2 if x2 - int(x2) == 0 else int(x2 + 1)
    return x1 if x1 - int(x1) == 0 else int(x1 + 1)


print(res())
