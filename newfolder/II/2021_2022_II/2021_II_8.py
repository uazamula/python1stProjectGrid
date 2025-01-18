# H(68) Тура, але уже складніша
# Всеукраїнська олімпіада з інформатики ІІ етап 2021-2022 н.р.

# https://uoi.eolymp.space/uk/problems/68
# https://archive.uoi.ua/static/uoi-2-22-1-tutorials.pdf розбір
# 100%
n, m, k = map(int, input().split())
coord = [i for i in range(k)]
nearest_vert = -1
nearest_horiz = m
coord_i_in_col0 = []
coord_j_in_lastrow = []
for i in range(k):
    coord[i] = list(map(int, input().split()))
    coord[i] = (n - coord[i][0], coord[i][1] - 1)
    if coord[i][1] == 0 and coord[i][0] > nearest_vert:
        nearest_vert = coord[i][0]
    if coord[i][0] == n - 1 and coord[i][1] < nearest_horiz:
        nearest_horiz = coord[i][1]
    if coord[i][1] == 0:
        coord_i_in_col0.append(coord[i][0])
    if coord[i][0] == n - 1:
        coord_j_in_lastrow.append(coord[i][1])
if nearest_vert > 0:
    for i in range(0, nearest_vert):
        coord.append((i, 0))
if nearest_horiz < m:
    for i in range(nearest_horiz + 1, m):
        coord.append((n - 1, i))

ROW, COL = 0, 1
most_left_index = m
most_bottom_index = -1


def nearest_to_edge(key, value, most_remote_index):
    most_nearest_figures = {}
    for elem in coord:
        if elem[key] in most_nearest_figures:
            if (elem[value] < most_nearest_figures[
                elem[key]] and key == ROW) or (
                    elem[value] > most_nearest_figures[
                elem[key]] and key == COL):
                most_nearest_figures[elem[key]] = elem[value]
        else:
            most_nearest_figures[elem[key]] = elem[value]
    return most_nearest_figures

most_left_figures = nearest_to_edge(ROW, COL,
                                    most_left_index)  # row_num:col_num
most_bottom_figures = nearest_to_edge(COL, ROW,
                                      most_bottom_index)  # col_num:row_num

most_left_figures_list = [[] for i in range(m)]
for i in range(n):
    if i in most_left_figures:
        most_left_figures_list[most_left_figures[i]].append(i)
T = [0 for i in range(n)]
shadowed_cells = 0


def sum_t(numer):  # порядковий номер елемента
    if numer == 0:
        return 0
    res = 0
    i = numer - 1
    while i > -1:
        # print('index=', i)
        res += T[i]
        i = (i & (i + 1)) - 1
    return res


def add_d(i, d, n):  # d прирощення елемента з індексом i
    while i < n:
        T[i] += d
        i = (i | (i + 1))


for i in range(0, m):
    if i in most_bottom_figures:
        shadowed_cells += sum_t(most_bottom_figures[i])
        for el in most_left_figures_list[i]:
            add_d(el, 1, n - 1)

set1 = {(key, value) for key, value in most_left_figures.items()}
set2 = {(key, value) for value, key in most_bottom_figures.items()}
print(m * n - 1 - shadowed_cells - len(set1.union(set2)))
