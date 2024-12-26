# A (92) Ксоня та олімпіада
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2021-2022 н.р.
# https://uoi.eolymp.space/uk/problems/92
# https://www.youtube.com/watch?v=t8iMBUrDMUw&list=PL_iXyua4WefmWxTGIE3D_fGT4lkS21wiQ - розбір

n,m,w,t = [int(x) for x in input().split()]
ans = 0
i=0
while ans<=n and t-i*w>=0:
    ans+=m
    i+=1
ans=min(n,ans)
#todo
print(ans)