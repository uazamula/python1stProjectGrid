# G (358) Квадрати
# Всеукраїнська олімпіада з інформатики ІІ етап (Kharkiv) 2024-2025 н.р.
# https://uoi.eolymp.space/uk/problems/358
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2024.pdf умова
# https://www.youtube.com/watch?v=QOVWCRvo4dE розбір (лише A-F)


# 65% (перевищено ліміт часу - 0,2 с) на eolymp
# Коротке замикання дасть суттєву економію в часі для випадків,
# де кількість 0 і 1 є приблизно однаковим

n = int(input())
N = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# опорна (перша) точка квадрата має координати (i,j). Наступна точка віддалена
# на r рядків вниз і c стовпчиків вправо
# від першої точки  (i,j)
for r in range(n-1):
    for c in range(1, n):
        # досліджуємо кожну точку
        for i in range(n - c - r):
            for j in range(r, n - c):
                s = N[i][j] + N[i + r][j + c] + N[i + c + r][j + c - r] + \
                    N[i + c][j - r]
                if s == 0 or s == 4:
                    # print(i,j, 'r=',r, 'c=',c)
                    ans += 1

print(ans)

# Variant2 з коротким замиканням  і зменшенням кількості операцій +,-
# пройшов тест на рідному порталі цієї задачі на 100%
# https://olympkh.dots.org.ua/
# на eolymp цей варіант дає лише 70% (через перевищення ліміту часу у 0.2 с)

# n = int(input())
# N = [input().split() for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         N[i][j] = True if N[i][j] == '1' else False
#
# ans = 0
# for c in range(1, n):
#     nc = n - c
#     for i in range(nc):
#         ic = i + c
#         for j in range(nc):
#             jc = j + c
#             if N[i][j] == N[i][jc] and N[i][j] == N[ic][jc] and N[i][j] == \
#                     N[ic][j]:
#                 ans += 1
#
# for r in range(1, n - 1):
#     for c in range(1, n):
#         nj = n - c
#         cmr = c - r
#         cr = c + r
#         for i in range(nj - r):
#             icr = i + cr
#             ir = i + r
#             for j in range(r, nj):
#
#                 if N[i][j] and N[ir][j + c] and N[icr][j + cmr] and N[i + c][j - r]:
#                     ans += 1
#                 if not (N[i][j] or N[ir][j + c] or N[icr][j + cmr] or N[i + c][j - r]):
#                     ans += 1
#
# print(ans)
