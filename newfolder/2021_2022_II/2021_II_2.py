# Андрій вирішив випити кави в одній Київській кав'ярні.
# Проте він згадав, що у Києві "червона зона".
# Нагадаємо, що у "червоній зоні" у Києві лише повністю вакциновані люди
# (тобто ті, які отримали два щеплення) можуть відвідувати кав'ярні.
# Якщо ж людина неповнолітня (строго менше ніж 18 років),
# то вона може відвідати кав'ярню лише з повністю вакцинованим дорослим,
# при цьому дитина не зобов'язана бути вакцинованою.
# Андрію n років та він отримав m щеплень.
# А його повнолітній батько, Борис, отримав уже k щеплень.
# Визначте, чи зможе Андрій потрапити у кав'ярню. Можливо, разом з батьком.
# Вхідні дані
# Перший рядок містить одне ціле числа n (12≤n≤30) — вік Андрія.
# Другий рядок містить два цілі числа m та k (0≤m,k≤2) — кількість щеплень,
# які отримали Андрій та Борис відповідно.
# Вихідні дані
# Виведіть «Yes», якщо Андрій зможе потрапити у кав'ярню, або «No» — інакше.
# Ви можете виводити букви у будь-якому регістрі.

n = int(input())
m, k = map(int, input().split())
ok = True
# todo
if n<18 and k<2 or n>=18 and m<2:
 ok=False
if ok:
 print('Yes')
else:
 print('No')
