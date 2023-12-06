# У зв'язку зі страхом після останніх скорочень в IT секторі Петрик хоче оцінити свою продуктивність. Він як стабільний працівник робить рівно одну робочу задачу за день, правда графік у нього специфічний: він працює a днів через b днів (тобто має a робочих днів поспіль та b вихідних після них).
# Петрик, бувши прихильником теорії хаотичного відпочинку, не працює кожен n-тий день, незалежно від того, чи є це робочим днем, чи вихідним. Проте, для компенсації, кожен m-тий день, якщо він для Петрика робочий, то він працює удвічі ефективніше, тобто робить дві задачі за день.
# Оцініть місячну продуктивність Петрика (скільки задач він зробить), якщо місяць має k днів та починається з першого робочого дня.

a = 10
b = 2
n = 11
m = 3
k = 5

tasks = 0
days = 0

while True:
    days += 1
    is_working = not (days % (a + b) > a or days % (a + b) == 0) and days != n
    if is_working:
        tasks += 1 + int(days == m)
    print(days, is_working, tasks)
    if days == k:
        break

print(tasks)