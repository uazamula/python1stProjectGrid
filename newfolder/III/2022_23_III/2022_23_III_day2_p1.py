# B (187) Галерея
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/187

# https://www.kievoi.ippo.kubg.edu.ua/kievoi/3/2023-2.pdf - завдання
# https://archive.uoi.ua/static/uoi-3-23-tutorials.pdf розбір

# 100%
a, b, c = map(int, input().split())
ans = max(a + b, a + c, b + c)
print(ans)
