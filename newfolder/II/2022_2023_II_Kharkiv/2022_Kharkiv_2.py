# B. (20) Сертифікати
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/20

M = int(input())
K = float(input())
if K >= M * 0.9:
    print("OUTSTANDING")
elif K >= M * 0.74:
    print("EXCELLENT")
elif K >= M * 0.6:
    print("VERY GOOD")
else:
    print("PARTICIPANT")
