# Задача 3 «Обробка фотографій з космосу» (30 балів)
# Ім’я вхідного файлу: input.txt
# Ім’я вихідного файлу: output.txt
# Максимальний час роботи на одному тесті: 3с
# Комп'ютер перетворив фотографiю частини поверхнi планети,
# зроблену з космiчного апарата, в двомiрну таблицю Map[1:M, 1:N],
# елементи якої - цифри 0 (суша) та 1 (вода).
# Є 4 типи поверхнi сушi (материк, острiв, пiвострiв та берег)
# та 3 типи поверхнi води (море,  озеро та затока).
# Тип  кожної  клiтини можна визначити в залежностi вiд того, до яких типiв
# було однозначно вiднесено ранiше деякi з чотирьох сусiднiх
# по горизонталi та  вертикалi клiтини:
#
# Тип 2 - материк - клiтина сушi, оточена чотирма клiтинами сушi.
# Тип 3 - острiв - клiтина сушi, оточена чотирма клiтинами води.
# Тип 4 - пiвострiв - клiтина сушi, що має 3 сусiднiх клiтини води,
#       або 2 сусiднiх клiтини води та >= 1 клiтини  пiвострова,
#       або 1 сусiдню клiтину води та >= 2 клiтин пiвострова.
# Тип 5 - берег - клiтина сушi, що не належить до типiв 2-4.
# !!!Тип 6 - море - клiтина води, що має хоча б одну сусiдню клiтину моря.
# Тип 7 - затока - клiтина моря, що має 2 або 3 сусiднiх клiтини сушi,
#       або 4 сусiднi клiтини затоки,
#       або 1 сусiдню клiтину сушi та не менше 2 клiтин затоки.
# Тип 8 - озеро - клiтина води, що не належить до типiв 6, 7.
#
# Вважається, що двi клiтини типу 4 належать до одного  пiвострова,
# якщо мiж ними можна пройти по сушi, переходячи на сусiднi клiтини типу 4
# по горизонталi або вертикалi. Таким же чином двi  клiтини типу  7
# належать до однiєї затоки,  якщо мiж ними можна пропливти по водi,
# перепливаючи на сусiднi клiтини типу 7 по горизонталi або вертикалi.
# Двi клiтини типу 8 належать до одного озера,  якщо мiж ними можна пропливти
# по водi, перепливаючи на сусiднi клiтини типу 8  по горизонталi або вертикалi.
# Крайнi рядки та стовпчики таблицi займає море.
# ЗАВДАННЯ: написати програму, яка для заданої таблицi-карти:
# 1. визначить номер типу кожної її клiтини;
# 2. обчислить кiлькість островiв, пiвостровiв,заток та  озер  на картi.
# ТЕХНIЧНI УМОВИ:
# 1. Кожна "фотографiя" в файлi має таку структуру:
#  – в першому рядку – число M,  кiлькiсть рядкiв таблицi Map,
#  – в другому рядку – число  N, кiлькiсть  стовпчикiв таблицi Map,
#  – в кожному з наступних M рядкiв – N цифр вiдповiдного рядка таблицi.
# 2. Результат для кожної "фотографiї" повинен складатися з:
#  - кiлькостей  островiв, пiвостровiв, заток та  озер  в окремих рядках.
# 3. Програма повинна обробляти таблицi для 2≤ M ≤20, 2≤N ≤ 40.

list = [[1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1], ]
M = len(list)
N = len(list[0])
count_islands=0
count_lakes=0
count_peninsulas=0
count_bays=0
last_checked_cell=[0, 0]
print(list)
print(M)
print(N)


# Тип 2 - материк - клiтина сушi, оточена чотирма клiтинами сушi.
# Тип 3 - острiв - клiтина сушi, оточена чотирма клiтинами води.
def umova(rowi, colj, isWater, types):
    return list[rowi][colj] == isWater and (list[rowi + 1][colj] in types) and (
                list[rowi][colj + 1] in types) and (
                list[rowi - 1][colj] in types) and (
                list[rowi][colj - 1] in types)


