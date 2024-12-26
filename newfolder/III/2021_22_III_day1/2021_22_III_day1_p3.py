# C (94) Ксоня та двокольорова фігура
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2021-2022 н.р.

# https://uoi.eolymp.space/uk/problems/94
# https://www.youtube.com/watch?v=t8iMBUrDMUw&list=PL_iXyua4WefmWxTGIE3D_fGT4lkS21wiQ - розбір

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
elif w>=4*b or b>=4*w:
    print(-1)
else:
    print('хз')
