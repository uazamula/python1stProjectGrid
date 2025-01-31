# B (98) Козак Вус та чарівні черевики
# Всеукраїнська олімпіада з інформатики ІІІ етап День 2 2021-2022 н.р.
# https://uoi.eolymp.space/uk/problems/98
# https://www.youtube.com/watch?v=ezG-aG44wmY -розбір
# https://archive.uoi.ua/static/uoi-3-22-tutorials.pdf - розбір

# 100%
k = int(input())
ans = 0

while k>1:
    ans+=1
    k=k//2

# TODO
print(ans)