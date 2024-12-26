# A (32) Знову функція?
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2020-21 IІ тур

# https://uoi.eolymp.space/uk/problems/32
# https://www.youtube.com/watch?v=TCHtw2k13lc
# https://www.youtube.com/watch?v=u01p3PyZ6z4

from math import sqrt
n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    a=arr[i][0]
    b=arr[i][1]
    c=arr[i][2]
    d=arr[i][3]

    x=(a+c)/2
    y=(b+d)/2
    f=sqrt((x-a)**2+(y-b)**2)+sqrt((x-c)**2+(y-d)**2)
    print(f)
# Є кращий і більш короткий варіант