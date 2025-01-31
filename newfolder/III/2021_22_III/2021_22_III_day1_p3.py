# C (94) Ксоня та двокольорова фігура
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2021-2022 н.р.

# https://uoi.eolymp.space/uk/problems/94
# https://www.youtube.com/watch?v=t8iMBUrDMUw&list=PL_iXyua4WefmWxTGIE3D_fGT4lkS21wiQ - розбір
# https://archive.uoi.ua/static/uoi-3-22-tutorials.pdf - розбір

# 100%

w, b = [int(x) for x in input().split()]
#todo
n, m = w, b
if w==b:
    print(f'1 {m+n}')
    print(n*'BW')
elif w-b==1:
    print(f'1 {m+n}')
    print('W'+(w-1)*'BW')
elif b-w==1:
    print(f'1 {m+n}')
    print('B'+(b-1)*'WB')
elif b==4 and w==1:
    print(3,3)
    print('.B.')
    print('BWB')
    print('.B.')
elif w==4 and b==1:
    print(3,3)
    print('.W.')
    print('WBW')
    print('.W.')
elif w>b and w<=3*b+1:
    n=3
    m=b*2+1
    row1=w-(b+1)
    row3=0
    if row1-b>0:
        row3=row1-b
        row1=b
    row1 = row1*'.W'
    row1 = row1+(m-len(row1))*'.'
    row3 = row3*'.W'
    row3 = row3+(m-len(row3))*'.'


    print(f'{n} {m}')
    print(row1)
    print(b*'WB'+'W')
    print(row3)
elif b>w and b<=3*w+1:
    n=3
    m=w*2+1
    row1=b-(w+1)
    row3=0
    if row1-w>0:
        row3=row1-w
        row1=w
    row1 = row1*'.B'
    row1 = row1+(m-len(row1))*'.'
    row3 = row3*'.B'
    row3 = row3+(m-len(row3))*'.'


    print(f'{n} {m}')
    print(row1)
    print(w*'BW'+'B')
    print(row3)
else:
    print(-1)

