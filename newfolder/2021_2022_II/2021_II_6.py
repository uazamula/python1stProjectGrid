# 6/ Прямі
#
# Дано n точок на декартовій системі координат. Тобто кожна точка має координати (x,y).
# Знайдіть кількість трійок точок, які знаходяться на одній горизонтальній або вертикальній прямій. Тобто, потрібно порахувати кількість таких трійок (a,b,c), що 1≤a<b<c≤n та pa​, pb​, pc​ — на одній прямій, де pi​ — i-та точка.
# Для 50% тестів точок рівно три.
# Вхідні дані
# Перший рядок містить одне ціле число n (3≤n≤100).
# Кожен з наступних n рядків містить по два цілі числа xi​ та yi​ (1≤xi​,yi​≤1000) — координати i-ої точки.
# Гарантується, що всі точки різні.
# Вихідні дані
# Виведіть кількість трійок точок, що знаходяться на одній прямій.
# Приклади
# Вхідні дані №1
# 6
# 1 1
# 1 2
# 1 3
# 2 2
# 2 3
# 3 3
# Відповідь №1
# 2
# Вхідні дані №2
# 3
# 5 6
# 5 3
# 5 10
# Відповідь №2
# 1
# Замітка
# У першому прикладі є дві трійки точок, що знаходяться на одній прямій — це трійки [(1,1),(1,2),(1,3)] та [(1,3),(2,3),(3,3)]. Зверніть увагу, що трійка [(1,1),(2,2),(3,3)] не рахується через те, що вона формує пряму по діагоналі, а нам потрібні лише ті, які формують або горизонтальні прямі, або вертикальні.
# У другому прикладі є одна трійка [(5,6),(5,3),(5,10)].
# Оцінювання
# Ваш розв'язок отримає принаймні 50% балів, якщо воно буде правильно працювати для n=3.
n = int(input())
import math
coordx=[i for i in range(n)]
coordy=[i for i in range(n)]
for i in range(n):
 coordx[i], coordy[i]= list(map(int, input().split()))
coordx.sort()
coordy.sort()
sum=0
def countsum(coords):
 global sum
 points=1
 for i in range(1,n):
  if coords[i-1]==coords[i]:
   points+=1
   if i==n-1 and points>=3:
    sum+=math.factorial(points)/6/math.factorial(points-3)
  else:
   if points>=3:
    sum+=math.factorial(points)/6/math.factorial(points-3)
   points=1
countsum(coordx)
countsum(coordy)
print(int(sum))