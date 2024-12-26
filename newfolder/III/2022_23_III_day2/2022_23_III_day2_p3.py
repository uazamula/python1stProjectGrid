# C (189) Дороги Потоколяндії
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/189

import math

n = int(input())
eps = 0.000000001


def res():
    if abs(math.log(n, 2) - round(math.log(n, 2))) < eps:
        return 'YES'
    if n % 2 != 0:
        return f'NO\n{1} {n}'
    else:
        return f'NO\n{1} {n // 2}'


print(res())