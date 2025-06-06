# E. (5) Скрутні часи
# Всеукраїнська олімпіада з інформатики ІІ етап 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/5
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2022i.pdf (розбір)

# У зв'язку зі страхом після останніх скорочень в IT секторі Петрик хоче оцінити свою продуктивність. Він як стабільний працівник робить рівно одну робочу задачу за день, правда графік у нього специфічний: він працює a днів через b днів (тобто має a робочих днів поспіль та b вихідних після них).
# Петрик, бувши прихильником теорії хаотичного відпочинку, не працює кожен n-тий день, незалежно від того, чи є це робочим днем, чи вихідним. Проте, для компенсації, кожен m-тий день, якщо він для Петрика робочий, то він працює удвічі ефективніше, тобто робить дві задачі за день.
# Оцініть місячну продуктивність Петрика (скільки задач він зробить), якщо місяць має k днів та починається з першого робочого дня.

#a = 10
#b = 2
#n = 11
#m = 3
#k = 5

a, b, n, m, k = map(int, input().split())

tasks = 0
days = 0

for i in range(1, k + 1):
    if 1 <= i % (a + b) <= a:
        tasks += 1
        if i % m == 0 and i % n != 0:
            tasks += 1
        if i % n == 0:
            tasks -= 1

print(tasks)