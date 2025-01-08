# B (183) Нова Пошта
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/183
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/3/2023-1.pdf -завдання

# https://oi.in.ua/wp-content/uploads/2023/01/LeuuW4bPSewGhtwFEnFcdBmj8mofKm7c.pdf розбір

# 100%
m = list(map(int, input().split()))
M1, M2 = map(int, input().split())
summ = sum(m)
cannot = False
numbers = ' 1 2 3 4 5'


def result():
    for i in range(len(m)):
        if m[i] > M1 and m[i] > M2:
            return "They can not do it!"

    if sum(m) > M1 + M2:
        return "They can not do it!"
    if sum(m) <= M1 and sum(m) <= M2:
        return ("They both can do it!")
    if sum(m) <= M1 and sum(m) > M2:
        return ("Vasyl can do it!")
    if sum(m) > M1 and sum(m) <= M2:
        return ("Petro can do it!")

    for i in range(len(m)):
        if m[i] <= M1 and summ - m[i] <= M2:
            return f"They need to work together!\nVasyl: {i + 1}\nPetro:{numbers.replace(' ' + str(i + 1), '')}"
        if m[i] <= M2 and summ - m[i] <= M1:
            return f"They need to work together!\nVasyl:{numbers.replace(' ' + str(i + 1), '')}\nPetro: {i + 1}"

    for i in range(len(m) - 1):
        for j in range(i + 1, len(m)):
            if m[i] + m[j] <= M1 and summ - (m[i] + m[j]) <= M2:
                return f"They need to work together!\nVasyl: {i + 1} {j + 1}\nPetro:{numbers.replace(' ' + str(i + 1), '').replace(' ' + str(j + 1), '')}"
            if m[i] + m[j] <= M2 and summ - (m[i] + m[j]) <= M1:
                return f"They need to work together!\nVasyl:{numbers.replace(' ' + str(i + 1), '').replace(' ' + str(j + 1), '')}\nPetro: {i + 1} {j + 1}"

    return "They can not do it!"


print(result())