# A. (1) Борги
# Всеукраїнська олімпіада з інформатики ІІ етап 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/1
# https://oi.in.ua/wp-content/uploads/2022/12/U8WVYuD4GHItSKNoRZjIUIPgavACGK.pdf - умови
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2022i.pdf (розбір)

# В Аліси зараз a гривень. Вона пам'ятає, що Петрик винен їй b гривень,
# а Світлана винна їй ще c гривень. Проте Аліса винна Ромчику d гривень.
# Якщо всі віддадуть борги, то скільки гривень буде в Аліси?

a = int(input())
b = int(input())
c = int(input())
d = int(input())
ans = a+b+c-d
print(ans)