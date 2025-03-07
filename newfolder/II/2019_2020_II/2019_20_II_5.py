# E (73) Стрічка
# UOI 2021-2022. II stage. Kyiv ?

# https://uoi.eolymp.space/uk/problems/73
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2021.pdf умова + розбір

# 100%

# Ліміт на час виконання 1 секунда
# Ліміт використання пам'яті 256 мегабайтів
# 50 спроб відправити цю задачу
# Дана стрічка довжини n сантиметрів. Кожен сантиметр може бути або червоним, або синім. Вам
# потрібно вирізати з цієї стрічки менші стрічки довжини два сантиметри, де один сантиметр червоний,
# а інший синій. Знайдіть, яку максимальну кількість таких стрічок можна зробити зі стрічки, яка нам
# дана.
# Вхідні дані
# Перший рядок містить рядок s (1 ≤ ∣s∣ ≤ 105
# ).
# Якщо i-ий символ B, то це означає, що i-ий сантиметр синій. Якщо ж i-ий символ R, то це означає,
# що i-ий сантиметр червоний.
# Вихідні дані
# Виведіть одне ціле число.
# Приклади
# Нижче ви знайдете приклади вхідних даних та відповідей, які має вивести ваша програма.
# Вхідні дані №1
# BBBRRRBBR
# Відповідь №1
# 3
arr = list(input())
s=0
i=1
is_forbid=False
while i<len(arr):
    if arr[i-1]!=arr[i]and  not is_forbid:
        s+=1
        is_forbid=True
    else:
        is_forbid=False
    i+=1

print(s)