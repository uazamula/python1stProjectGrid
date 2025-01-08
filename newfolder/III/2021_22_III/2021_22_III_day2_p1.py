# A (97) Козак Вус та таємний лист
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2021-2022 н.р.
# https://uoi.eolymp.space/uk/problems/97
# https://www.youtube.com/watch?v=ezG-aG44wmY -розбір
# https://archive.uoi.ua/static/uoi-3-22-tutorials.pdf - розбір

# 100%
a, b, c = map(int, input().split())
ans = a*((b+c)+b*c)
print(ans)