# D (122) Випробування автомата
# Всеукраїнська олімпіада з інформатики ІІІ етап 2014-2015 н.р.

# https://uoi.eolymp.space/uk/problems/122
# https://static.eolymp.com/content/sd/sduseuu0u91ld9un0f264i9ov0.pdf
# http://soippo.edu.ua/images/%D0%9E%D0%BB%D1%96%D0%BC%D0%BF%D1%96%D0%B0%D0%B4%D0%B8/Inform_Zbirniki_olimpiad/Informatika_2015.pdf
# тут є задачі 2014-15 н.р. ІІ, ІІІ етапів, умова і розвʼязок,
# крім D, E першого дня, але і для них є підказки

# 100%
n = int(input())
a = list(map(int, input().split()))
ans = 0
getcoin = 0
for i in range(n):
    if a[i] == 5:
        getcoin += 1
    else:
        increment = (a[i] - 5) // 5 - getcoin
        if increment > 0:
            ans = ans + increment
            getcoin = 0
        else:
            getcoin = -increment

print(ans)

# набір тестів
# (1)
# вхід
# 3
# 10 5 100
# результат
# 19

# (2)
# вхід
# 3
# 5 5 10
# результат
# 0

# (3)
# вхід
# 4
# 50 5 5 5
# результат
# 9

# (4+)
# вхід
# 23
# 5 50 5 10 10 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 100
# результат
# 11

# (5+)
# вхід
# 23
# 5 50 5 10 10 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 10
# результат
# 9
