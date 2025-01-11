# Дано масив а. Знайти масив T для дерева Фенвіка.
# https://www.youtube.com/watch?v=uSFzHCZ4E-8 - реалізація дещо інша,
# принцип той самий
a = [5, 6, 8, 10, -5, 3, 2, 11]
k = 2
n = len(a)
T = [a[i] for i in range(n)]
while k <= n:
    for i in range(k - 1, n, k):
        T[i] += T[i-k//2]
    k *= 2

for i in range(n):
    print(T[i], end='  ')