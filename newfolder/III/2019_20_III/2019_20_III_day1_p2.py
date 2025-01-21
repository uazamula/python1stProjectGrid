# B (113) Козак Вус і гармата
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2019-2020 н.р.
# https://uoi.eolymp.space/uk/problems/113
# http://3.66.171.105/wp-content/uploads/2020/02/tour-1.pdf - умова
# https://archive.uoi.ua/static/uoi-3-20-tutorials.pdf - розбір
# 100%
n = int(input())
a=list(map(int, input().split()))
ans=1
shot_len=0
# print(shot_len, ans)

for i in range(1,n):
    if shot_len<=a[i]-2:
        shot_len+=1
    else:
        ans+=1
        shot_len=1
    # print(i, shot_len, ans)

if n==1:
    ans=0
print (ans)
