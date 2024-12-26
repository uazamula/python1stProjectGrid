# C. Кінь
# UOI 2022. II stage. Kyiv ?
# Ліміт на час виконання 1 секунда
# Ліміт використання пам'яті 256 мегабайтів
# 50 спроб відправити цю задачу
# Дано шахова дошка розміром 8×8. На цій дошці є лише одна фігура — кінь. Знайдіть кількість клітин,
# на яку кінь може переміститися за один хід. Нагадаємо, що кінь рухається "буквою Г". Формально,
# кінь може переміститися з клітини з координатами (x1, y1) у клітину (x2,y2), якщо
# ∣x1 − x2∣ = 1 та ∣y1 − y2∣ = 2, або ж ∣x1 − x2∣ = 2 та ∣y1 − y2∣ = 1.
# На малюнку чорний кінь може переміститися на 8 клітинок, а білий лише на 2.
# Вхідні дані
# Перший рядок містить два символи. Перший символ — англійська буква від a до h у нижньому
# регістрі. Другий символ — цифра від 1 до 8.
# Вихідні дані
# Виведіть одне ціле число.
# Приклади
# Нижче ви знайдете приклади вхідних даних та відповідей, які має вивести ваша програма.
# Вхідні дані №1
# d4
# Відповідь №1
# 8
# Вхідні дані №2
# h1
# Відповідь №2
# 2

arr = list(input())
# Variant 1
map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
c1, c2 = map[arr[0]], int(arr[1])

# todo
s=0
if 3<=c2<=6 and 3<=c1<=6:
    s=8
if c1==1 and c2 in[1,8] or c1==8 and c2 in [1,8]:
    s=2
if c1 in [2,7] and c2 in [1,8]  or  c2 in [2,7] and c1 in [1,8]:
    s=3
if 3<=c1<=6 and c2 in[1,8] or  3<=c2<=6 and c1 in[1,8]:
    s=4
if c1 in[2,7] and c2 in[2,7]:
    s=4
if c2 in[2,7] and 3<=c1<=6 or c1 in[2,7] and 3<=c2<=6:
    s=6
print(s)

#Variant2
map1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':4, 'f':3, 'g':2, 'h':1}
map2 = {1:1, 2:2, 3:3, 4:4, 5:4, 6:3, 7:2, 8:1}

c1, c2 = map1[arr[0]], map2[int(arr[1])]

# todo
s=0
if c1>=3 and c2>=3:
    s=8
if c1==1 and c2==1:
    s=2
if c1 + c2==3:
    s=3
if c1==1 and c2 in[3,4] or  c2==1 and c1 in[3,4]:
    s=4
if c1 ==2 and c2 ==2:
    s=4
if c1==2 and c2 in[3,4] or c2==2 and c1 in[3,4]:
    s=6
print(s)