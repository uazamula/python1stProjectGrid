# B (93) Ксоня та алфавітне коло
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2021-2022 н.р.

# https://uoi.eolymp.space/uk/problems/93
# https://www.youtube.com/watch?v=t8iMBUrDMUw&list=PL_iXyua4WefmWxTGIE3D_fGT4lkS21wiQ - розбір


n = int(input())
a = [ord(i) for i in input()]
a=a[:]+a[:]
count=0
maxlength=1
for i in range(1,2*n):
    if a[i]-a[i-1]==1:
        count+=1
        maxlength=max(maxlength,count)
    else:
        count=1


print(maxlength)