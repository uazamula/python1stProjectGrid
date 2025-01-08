# B (212) Перші книжки
# Всеукраїнська юніорська та дівоча олімпіада з інформатики 2022-23 ІII тур
# https://uoi.eolymp.space/uk/problems/212
# https://oi.in.ua/wp-content/uploads/2023/03/A2P6Tjv4fBhs38xmDp1uJYCth3RiKtqT.pdf - умова
# https://archive.uoi.ua/static/ujgoi-23-v3-tutorials.pdf - розбір
# 100%

a = list(map(int,input().split()))
a.sort()
print (a[4]+a[3]+a[2]-a[1]-a[0])