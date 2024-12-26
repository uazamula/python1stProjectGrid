# C. () Сума тризначних паліндромів
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/21
nstr = input()
n = int(nstr)

res = 0
if n // 100 != n % 10:

    if n % 10 == 0:
        res = int(nstr[0] + nstr[1] + nstr[0])
    else:
        res = int(nstr[0] + nstr[1] + nstr[0]) + int(
            nstr[2] + nstr[1] + nstr[2])
else:
    s = 0
    for i in range(10):
        if int(nstr[1]) != i:
            s += i
    res = ((n // 100) * 100 + n % 10) * 9 + 10 * s

print(res)
