# C. (11) Степан і пари
# Всеукраїнська олімпіада з інформатики ІІІ етап Тур 1 2012-2013 н.р.
# https://drive.google.com/file/d/0BzXzAlavBkWxMi1famRXdkZTWlE/view?resourcekey=0-9tt3mjFHjgw0tOXZlYNmFA

# https://uoi.eolymp.space/uk/problems/11

n = int(input())
res = 0
for i in range(n):
    res += n // (i + 1)
print(res)
