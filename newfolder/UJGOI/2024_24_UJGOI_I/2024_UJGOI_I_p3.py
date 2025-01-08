# C (248)  Кольоровi м’ячики
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2024 I тур
# https://uoi.eolymp.space/uk/problems/248
# https://oi.in.ua/wp-content/uploads/2024/01/ujgoi-24-v1-ukr-statements.pdf

# 100%

y1, b1 = map(int, input().split())
y2, b2 = map(int, input().split())
y3, b3 = map(int, input().split())

boxes = [[y1, b1], [y2, b2], [y3, b3]]
imaxblue = -1
maxblue = -1
imaxyellow = -1
maxyellow = -1

for i in range(len(boxes)):
    if maxblue < boxes[i][1]:
        maxblue = boxes[i][1]
        imaxblue = i
    if maxyellow < boxes[i][0]:
        maxyellow = boxes[i][0]
        imaxyellow = i

res = -1


if imaxblue != imaxyellow:
    iy = list({0, 1, 2}.difference({imaxyellow}))
    ib = list({0, 1, 2}.difference({imaxblue}))
    res = 0
    for i in iy:
        res += boxes[i][0]
    for i in ib:
        res += boxes[i][1]
else:
    boxes.sort(key=lambda x: -(x[0] + x[1]))
    if boxes[0][0] > boxes[0][1]:
        res = boxes[0][1]
        res += min(boxes[2][1], boxes[1][1])
        res += boxes[1][0] + boxes[2][0]
    else:
        if boxes[0][0] < boxes[0][1]:
            res = boxes[0][0]
            res += min(boxes[2][0], boxes[1][0])
            res += boxes[1][1] + boxes[2][1]
        else:
            if boxes[1][0] < boxes[1][1]:
                res = boxes[0][1] + boxes[2][1] + boxes[1][0] + boxes[2][0]
            else:
                res = boxes[0][0] + boxes[2][0] + boxes[1][1] + boxes[2][1]

print(res)
