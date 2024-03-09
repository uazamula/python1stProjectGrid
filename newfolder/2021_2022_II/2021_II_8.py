import time

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
        if i not in coord_i_in_col0:
            coord.append((i, 0))
if nearest_horiz < m:
    for i in range(nearest_horiz + 1, m):
        if i not in coord_j_in_lastrow:
            coord.append((n - 1, i))

sum = m * n - 1

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

most_left_figures_list = [[key, value] for key, value in
                          most_left_figures.items()]

start = time.time()
for key, value in most_bottom_figures.items():
    substr = len([0 for key2, value2 in most_left_figures.items() if
                  key2 < value and value2 < key])
    sum -= substr
print(f'time={time.time() - start}')
set1 = {(key, value) for key, value in most_left_figures.items()}
set2 = {(key, value) for value, key in most_bottom_figures.items()}

sum -= len(set1.union(set2))
print(sum)
