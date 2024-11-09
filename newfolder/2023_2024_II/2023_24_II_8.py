n, m = map(int, input().split())
ai = list(map(int, input().split()))
arr = [[ai[i], 1] for i in range(n)]
k = 0
arr.sort(key=lambda x: -x[0])
keys = {el for el in ai}
res = arr[0][0]
d = {}
for key in ai:
    d[key] = 1 if key not in d else (d[key] + 1)
s = 2 ** 0 if n == 1 else d[max(keys)]
max_key = max(keys)

while True:

    if s >= m:
        break
    if n > 0:# TODO ця умова завжди виконується
        k += 1

        new_el = max_key // 2
        if max_key % 2 == 0:
            d[new_el] = d[max_key] if new_el not in d else (
                        d[new_el] + d[max_key])
            d[new_el - 1] = d[max_key] if (new_el - 1) not in d else (
                        d[new_el - 1] + d[max_key])
            keys.update([new_el, new_el - 1])
        else:
            d[new_el] = 2 * d[max_key] if new_el not in d else (
                        d[new_el] + 2 * d[max_key])
            keys.add(new_el)

        keys.remove(max_key)
        del d[max_key]
        max_key = max(keys)
        s += d[max_key]

        if m <= s and max_key > 1:
            res = max_key
        else:
            res = 1

    else:  # TODO можна видаляти цю гілку, вона для n=1

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

print(res)
