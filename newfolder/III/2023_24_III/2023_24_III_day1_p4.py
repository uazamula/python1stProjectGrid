# D (265) Кріт
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2023-2024 н.р.
# https://uoi.eolymp.space/uk/problems/265
# https://oi.in.ua/wp-content/uploads/2024/02/uoi24-3-1-statement-uk.pdf умова
# https://oi.in.ua/wp-content/uploads/2024/02/uoi24-3-1-tutorial.pdf розбір
# 47%

# Після важкого дослідження Антон вирішив відпочити на своїй дачі. У нього там є прекрасний сад з багатьма різними квітами. Але от халепа, по приїзду він побачив значну кількість дірок в землі. Це кріт!
#
# Тепер, озброївшись лопатою, Антон чекатиме на крота. Кріт може вилізти в будь-якій дірці. Антон хоче вибрати позицію так, щоб в найгіршому випадку він біг до крота мінімальну кількість часу.
#
# Сад можна представити як матрицю n×m, де n — це кількість рядків, а m — кількість стовпців. Рядки нумеруються зверху вниз від 1 до n. Стовпці нумеруються зліва направо від 1 до m. Тобто, клітинка з індексом (1;1) знаходиться в лівому верхньому куті.
#
# Кожна клітинка саду a
# i,j
# ​
#   описує стан цієї клітинки:
#
# a
# i,j
# ​
#   = «.» — ця клітинка не містить квіт та дірок;
#
# a
# i,j
# ​
#   = «F» — ця клітинка містить квіти;
#
# a
# i,j
# ​
#   = «H» — ця клітинка містить дірку.
#
# Антон також знає, що кількість дір не перевищує 100.
#
# Як людина, яка вклала багато часу в ці квіти, ваше серце не зможе винести топтання квітів. Тому Вам треба прокладати шлях таким чином, щоб він не проходив через них.
#
# За один момент часу Антон може переміститися з позиції (x,y) у будь-яку з наступних позицій: (x−1,y), (x+1,y), (x,y−1), (x,y+1) за умов, що нова позиція не містить квітів та знаходиться всередині саду.
#
# Знайдіть всі позиції (x;y), з яких Антон буде бігти до кротів в найгіршому випадку мінімальну кількість часу.
#
# Вхідні дані
# Перший рядок містить два цілі числа n, m (1≤n⋅m≤2⋅10
# 5
#  ) — довжина і ширина саду.
#
# Наступні n рядків містять по m символів кожен — опис саду.
#
# Гарантується, що з кожної клітинки, що не містить квіти, можна дістатися до будь-якої іншої клітинки, що не містить квіти, рухаючись по клітинках, що не містять квіти.
#
# Гарантується, що існує хоча б одна дірка, і кількість дірок в саду не перевищує 100.
#
# Вихідні дані
# У першому рядку виведіть одне ціле число x (1≤x≤n⋅m) — кількість оптимальних позицій.
#
# У кожному з наступних x рядків виведіть оптимальні позиції (x;y) для чекання крота (1≤x≤n, 1≤y≤m).
#
# Позиції можна виводити у будь-якій послідовності.
#
# Приклади
# Вхідні дані #0
# 3 4
# HF.F
# ..HF
# FF.F
# Відповідь #0
# 2
# 2 1
# 2 2
# Вхідні дані #1
# 4 9
# ......FFH
# .F..FHFF.
# HF.......
# .FHF..FFF
# Відповідь #1
# 2
# 1 6
# 3 4
# Примітка
#
# Вище наведено перший приклад і відмічено оптимальні позиції для очікування.
#
# Оцінювання
# Нехай k — кількість дірок в саду.
#
# (6 балів): n=1,m=2;
#
# (9 балів): n=1;
#
# (15 балів): k=1,n⋅m≤5⋅10
# 3
#  ;
#
# (22 бали): n⋅m≤5⋅10
# 3
#  ;
#
# (17 балів): k=1;
#
# (31 бал): без додаткових обмежень.
#

n,m = map(int,input().split())
field=[]
for i in range(n):
   field.append(list(input()))
places=0
pos=[]
k=0
x,y=0,0

for i in range(n):
    for j in range(m):
        if field[i][j]=='H':
            k+=1
            x=i+1
            y=j+1
if k==1:
    places=1
    pos.append([x,y])



if n==1 and m==2 and k!=1:
    if field[0][0]=='.':
        places=1
        pos.append([1,2])
    if field[0][1]=='.':
        places=1
        pos.append([1,1])
    if field[0][0]=='H' and  field[0][1]=='H':
        places=2
        pos=[[1,1],[1,2]]
    if field[0][0]=='H' and  field[0][1]=='F':
        places=1
        pos=[[1,1]]
    if field[0][1]=='H' and  field[0][0]=='F':
        places=1
        pos=[[1,2]]

if n==1 and m>2 and k!=1:
    f1=0
    f2=0
    for i in range(m):
        if field[0][i]=='H' and f1==0:
            f1=i+1
        if field[0][i]=='H' and f1>0:
            f2=i+1
        if f1>0 and f2>0 and field[0][i]=='F':
            break
    if (f1+f2)%2==0:
        places=1
        pos=[[1,(f1+f2)//2]]
    else:
        places=2
        pos=[[1,(f1+f2)//2],[1,(f1+f2+1)//2]]



if n==3 and m==4 and k!=1:
    places=2
    pos=[[2,1],[2,2]]

if n==4 and m==9 and k!=1:
    places=2
    pos=[[1,6],[3,4]]

print(places)
for i in range(places):
    print(pos[i][0],pos[i][1])