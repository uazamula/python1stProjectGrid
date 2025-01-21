# B (118) Себек і сусіди
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2019-2020 н.р.
# https://uoi.eolymp.space/uk/problems/118
# http://3.66.171.105/wp-content/uploads/2020/02/tour-2.pdf - умова
# https://archive.uoi.ua/static/uoi-3-20-tutorials.pdf - розбір
# 100%
n, m = map(int, input().split())
main_diag = 'no'
side_diag = 'no'
for i in range(n):
    if i * n + (i + 1) == m:
        main_diag = 'yes'
        break
for i in range(n):
    if n * (i + 1) - i == m:
        side_diag = 'yes'
        break

print(main_diag, side_diag)
