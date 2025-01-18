# Дано масив а. Знайти суму перших семи елементів a.
# !!! бітові операції (&, |,  ^) мають нижчий пріоритет, ніж + або -
# https://www.youtube.com/watch?v=objfzBahJW4&list=PL4ECjTneTeIIJNv2Asp1Q1DnGOtkiwo81
a = [5, 6, 8, 10, -5, 3, 2, 11, 1, 12, 3, 4, 5, 6, 7, -1]
n = len(a)


def get_t():  # формування T
    k = 2
    T = [a[i] for i in range(n)]
    while k <= n:
        for i in range(k - 1, n, k):
            T[i] += T[i - k // 2]
        k *= 2
    return T


T = get_t()[:]


def sum_t(numer):  # порядковий номер елемента
    if numer == 0:
        return 0
    res = 0
    i = numer - 1
    while i > -1:
        # print('index=', i)
        res += T[i]
        i = (i & (i + 1)) - 1
    return res


def add_d(i, d):  # d прирощення елемента з індексом i
    while i < n:
        T[i] += d
        i = (i | (i + 1))


# Приклад розрахунку
l, r = 1, 5  # порядкові номери елементів на лівій і правій границі

print('sum=', sum_t(r) - sum_t(l - 1))
for t in T:
    print(t, end='  ')
print()
print('sum=', sum_t(10))

add_d(7, 10)
for t in T:
    print(t, end='  ')
print()
print('sum=', sum_t(10))
