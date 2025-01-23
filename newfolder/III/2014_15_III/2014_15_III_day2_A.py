# A (127) День іменинника
# Всеукраїнська олімпіада з інформатики ІІІ етап день 2 2014-2015 н.р.

# https://uoi.eolymp.space/uk/problems/123
# https://static.eolymp.com/content/sd/sduseuu0u91ld9un0f264i9ov0.pdf
# http://soippo.edu.ua/images/%D0%9E%D0%BB%D1%96%D0%BC%D0%BF%D1%96%D0%B0%D0%B4%D0%B8/Inform_Zbirniki_olimpiad/Informatika_2015.pdf
# тут є задачі 2014-15 н.р. ІІ, ІІІ етапів, умова і розвʼязок,
# крім D, E першого дня, але і для них є підказки

#100%
n,k = map(int,input().split())
a=list(map(int,input().split()))
d={}
for el in a:
    if el in d:  d[el]+=1
    else:  d[el]=1

arr=[]
count=0
for key in d:
    if d[key]>=k:
        chocolades=d[key]//k
        count+=chocolades
        for i in range(chocolades):
            arr.append(key)
if arr:
    arr.sort()
    print(count)
    print (' '.join(map(str,arr)))
else:
    print(0)
