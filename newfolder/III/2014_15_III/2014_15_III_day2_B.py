# B (128) Стрічка
# Всеукраїнська олімпіада з інформатики ІІІ етап день 2 2014-2015 н.р.

# https://uoi.eolymp.space/uk/problems/123
# https://static.eolymp.com/content/sd/sduseuu0u91ld9un0f264i9ov0.pdf
# http://soippo.edu.ua/images/%D0%9E%D0%BB%D1%96%D0%BC%D0%BF%D1%96%D0%B0%D0%B4%D0%B8/Inform_Zbirniki_olimpiad/Informatika_2015.pdf
# тут є задачі 2014-15 н.р. ІІ, ІІІ етапів, умова і розвʼязок,
# крім D, E першого дня, але і для них є підказки

# 100%
n, a, b, c = map(int, input().split())


def get_arr(a, b, c):
    ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ans11, ans12, ans13, ans14, ans15, ans16, ans17, ans18, ans19, ans20, ans21 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    def f(y, x):
        if x > 0 and x % a == 0:
            return x // a + y
        return 0
        # f(0,n), f(1,n-b), f(1,n-c),f(2,n-2*b),f(2,n-2*c),f(2,n-b-c)

    # if n%a==0:
    #     ans1=n//a
    # if (n-b)%a==0:
    #     ans2=(n-b)//a+1
    # if (n-2*b)%a==0:
    #     ans3=(n-2*b)//a+2
    # if (n-c)%a==0:
    #     ans4=(n-c)//a+1
    # if (n-2*c)%a==0:
    #     ans5=(n-2*c)//a+2
    # if (n-b-c)%a==0:
    #     ans6=(n-b-c)//a+2
    # 95% без нижніх рядків
    x = n - 3 * b
    if x > 0 and x % a == 0: ans7 = x // a + 3
    x = n - 3 * c
    if x > 0 and x % a == 0: ans8 = x // a + 3
    x = n - 2 * b - c
    if x > 0 and x % a == 0: ans9 = x // a + 3
    x = n - 2 * c - b
    if x > 0 and x % a == 0: ans10 = x // a + 3
    # 98% без нижніх рядків
    x = n - 4 * b
    if x > 0 and x % a == 0: ans11 = x // a + 4
    x = n - 4 * c
    if x > 0 and x % a == 0: ans12 = x // a + 4
    x = n - 2 * b - 2 * c
    if x > 0 and x % a == 0: ans13 = x // a + 4
    x = n - 3 * c - b
    if x > 0 and x % a == 0: ans14 = x // a + 4
    x = n - 3 * b - c
    if x > 0 and x % a == 0: ans15 = x // a + 4

    x = n - 5 * b
    if x > 0 and x % a == 0: ans16 = x // a + 5
    x = n - 5 * c
    if x > 0 and x % a == 0: ans17 = x // a + 5
    x = n - 3 * b - 2 * c
    if x > 0 and x % a == 0: ans18 = x // a + 5
    x = n - 3 * c - 2 * b
    if x > 0 and x % a == 0: ans19 = x // a + 5
    x = n - 4 * b - c
    if x > 0 and x % a == 0: ans20 = x // a + 5
    x = n - 4 * c - b
    if x > 0 and x % a == 0: ans21 = x // a + 5

    return [f(0, n), f(1, n - b), f(1, n - c), f(2, n - 2 * b), f(2, n - 2 * c),
            f(2, n - b - c), ans7, ans8, ans9, ans10, ans11, ans12, ans13,
            ans14, ans15, ans16, ans17, ans18, ans19, ans20, ans21]


print(max(get_arr(a, b, c) + get_arr(b, c, a) + get_arr(c, a, b)))
