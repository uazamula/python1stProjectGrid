# Дано масив а. Знайти масив T для дерева Фенвіка.
a = [5, 6, 8, 10, -5, 3, 2, 11, 1, 12]
k = 1
n = len(a)
T = [a[i] for i in range(n)]
while 2 ** k <= n:
    for i in range(2 ** k - 1, n, 2 ** k):
        T[i] += T[i-(2**(k-1))]
    k += 1

for i in range(n):
    print(T[i], end='  ')