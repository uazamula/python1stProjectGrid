n, m = map(int, input().split())
ai = list(map(int, input().split()))
arr = [[ai[0], 1]]
k = 0
s = 2 ** 0
res = ai[0]
if n == 1:
    while True:
        if s >= m:
            # print(res)
            break
        k += 1
        if len(arr) == 1:

            if arr[0][0] % 2 == 0:
                arr[0][0] = arr[0][0] // 2
                # arr[0][1]=arr[0][1]
                arr.append([arr[0][0] - 1, arr[0][1]])
            else:
                arr[0][0] = arr[0][0] // 2
                arr[0][1] = 2 * arr[0][1]
        else:

            if arr[0][0] % 2 == 0:
                arr[0][0] = arr[0][0] // 2
                arr[0][1] = arr[0][1]
                arr[1][0] = arr[0][0] - 1
                arr[1][1] = arr[0][1] + 2 * arr[1][1]
            else:
                arr[0][0] = arr[0][0] // 2
                arr[0][1] = 2 * arr[0][1] + arr[1][1]
                arr[1][0] = arr[0][0] - 1
                arr[1][1] = arr[1][1]

        arr.sort(key=lambda x: -x[0])

        if m <= s + arr[0][1] and m >= s or len(arr) == 1:
            res = arr[0][0]
        else:
            res = arr[1][0]
        s += 2 ** k

        if len(arr) > 1:
            if arr[0][0] == arr[1][0]:
                # print(arr[0][0])
                arr[0][1] += arr[1][1]
                arr.pop(1)
else:
    print('oops')

print(res)
# print('r')
# print('k=',k,'s=',s)
# print ('n=',n,'m=',m,ai)
# print(arr)
