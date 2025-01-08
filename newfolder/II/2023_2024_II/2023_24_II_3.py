# C (240) Перевірте календар!
# Всеукраїнська олімпіада з інформатики ІІ етап 2023-2024 н.р.
# https://uoi.eolymp.space/uk/problems/240
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2023.pdf
# https://oi.in.ua/wp-content/uploads/2023/12/gstdnnklefqyulnnsumu.pdf розбір
# 100%

d1, m1 = map(int,input().split())
d2, m2 = map(int,input().split())
if ((d1+13)-30==d2 and ((m2-m1==1)or(m1-m2==11)))or (d1+13==d2 and m1==m2):
    print ("Same birthday!")
else:
    print ("Not the same")