# G. Додавання
# Ліміт на час виконання 1 секунда
# Ліміт використання пам'яті 256 мегабайтів
# 50 спроб відправити цю задачу
# Дано n цілих чисел a1, a2, … , an. За одну операцію ви можете додати одне число до іншого. Тобто,
# виконати операцію ai = ai + aj
# , де i ≠ j. Виконайте не більше 2n операцій, щоб зробити масив
# неспадним. Тобто, a1 ≤ a2 ≤ ⋯ ≤ an. Зверніть увагу, що вам необов'язково мінімізувати кількість
# операцій. Головне, щоб кількість не перевищувала 2n.
# Вхідні дані
# Перший рядок містить одне ціле число n (1 ≤ n ≤ 103
# ).
# Другий рядок містить n цілих чисел a1, a2, … , an (∣ai∣ ≤ 109
# ).
# Вихідні дані
# У першому рядку виведіть одне ціле число k (0 ≤ k ≤ 2n) — кількість операцій.
# У кожному з наступних k рядків виведіть по два цілі числа i та j (1 ≤ i, j ≤ n, i ≠ j), це означає, що
# виконається операція ai = ai + aj
# .
# Абсолютне значення будь-якого числа у будь-який момент не має перевищувати 1018
# .
# Оцінювання
# Розв'язок, який буде працювати правильно для тестів, у яких n = 2, набиратиме принаймні 20 балів.
# Розв'язок, який буде працювати правильно для тестів, у яких усі числа додатні, набиратиме
# принаймні 50 балів.
# Приклади
# Нижче ви знайдете приклади вхідних даних та відповідей, які має вивести ваша програма.
# Вхідні дані №1
# 4
# -5 4 -3 9
# Відповідь №1
# 1
# 3 4

# Опис ідеї розвʼязання
# Задача G. Додавання. Нехай у нас всі числа додатні. Тоді ми можемо за n − 1 операцію розв’язати
# задачу: до другого числа додамо перше, до третього друге, і так далі. Таким чином і-те число — це сума
# перших і чисел. Оскільки всі числа додатні, то новий масив буде зростати. Нехай у нас всі числа
# від’ємні. Будемо робити це саме, але навпаки. До передостаннього числа додамо останнє, до третього
# числа з кінця, додамо друге число з кінця, і так далі. Якщо ж у нас є як і від’ємні числа, так і додатні, то
# знайдемо максимальне і мінімальне число. Нехай m1 — максимальне число, а m2 — мінімальне. Якщо
# m1 ≥ |m2|, то ми можемо до всіх чисел, крім m1, додати m1. Це зробить всі числа додатними. Для цього
# нам потрібно рівно n − 1. А таку задачу ми вже вміємо розв’язувати за n − 1. Якщо ж m1 < |m2|, то до всіх
# чисел, крім m2, додамо m2. Всі числа вийдуть від’ємними. Таку задачу також вміємо розв’язувати.
# 12
# 1 100
# 2 20
# 3 40
# 4 40
# 5 50
# 6 50
# 6 60
# 7 70
# 7 80
# 8 90
# 9 100
# 10 100

n = int(input())
a = list(map(int, input().split()))
k = 0
res = []
if n == 2:
    if a[0] > a[1]:
        if abs(a[0]) >= abs(a[1]) and a[1] < 0:
            k += 2
            res = [[2, 1], [2, 1]]
        if abs(a[0]) >= abs(a[1]) and a[1] >= 0:
            k += 1
            res = [[2, 1]]
        if a[0] <= 0:
            k += 1
            res = [[1, 2]]
        if abs(a[0]) < abs(a[1]) and a[0] > 0:
            k += 2
            res = [[1, 2], [1, 2]]
else:
    if min(a) >= 0:
        for i in range(1, n):
            if a[i - 1] > a[i]:
                a[i] += a[i - 1]
                k += 1
                res.append([i + 1, i])
    else:
        if max(a) <= 0:
            # for i in range(n):
            #     a[i]+=10**9
            for i in range(1, n)[::-1]:
                # print(i)
                if a[i - 1] > a[i]:
                    a[i - 1] += a[i]
                    k += 1
                    res.append([i, i + 1])
        else:
            max_el = max(a)
            min_el = min(a)
            if abs(max_el) < abs(min_el):
                max_el = min_el
            max_el_index = a.index(max_el)

            # print(max_el, max_el_index)
            for i in range(n):
                if i != max_el_index:
                    a[i] += max_el
                    k += 1
                    res.append([i + 1, max_el_index + 1])
            if a[max_el_index] >= 0:
                for i in range(1, n):
                    if a[i - 1] > a[i]:
                        a[i] += a[i - 1]
                        k += 1
                        res.append([i + 1, i])
            else:
                for i in range(1, n)[::-1]:
                    # print(i)
                    if a[i - 1] > a[i]:
                        a[i - 1] += a[i]
                        k += 1
                        res.append([i, i + 1])

print(k)
for i in range(k):
    print(res[i][0], res[i][1])

