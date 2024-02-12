# На екзамені з алгоритмів Петрик витягнув нещасливу задачу, тому вельми
# просить вашої допомоги. Перед вами стандартна шахова дошка 8×8, клітинки
# якої пронумеровані зліва направо від a до h та знизу вгору від 1 до 8.
# Серед білих фігур дошці можуть бути всі види фігур, крім короля, а серед
# чорних навпаки — є лише один король. Також відомо що фігури розставлені
# абсолютно довільно, тобто їх розміщення може не підпорядковуватись
# стандартним правилам шахів (білі навіть можуть мати забагато фігур певного
# типу). Вашою задачею є визначити, у якому положенні знаходиться чорний
# гравець: мат, пат чи звичайне положення.

# Довідка з шахів: Шах — тактичний хід, при якому проходить напад на короля
# суперника. Мат — ситуація, коли король опиняється під шахом, і у гравця
# нема жодного можливого ходу, після якого король перестав би перебувати під
# шахом. Пат — становище, коли сторона, котра повинна ходити, не може це
# зробити, бо всі її фігури позбавлені можливості зробити хід, при цьому
# король не перебуває під шахом.

# Правила ударів/ходів фігур в рамках задачі: Королева — б'є по вертикалях,
# діагоналях та горизонталях, на яких вона перебуває, але вона не може
# перескакувати через інші фігури. Тура — б'є по вертикалях та горизонталях,
# на яких вона перебуває, але не може перескакувати через інші фігури. Слон —
# б'є по діагоналях, на яких він перебуває, але не може перескакувати через
# інші фігури. Кінь — хід конем складається строго з двох пересувань: на одне
# поле по вертикалі чи горизонталі, потім віддаляючись від вихідного поля на
# одне поле по діагоналі. Це єдина фігура, яка може перескакувати через інші
# фігури. Пішак — б'є по діагоналі на одну клітинку в сторону суперника (
# таким чином білі пішаки завжди б'ють тільки по діагоналі вгору). Король —
# пересувається зі свого поля на одне з вільних суміжних полів (у тому числі
# й по діагоналі), що не перебуває під ударом фігур суперника. Може бити
# фігуру, яка знаходиться на суміжному полі, якщо вона не під ударом.
#
# Вхідні дані Вхідні дані містять 8 рядків, кожен з яких складається з 8
# символів. Кожен символ задає відповідну клітинку шахової дошки: символ «.»
# позначає пусту клітинку символ «p» позначає пішака символ «r» позначає туру
# символ «n» позначає коня символ «b» позначає слона символ «Q» позначає
# королеву символ «K» позначає короля Гарантується, що є рівно один король.
# Вихідні дані У випадку мату у першому рядку виведіть «Checkmate»,
# а в наступних рядках виведіть клітинки всіх фігур, що завдають шах у
# довільному порядку. У випадку пату у першому рядку виведіть «Stalemate». В
# іншому випадку виведіть «Continue» та у довільному порядку всі клітинки,
# у які король може зробити хід.
import copy

no_king = None
is_checkmate = False
movement_to = []
e = '.'
K = 'K'
p = 'p'
r = 'r'
b = 'b'
n = 'n'
Q = 'Q'
chess = [[e, e, e, n, e, n, e, e, ],
         [e, e, n, e, e, r, n, b, ],
         [e, n, e, e, r, e, n, e, ],
         [e, e, n, e, e, e, n, e, ],
         [e, e, e, n, n, n, n, e, ],
         [e, r, b, e, Q, e, e, n, ],
         [e, e, e, e, e, e, e, e, ],
         [e, p, e, e, e, K, e, e, ], ]

chess_old = [[el for el in line] for line in chess]  # copy.deepcopy(chess)
check = []

k_pos = None
for i in range(8):
    for j in range(8):
        if chess[i][j] == K:
            k_pos = (i, j)


def game():
    for i in range(8):
        for j in range(8):
            if chess[i][j] != e:
                # pawn
                if chess[i][j] == p:
                    if k_pos[0] == i - 1 and abs(k_pos[1] - j) == 1:
                        print()
                        check.append([i, j])
                # rook, Queen
                if chess[i][j] == r or chess[i][j] == Q:
                    if k_pos[0] == i:
                        check.append([i, j])
                        for k in range(min(k_pos[1], j) + 1, max(k_pos[1], j)):
                            if chess[i][k] != e:
                                check.pop()
                                break
                    if k_pos[1] == j:
                        check.append([i, j])
                        for k in range(min(k_pos[0], i) + 1, max(k_pos[0], i)):
                            if chess[k][j] != e:
                                check.pop()
                                break
                # bishop, Queen
                if chess[i][j] in [b,Q]:
                    if abs(k_pos[0] - i) == abs(k_pos[1] - j):
                        check.append([i, j])
                        for k in range(1, abs(k_pos[0] - i)):
                            add_i = round(
                                k * (k_pos[0] - i) / abs(k_pos[0] - i))
                            add_j = round(
                                k * (k_pos[1] - j) / abs(k_pos[1] - j))
                            print(k, i, j)
                            print(add_i, add_j)
                            if chess[i + add_i][j + add_j] != e:
                                check.pop()
                                break
                #knight
                if chess[i][j] == n:
                    if abs(k_pos[0] - i) == 1 and abs(k_pos[1] - j) == 2 or \
                            abs(k_pos[0] - i) == 2 and abs(k_pos[1] - j) == 1:
                        check.append([i, j])

    print(check)


def get_movement(border_condition, addx, addy):
    if border_condition:
        global check
        global k_pos
        check = []
        k_pos = (old_k_pos[0] + addx, old_k_pos[1] + addy)
        chess[old_k_pos[0]][old_k_pos[1]] = e
        chess[k_pos[0]][k_pos[1]] = K
        game()
        for i in range(8):
            print(chess[i])
        print(check)
        if not check:
            movement_to.append([k_pos[0], k_pos[1]])
        print(movement_to)
        k_pos = (old_k_pos[0], old_k_pos[1])
        for i in range(8):
            for j in range(8):
                chess[i][j] = chess_old[i][j]


game()
checkmate_maybe = copy.deepcopy(check)
old_k_pos = (k_pos[0], k_pos[1])
print(chess_old)

get_movement(old_k_pos[0] > 0, -1, 0)
# chess = list(chess_old)
print(chess_old)
get_movement(old_k_pos[1] > 0, 0, -1)
print(checkmate_maybe)
get_movement(old_k_pos[0] > 0 and old_k_pos[1] > 0, -1, -1)
get_movement(old_k_pos[0] < len(chess) - 1 and old_k_pos[1] > 0, 1, -1)
get_movement(old_k_pos[0] < len(chess) - 1, 1, 0)
get_movement(old_k_pos[0] < len(chess) - 1 and old_k_pos[1] < len(chess[0]) - 1,
             1, 1)
get_movement(old_k_pos[1] < len(chess[0]) - 1, 0, 1)
get_movement(old_k_pos[0] > 0 and old_k_pos[1] < len(chess[0]) - 1, -1, 1)
if movement_to:
    print('Continue')
    print(movement_to)
if not checkmate_maybe and not movement_to:
    print('Stalemate')
if checkmate_maybe and not movement_to:
    print('Checkmate')
    print(checkmate_maybe)
