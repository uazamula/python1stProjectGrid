# D (249) Кольоровий рядок
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2024 I тур
# https://uoi.eolymp.space/uk/problems/249
# https://oi.in.ua/wp-content/uploads/2024/01/ujgoi-24-v1-ukr-statements.pdf

# 100%

n = int(input())
a = list(map(int, input()))
count1 = 0
for el in a:
    if el == 1:
        count1 += 1

if count1 != n:
    print('No')
else:
    print('Yes')
