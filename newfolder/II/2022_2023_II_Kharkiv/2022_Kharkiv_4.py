# D. (22) Посміхайлики
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/22
n = int(input())
s1 = n // 105
r2 = n % 105
s2 = r2 // 15
r3 = r2 % 15
s3 = r3 // 3
r4 = r3 % 3
s4 = r4
print(s1 * ';-D', s2 * ':-D', s3 * ';-)', s4 * ':-)', sep='')