# Тип 4 - пiвострiв - клiтина сушi, що має 3 сусiднiх клiтини води,
#       або 2 сусiднiх клiтини води та >= 1 клiтини  пiвострова,
#       або 1 сусiдню клiтину води та >= 2 клiтин пiвострова.
def isPeninsula(rowi, colj):
    countWater = 0;
    if (list[rowi + 1][colj] in [1, 6, 7, 8]):
        countWater += 1
    if (list[rowi - 1][colj] in [1, 6, 7, 8]):
        countWater += 1
    #     print(rowi)
    #     print(colj+1)
    if (list[rowi][colj + 1] in [1, 6, 7, 8]):
        countWater += 1
    if (list[rowi][colj - 1] in [1, 6, 7, 8]):
        countWater += 1
    countLand = 0;

    if (list[rowi + 1][colj] == 4):
        countLand += 1
    if (list[rowi - 1][colj] == 4):
        countLand += 1
    if (list[rowi][colj + 1] == 4):
        countLand += 1
    if (list[rowi][colj - 1] == 4):
        countLand += 1

    return list[rowi][colj] in [0, 2, 3, 4, 5] and (
                countWater == 3 or (countWater == 2 and countLand >= 1) or (
                    countWater == 1 and countLand >= 2))


# Тип 7 - затока - клiтина моря, що має 2 або 3 сусiднiх клiтини сушi,
#       або 4 сусiднi клiтини затоки,
#       або 1 сусiдню клiтину сушi та не менше 2 клiтин затоки.
def isBay(rowi, colj):
    countBay = 0;
    if (list[rowi + 1][colj] == 7):
        countBay += 1
    if (list[rowi - 1][colj] == 7):
        countBay += 1
    if (list[rowi][colj + 1] == 7):
        countBay += 1
    if (list[rowi][colj - 1] == 7):
        countBay += 1

    countLand = 0;
    if (list[rowi + 1][colj] in [0, 2, 3, 4, 5]):
        countLand += 1
    if (list[rowi - 1][colj] in [0, 2, 3, 4, 5]):
        countLand += 1
    if (list[rowi][colj + 1] in [0, 2, 3, 4, 5]):
        countLand += 1
    if (list[rowi][colj - 1] in [0, 2, 3, 4, 5]):
        countLand += 1

    return list[rowi][colj] == 6 and (
                countLand == 3 or countLand == 2 or countBay == 4 or (
                    countLand == 1 and countBay >= 2))


# Розставляння по периметру Тип 6 - море
for i in range(0, M):
    for j in range(0, len(list[i])):
        if (i == 0 or i == M - 1 or j == 0 or j == N - 1):
            list[i][j] = 6

        # Перевірка на Тип 6 - море
ranges = [[1, M - 1, 1, N - 1, 1, 1], [1, M - 1, N - 2, 0, 1, -1],
          [M - 2, 0, 1, N - 1, -1, 1], [M - 2, 0, N - 2, 0, -1, -1]]
# Потрібно з чотирьох боків іти
for k in range(4):
    for i in range(ranges[k][0], ranges[k][1], ranges[k][4]):
        for j in range(ranges[k][2], ranges[k][3], ranges[k][5]):
            if (list[i][j] == 1 and (
                    (list[i + 1][j] == 6) or (list[i][j + 1] == 6) or (
                    list[i - 1][j] == 6) or (list[i][j - 1] == 6))):
                list[i][j] = 6
print()
for rowi in range(M):
    s = ''
    for colj in range(len(list[rowi])):
        s += str(list[rowi][colj])
    print(s)

for k in range(4):
    print(k)
    print(ranges[k])
    for i in range(ranges[k][0], ranges[k][1], ranges[k][4]):
        for j in range(ranges[k][2], ranges[k][3], ranges[k][5]):

            # Перевірка на Тип 2 - материк
            #         if(list[rowi][colj]==0 and list[rowi+1][colj]==0 and list[rowi][colj+1]==0
            #            and list[rowi-1][colj]==0 and list[rowi][colj-1]==0):

            if (umova(i, j, 0, [0, 2, 3, 4, 5])):
                list[i][j] = 2

            # Перевірка на Тип 3 - острів
            elif (umova(i, j, 0, [1, 6, 7, 8])):
                list[i][j] = 3
                count_islands+=1
            # Перевірка на Тип 4 - півострів
            elif (isPeninsula(i, j)):
                list[i][j] = 4
            # Перевірка на Тип 5 - берег
            elif (list[i][j] == 0):
                list[i][j] = 5
            # Перевірка на Тип 7 - затока
            elif (isBay(i, j)):
                list[i][j] = 7
            # Перевірка на Тип 8 - озеро
            elif (list[i][j] == 1):
                list[i][j] = 8

print()
for rowi in range(M):
    s = ''
    for colj in range(len(list[rowi])):
        s += str(list[rowi][colj])
    print(s)
# Задача зводиться до пошуку кількості компонентів звʼязності графа
# (півострови, озера, затоки - окремо для кожного типу)
while True:
    break
