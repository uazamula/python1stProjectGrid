# A (182) Піксельний равлик
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/182

k = int(input())
ans = 1 + (4*(k-1) if k>1 else 1) + 2*(k+2) + k+1 + k


# TODO
print(ans)