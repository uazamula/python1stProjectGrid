# A (112) Козак Вус і екзамен
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2019-2020 н.р.
# https://uoi.eolymp.space/uk/problems/112
# http://3.66.171.105/wp-content/uploads/2020/02/tour-1.pdf - умова
# https://archive.uoi.ua/static/uoi-3-20-tutorials.pdf - розбір
# 100%
n, a, b, c = map(int, input().split())
ans = 0
if a == b:
    ans = n + c
elif a == 0 and b != 0:
    ans = n
elif a != 0 and a != b:
    ans = max(0, n - c // 4)

print(ans)