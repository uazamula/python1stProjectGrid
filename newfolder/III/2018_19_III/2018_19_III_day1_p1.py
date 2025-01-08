# A (132) Козак Вус і важлива знахідка
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2018-2019 н.р.
# https://uoi.eolymp.space/uk/problems/132
# https://drive.google.com/drive/folders/1kfkzDYzTEIofYhV1fJ5SyjT51rPruzZK - умова(Терлецька)
# http://3.66.171.105/wp-content/uploads/2019/02/uoi-reg-2019-1-ed.pdf - розбір
# 100%

A, B, C, D = map(int, input().split())
a = [A, B, D, C]
b = [0, 0, 0, 0]
maxv = A * (B + C - D)
maxi = 0
for i in range(1, 4):
    b[0] = a[3]
    b[1] = a[0]
    b[2] = a[1]
    b[3] = a[2]
    a = b[:]
    if maxv < a[0] * (a[1] - a[2] + a[3]):
        maxi = i
        maxv = a[0] * (a[1] - a[2] + a[3])

print(maxi)
