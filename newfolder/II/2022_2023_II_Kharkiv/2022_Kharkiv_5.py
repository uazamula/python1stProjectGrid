# E (23) Коригування масивів
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/23

n = int(input())
a = list(map(int, input().split()))
b = a[:]
asc = True
if a[0] > 0:
    b[0] = -a[0]
for i in range(1, n):
    if a[i] < b[i - 1] or a[i] > 0:
        if -b[i] >= b[i - 1]:
            b[i] = -a[i]
        if b[i] < b[i - 1]:
            asc = False
            break
if asc:
    print('YES')
    print(' '.join(map(str, b)))
else:
    print('NO')
