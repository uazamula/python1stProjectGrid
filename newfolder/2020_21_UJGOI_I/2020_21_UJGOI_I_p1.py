# A (27) Тестування
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2020-21 І тур
# https://uoi.eolymp.space/uk/problems/27
# https://www.youtube.com/watch?v=CWj4YgOxvew - розбір
#

n = int(input())
a = list(map(int, input().split()))
pos = -1
remainder_of_unique = 0
x = a[0] % 2 + a[1] % 2 + a[2] % 2
if x == 0 or x == 1:
    remainder_of_unique = 1
if x == 2 or x == 3:
    remainder_of_unique = 0
for i in range(n):
    if a[i] % 2 == remainder_of_unique:
        pos = i + 1
        break
print(pos)
