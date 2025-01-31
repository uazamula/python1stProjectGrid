# B (123) Кросворд
# Всеукраїнська олімпіада з інформатики ІІІ етап день 1 2014-2015 н.р.

# https://uoi.eolymp.space/uk/problems/123
# https://static.eolymp.com/content/sd/sduseuu0u91ld9un0f264i9ov0.pdf
# http://soippo.edu.ua/images/%D0%9E%D0%BB%D1%96%D0%BC%D0%BF%D1%96%D0%B0%D0%B4%D0%B8/Inform_Zbirniki_olimpiad/Informatika_2015.pdf
# тут є задачі 2014-15 н.р. ІІ, ІІІ етапів, умова і розвʼязок,
# крім D, E першого дня, але і для них є підказки

# 100% - обмеження за часом
n = int(input())
a = [input() for i in range(n)]


def countwords(a):
    count = 0
    for row in a:
        tracked = True
        for s in range(1, n):
            if tracked and row[s] == '-' and row[s - 1] == '-':
                count += 1
                tracked = False
            if row[s] == '#':
                tracked = True
    return count


ac = [[a[j][i] for j in range(n)] for i in range(n)]
# без list comprehension втрачається 22%
# for i in range(n):
#     for j in range(n):
#         ac[i].append(a[j][i])


print(countwords(a), countwords(ac))
