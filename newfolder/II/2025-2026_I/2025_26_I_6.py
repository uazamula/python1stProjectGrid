n = int(input())
c = [int(i) for i in input().split()]

s = 0
maxs = 0
for i in range(n):
    if c[i] == 2:
        s = s + 1
        maxs = max(s, maxs)
    else:
        s = 0
if maxs > n / 2:
    print(maxs * 2)  # суператака
else:
    print(n)  # звичайна атака
