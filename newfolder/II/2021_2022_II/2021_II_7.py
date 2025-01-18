# G(67) Операції
# Всеукраїнська олімпіада з інформатики ІІ етап 2021-2022 н.р.

# https://uoi.eolymp.space/uk/problems/67
# https://archive.uoi.ua/static/uoi-2-22-1-tutorials.pdf розбір

# Дано n цілих чисел a1​,a2​,…,an​. Спочатку вони всі рівні нулю.
# Дано m операцій, кожен з яких описується двома числа ki​ та ci​, які означають, що ви можете ki​ разів вибрати будь-який елемент з масиву a та замінити його значення на ci​. Зверніть увагу, що елементи, які ви вибираєте, не обов'язково мають бути різними. Також ви не зобов'язані робити i-ту операцію рівно ki​ разів, ви можете виконати її будь-яку кількість разів, але не більше ki​. Також ви можете не виконувати операцію взагалі.
# Всі m операцій ви маєте виконувати послідовно. Тобто, спочатку всі заміни першої операції, потім другої, і так далі.
# Знайдіть максимальну можливу суму масиву, що може вийти в кінці.
# Вхідні дані
# Перший рядок містить два цілі числа n та m (1≤n,m≤105).
# Кожен з наступних m рядків містить по два цілі числа ki​ та ci​ (1≤ki​,ci​≤105).
# Вихідні дані
# Виведіть одне ціле число.
# Приклади
# Вхідні дані №1
# 3 2
# 2 1
# 2 3
# Відповідь №1
# 7
# Вхідні дані №2
# 10 1
# 6 3
# Відповідь №2
# 18

n, m = map(int, input().split())
k = [0 for i in range(m)]

# Закоментований нижче код дає змогу отримати
# лише 30% балів через недотримання ліміту часу

# c=[0 for i in range(m)]
# a=[0 for i in range(n)]
# for i in range(m):
# k[i],c[i]=map(int, input().split())
# for i in range(m):
# count_k=0
# for j in range(n):
# count_k+=1
# if c[i]>a[j]:
# a[j]=c[i]
# if count_k==k[i]:
# break
# a.sort()

# Спробуємо код нижче. Він не знаходить самого масиву,
# але знаходить його максимальну суму
# Саме цього вимагає умова задачі

for i in range(m):
    k[i] = list(map(int, input().split()))


def fun(e):
    return e[1]


k.sort(reverse=True, key=fun)
n_remain = n
count = 0
sum = 0
while True:
    if k[count][0] <= n_remain:
        sum += k[count][1] * k[count][0]
        n_remain -= k[count][0]
        count += 1
        if m <= count:
            break
    else:
        sum += k[count][1] * n_remain
        break
print(sum)
