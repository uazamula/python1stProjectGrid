from math import *
n = int(input())
a = list(map(int, input().split()))

d = {20: 0, 40: 0, 60: 0, 80: 0, 100: 0}
for i in range(n):
    d[a[i]] += 1

count = d[100]
if d[80] >= d[20]:
    count += d[80]
    if d[60] >= d[40]:
        count += d[60]
    else:
        count += d[60]
        d[40] -= d[60]
        count += int(ceil((d[40]) / 2))
else:
    count += d[80]
    d[20] -= d[80]
    if d[60] > d[40]:
        count += d[40]
        d[60] -= d[40]
        if 2 * d[60] >= d[20]:
            count += d[60]
        else:
            count += int(ceil((d[60] * 60 + d[20] * 20) / 100))
    elif d[60] == d[40]:
        count += d[40] + int(ceil(d[20] * 20 / 100))
    else:
        count += d[60]
        d[40] -= d[60]
        if 3 * d[40] <= d[20]:
            d[20] -= 3 * d[40]
            count += d[40] + int(ceil((d[20] * 20) / 100))
        elif 2 * d[20] <= d[40]:
            count += d[20]
            d[40] -= 2 * d[20]
            count += int(ceil((d[40]) / 2))
        else:
            count += int(ceil((d[40] * 40 + d[20] * 20) / 100))
print(count)