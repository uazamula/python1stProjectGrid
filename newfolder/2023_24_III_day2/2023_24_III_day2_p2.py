# B (268) Хрестики-нулики
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2023-2024 н.р.
# https://uoi.eolymp.space/uk/problems/268
a = []
for i in range(3):
    a.append(list(input()))
b = []
for i in range(3):
    b.append(list(input()))
countxa = 0
count0a = 0
countxb = 0
count0b = 0

isequal = True
countchanges = 0

for i in range(3):
    for j in range(3):
        if a[i][j] == 'X':
            countxa += 1
        if a[i][j] == '0':
            count0a += 1
        if b[i][j] == 'X':
            countxb += 1
        if b[i][j] == '0':
            count0b += 1
        if a[i][j] != b[i][j]:
            isequal = False
            countchanges += 1


def res():
    if isequal:
        return 'YES'
    if countchanges > 1:
        return 'NO'

    if count0a + countxa + 1 == count0b + countxb:
        if count0a == count0b and countxb == count0a + 1 \
                or countxa == countxb and count0b == countxb:
            return 'YES'
    return 'NO'


print(a, b, countxa, count0a, countxb, count0b)
print(res())