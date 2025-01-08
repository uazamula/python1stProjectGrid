# D (185) Ділянки
# Всеукраїнська олімпіада з інформатики ІІІ етап День 1 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/185
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/3/2023-1.pdf -завдання

# https://oi.in.ua/wp-content/uploads/2023/01/LeuuW4bPSewGhtwFEnFcdBmj8mofKm7c.pdf розбір

# 100%

# Вимірювання земельної ділянки − важлива геодезична процедура. Щоб отримати точні числові показники, процедуру вимірювання повинні виконувати професійні геодезисти.
#
# Розглянемо таку задачу. Нехай є квадратна ділянка, яку геодезисти розділили на n
# 2
#   прямокутних ділянок, провівши (n−1) вертикальних ліній та (n−1) горизонтальних ліній. Пронумеруємо стовпчики та рядки діляночок так, як вказано на малюнку (масштабу не дотримано). Тобто рядки нумеруються знизу вгору цілими числами від 1 до n; а стовпчики нумеруються зліва направо цілими числами від 1 до n.
#
# Ділянки, які знаходяться на перетині i-го стовпчика та i-го рядка (1≤=i≤=n), будемо називати «головною діагоналлю». Ділянки, які знаходяться на перетині (i+1)-го стовпчика та i-го рядка (1≤=i≤=n−1), будемо називати «побічною діагоналлю».

# Вам відомі площі ділянок на головній та побічній діагоналях. Обчисліть площу ділянки, що знаходиться на перетині p-го стовпчика та q-го рядка.
#
# Вхідні дані
# Перший рядок містить одне ціле число n (2≤n≤1000).
#
# Другий рядок містить n цілих чисел a
# 1
# ​
#  ,a
# 2
# ​
#  ,…,a
# n
# ​
#   (1≤a
# i
# ​
#  ≤10
# 9
#  ) — площі ділянок на головній діагоналі.
#
# Третій рядок містить n−1 цілих чисел b
# 1
# ​
#  ,b
# 2
# ​
#  ,…,b
# n−1
# ​
#   (1≤b
# i
# ​
#  ≤10
# 9
#  ) — площі ділянок на побічній діагоналі.
#
# Четвертий рядок містить два цілі числа p та q (1≤p,q≤n) — координати ділянки, площу якої треба обчислити.
#
# Вихідні дані
# Виведіть площу ділянки, що знаходиться на перетині p-го стовпчика та q-го рядка.
#
# Ми хочемо знати точне значення площі, тому відповідь треба виводити у факторизованому вигляді. Іншими словами, відповідь треба представити як декілька рядків, кожен з яких містить два цілі числа p
#   обов'язково просте та всі числа p
#   різні, а число s
#   — ціле та не дорівнює нулю. Шукана площа має дорівнювати:
#,
# де k — кількість рядків у відповіді. Рядки треба відсортувати за зростанням простих чисел p
# i
# ​
#  . Нагадаємо, що число X вважається простим, якщо воно має рівно два цілі додатні дільники: 1 та X.
# Якщо шукана площа дорівнює 1, то виведіть дві одиниці: «1 1».

# input
import time

n = int(input())
a = []
b = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p, q = map(int, input().split())


def fsquare(a, b):
    numbers = {}

    def factorize(number, pos):
        d = int(number ** 0.5)
        i = 1
        step = 1

        while d > 1:
            if i == 3:
                step = 2
            i += step

            if i > d: break

            if number % i == 0:
                if i in numbers:
                    numbers[i] = numbers[i] + pos
                else:
                    numbers[i] = pos
                number = number // i
                d = int(number ** 0.5)

                i = 1
                step = 1
        if number in numbers:
            numbers[number] = numbers[number] + pos
        else:
            numbers[number] = pos

    if q >= p:
        for k in range(p - 1, q):
            factorize(a[k], 1)
        for k in range(p - 1, q - 1):
            factorize(b[k], -1)
    else:
        for k in range(q - 1, p - 1):
            factorize(b[k], 1)
        for k in range(q, p - 1):
            factorize(a[k], -1)

            # print(numbers)
    for key in list(numbers):
        if numbers[key] == 0:
            del numbers[key]

    if len(numbers) > 1:
        if 1 in numbers:
            # print('if')
            del numbers[1]
    else:
        if len(numbers) == 0:
            # print('else')
            numbers = {1: 1}

    return numbers


def tostr(factorize):
    s = ''
    arr = []
    for key in factorize:
        arr.append([key, factorize[key]])
    arr.sort(key=lambda x: x[0])
    for i in range(len(arr)):
        s += str(arr[i][0]) + ' ' + str(arr[i][1]) + '\n'
    return s


# p -> column!
# q -> row!
# if p - 1 == q:
# print(tostr(fsquare([b[q - 1]], [1])))
# if p == q:
#   print(a[p-1])
# print(tostr(fsquare([a[p - 1]], [1])))
# print (n,a,b,p,q)
start = time.time()
print(tostr(fsquare(a, b)))
end = time.time()
print(end-start)