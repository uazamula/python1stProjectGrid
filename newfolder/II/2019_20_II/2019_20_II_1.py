# A. Шахи
# UOI 2022. II stage. Kyiv ?

# Ліміт на час виконання 1 секунда
# Ліміт використання пам'яті 256 мегабайтів
# 50 спроб відправити цю задачу
# Дано шахове поле розміром n×m клітин. n, m — парні числа. Знайдіть кількість білих клітин.
# Вхідні дані
# Перший рядок містить два цілі числа n та m (2 ≤ n, m ≤ 100). Гарантується, що обидва числа парні.
# Вихідні дані
# Виведіть одне ціле число.
# Приклади
# Нижче ви знайдете приклади вхідних даних та відповідей, які має вивести ваша програма.
# Вхідні дані №1
# 8 8
# Відповідь №1
# 32
# Вхідні дані №2
# 10 2
# Відповідь №2
# 10

n, m = map(int, input().split())
c = int(n*m/2)
# todo
print(c)