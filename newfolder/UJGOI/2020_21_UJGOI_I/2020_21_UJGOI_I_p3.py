# C (29) Ігорчик та яблучка
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2020-21 І тур
# https://uoi.eolymp.space/uk/problems/29
# https://www.youtube.com/watch?v=CWj4YgOxvew - розбір
n, m, k = map(int, input().split())
a = [n, m, k]
a.sort()
if a[0] + a[1] >= a[2]:
    res = sum(a) // 2
else:
    res = a[0] + min(a[2] - a[0], a[1])
print(res)
