# H. (26) Коригування рядків
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/26
# TODO
n = input()
maybe=False
count=0
nold=n
spells=[]
for i in range(len(n)//2):
    if n[i]!=n[-1-i]:
        count+=1
        if count>=3:
            break
        spells.append(n[i])
        spells.append(n[-1-i])

if count>=3:
    print('NO')
elif count==0:
    print('YES')
else:
    if count==2:
        pass
    if count==1:
        pass
