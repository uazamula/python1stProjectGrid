# G[B] (15) Степан і сірники
# Всеукраїнська олімпіада з інформатики ІІІ етап Тур 2 2012-2013 н.р.
# https://drive.google.com/file/d/0BzXzAlavBkWxMi1famRXdkZTWlE/view?resourcekey=0-9tt3mjFHjgw0tOXZlYNmFA

# https://uoi.eolymp.space/uk/problems/15

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
res = ['yes' for i in range(n)]
for i in range(n):
    a[i].sort()

for i in range(n):
    d = {}
    for j in range(12):
        d[a[i][j]] = 1 if a[i][j] not in d else (d[a[i][j]] + 1)
    for key in d:
        if d[key] % 4 != 0:
            res[i] = 'no'
            break

for i in range(n):
    print(res[i])
