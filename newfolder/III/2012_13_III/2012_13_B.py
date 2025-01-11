# B.(10) День святого Валентина
# Всеукраїнська олімпіада з інформатики ІІІ етап Тур 1 2012-2013 н.р.
# https://drive.google.com/file/d/0BzXzAlavBkWxMi1famRXdkZTWlE/view?resourcekey=0-9tt3mjFHjgw0tOXZlYNmFA

# https://uoi.eolymp.space/uk/problems/10
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
uglity = 10 ** 10

for i in range(n - k + 1):
    if a[i + k - 1] - a[i] < uglity:
        uglity = a[i + k - 1] - a[i]
print(uglity)