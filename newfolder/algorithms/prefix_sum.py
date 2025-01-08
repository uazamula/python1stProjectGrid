# Дано масив а. Знайти всі суми трьох сусідніх елементів a.
a = [5, 6, 8, 10, -5, 3, 2, 11, 1, 12]

prefix_sum = [0]
for i in range(len(a)):
    prefix_sum.append(prefix_sum[i] + a[i])

my_sum = []
for i in range(3, len(prefix_sum)):
    my_sum.append(prefix_sum[i] - prefix_sum[i - 3])

print(prefix_sum)
print(my_sum)
