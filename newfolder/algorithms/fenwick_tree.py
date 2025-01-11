# Дано масив а. Знайти суму перших семи елементів a.
# !!! бітові операції (&, |,  ^) мають нижчий пріоритет, ніж + або -
# https://www.youtube.com/watch?v=objfzBahJW4&list=PL4ECjTneTeIIJNv2Asp1Q1DnGOtkiwo81
a = [5, 6, 8, 10, -5, 3, 2, 11, 1, 12]
k = 2
n = len(a)
T = [a[i] for i in range(n)]
while k <= n:
    for i in range(k - 1, n, k):
        T[i] += T[i - k // 2]
    k *= 2


def sum_t(numer):
    if numer == 0:
        return 0
    res = 0
    i = numer - 1
    while i > -1:
        # print('index=', i)
        res += T[i]
        i = (i & (i + 1)) - 1
    return res

l,r=1,5

print(sum_t(r)-sum_t(l-1))
