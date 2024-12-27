

# Успішно склавши сесію, Петрик збирається відправитись автівкою до своїх
# батьків у Кременчук, відстань до якого від університету рівна d кілометрів.
# Машина Петрика не є новою, тому споживає цілих w літрів бензину кожен
# кілометр дороги. По дорозі до рідної домівки розміщено n заправок,
# кожна з яких пропонує пальне за ci​ гривень за літр та розміщена
# на відстані xi​ кілометрів від точки відправлення. Проте, на подив,
# кожна заправка пропонує свій унікальний вид бензину, які змішувати між собою
# в баку не можна.
# Перед поїздкою Петрик хоче замінити розмір бака для пального, проте не знає
# на який саме. Допоможіть Петрику визначити мінімальний розмір бака для
# пального такий, що вартість дороги до родичів буде мінімальною.
# Тобто першочергово слід мінімізувати затрати на пальне.
# Гарантується, що початково бак пустий та існує таке i, що xi=0.


#d = 10  # distance
#w = 10  # gaz per km
#n = 4  # gas stations
#c = [3, 4, 2, 1]  # price
#x = [0, 1, 2, 9]  # distance to gas station

# read
d, w = map(int, input().split())
n = int(input())
c_unsorted = list(map(int, input().split()))  # price
x_unsorted = list(map(int, input().split()))  # distance to gas station

# sorting
cx = []
for i in range(n):
    cx.append([c_unsorted[i], x_unsorted[i]])
cx.sort(key=lambda x: (x[0], -x[1]))

# main
cmin = cx[0][0]
dist_to_uni = cx[0][1]
delta = d - dist_to_uni

for i in range(1, len(cx)):
    if cx[i][0] <= cmin:
        if cx[i][1] <= dist_to_uni:
            if dist_to_uni - cx[i][1] >= delta:
                delta = dist_to_uni - cx[i][1]
            dist_to_uni = cx[i][1]

    else:
        if cx[i][1] <= dist_to_uni:
            cmin = cx[i][0]
            if dist_to_uni - cx[i][1] >= delta:
                delta = dist_to_uni - cx[i][1]
            dist_to_uni = cx[i][1]

print(delta * w)