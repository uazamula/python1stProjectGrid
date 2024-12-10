# B (188) Невільний песик
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2022-2023 н.р.
# https://uoi.eolymp.space/uk/problems/188

# input
n, x1, y1, x2, y2 = map(int,input().split())
pos=[0 for i in range(n)]
r=pos[:]
for i in range(n):
    pos[i], r[i] = map(int,input().split())
# main part
def res():
    for i in range(n):
        dog_inside = (x1-pos[i])**2+y1**2<=r[i]**2
        hive_inside = (x2-pos[i])**2+y2**2<=r[i]**2
        if dog_inside != hive_inside:
            return f'NO\n{i+1}'
    return 'YES'

print(res())