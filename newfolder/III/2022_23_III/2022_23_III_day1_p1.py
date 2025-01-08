# A (182) Піксельний равлик
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/182
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/3/2023-1.pdf -завдання

# https://archive.uoi.ua/static/uoi-3-23-tutorials.pdf розбір

# 100%

k = int(input())
ans = 1 + (4*(k-1) if k>1 else 1) + 2*(k+2) + k+1 + k

print(ans)