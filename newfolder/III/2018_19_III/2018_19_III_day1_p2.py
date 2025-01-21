# B (133) Козак Вус і цікава задача
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2018-2019 н.р.
# https://uoi.eolymp.space/uk/problems/133
# https://drive.google.com/drive/folders/1kfkzDYzTEIofYhV1fJ5SyjT51rPruzZK - умова(Терлецька)
# http://3.66.171.105/wp-content/uploads/2019/02/uoi-reg-2019-1-ed.pdf - розбір
# 100%
n, m, p = map(int, input().split())


def res():
    if 2 * m + 6 * n == p and m >= 3:
        return f'YES\n1 {n}\n1 {n}\n{m - 2} {n}'
    if 2 * n + 6 * m == p and n >= 3:
        return f'YES\n1 {m}\n1 {m}\n{n - 2} {m}'
    sidetype34 = (p - 4 * n - 2 * m) // 2
    if 4 * n + 2 * m + 2 * sidetype34 == p and sidetype34 > 0 and sidetype34 < m and n > 1 and m > 1:
        return f'YES\n{n} {m - sidetype34}\n{1} {sidetype34}\n{n - 1} {sidetype34}'
    sidetype56 = (p - 2 * n - 4 * m) // 2
    if 2 * n + 4 * m + 2 * sidetype56 == p and sidetype56 > 0 and sidetype56 < n and n > 1 and m > 1:
        return f'YES\n{m} {n - sidetype56}\n{1} {sidetype56}\n{m - 1} {sidetype56}'
    return 'NO'


print(res())