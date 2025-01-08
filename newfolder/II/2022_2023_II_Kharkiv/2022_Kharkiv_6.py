# F(24) Відновлення масивів
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/24
# 44% because of time limit in 200ms
n,m = map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
sup=10**9+1
a.sort(key=lambda x: -x[2])
d={}
d[max(a[0][0],a[0][1])]=sup
d[min(a[0][0],a[0][1])]=a[0][2]
for i in range(1,m):
    if max(a[i][0],a[i][1]) not in d: d[max(a[i][0],a[i][1])]=a[i][2]
    if min(a[i][0],a[i][1]) not in d: d[min(a[i][0],a[i][1])]=a[i][2]
ans = [str(d[i]) for i in range(1,n+1)]
# print (a)
print(' '.join(ans))