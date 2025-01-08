# A (55) Міжнародна олімпіада
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2021-22 ІI тур
# https://uoi.eolymp.space/uk/problems/55
# https://archive.uoi.ua/static/ujgoi-22-v2-tutorials.pdf - розбір
# 100%
year = int(input())
tasks = 0
if year == 1989:
    tasks = 1
elif 1990 <= year <= 1992:
    tasks = 2
elif year == 1993:
    tasks = 4
elif year in [2009, 2010]:
    tasks = 8
else:
    tasks = 6
print(tasks)
