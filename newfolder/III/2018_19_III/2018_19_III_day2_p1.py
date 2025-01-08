# A (137) Газон у Потоколяндії
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2018-2019 н.р.
# https://uoi.eolymp.space/uk/problems/137
#  - умова
# http://3.66.171.105/wp-content/uploads/2019/02/uoi-reg-2019-2-ed.pdf - розбір
# 100%

n,k = map(int,input().split())
if n%k==0:
    x=n//k
    print(x)
elif 2*k>n:
    print(3)
else:
    x= n//k+1
    print(x)