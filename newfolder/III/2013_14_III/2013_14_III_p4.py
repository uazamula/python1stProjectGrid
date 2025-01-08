# D (80) Гарні числа
# Всеукраїнська олімпіада з інформатики ІІІ етап 2013-2014 н.р.

# https://uoi.eolymp.space/uk/problems/80
# http://gimn14.mypsx.net/schoololymp/joomla/index.php/home?start=72

# 40% (part is wrong, part is out of time)

import math

n = int(input())
a = list(map(int, input().split()))
p = 1
number = None
res = 'Beautiful'
for i in range(n):
    p *= a[i]
for i in range(2, int(math.isqrt(p)) + 1):
    if p % (i * i) == 0:
        number = i
        break
print(res if number is None else number)
