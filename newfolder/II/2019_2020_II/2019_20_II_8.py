# H (76) Квадрати
# UOI 2021-2022. II stage. Kyiv ?

# https://uoi.eolymp.space/uk/problems/76
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2021.pdf умова + розбір

# Ліміт на час виконання 2 секунди
# Ліміт використання пам'яті 256 мегабайтів
# 50 спроб відправити цю задачу
# Дано поле m×m. n клітинок з цього поля чорні, всі інші — білі. Для кожного цілого
# числа t від 0 до k
# 2
# знайдіть кількість квадратів k×k, де рівно t клітин чорні.
# Вхідні дані
# Перший рядок містить три цілі числа n, m, k (1 ≤ n ≤ 105
# , 1 ≤ m ≤ 109
# , 2 ≤ k ≤ 4).
# Кожен з наступних n рядків містить по два цілі числа xi та yi (1 ≤ xi
# , yi ≤ m) — координати чорної
# точки. Гарантується, що усі пари різні.
# Вихідні дані
# Для кожного цілого числа t від 0 до k
# 2
# виведіть відповідь.
# Оцінювання
# Рішення, які працюватимуть правильно при m ≤ 103
# , отримають принаймні 30 балів.
# Рішення, які працюватимуть правильно при k = 2, отримають принаймні 33 бали.
# Рішення, які працюватимуть правильно при k ≤ 3, отримають принаймні 66 балів.
# Приклади
# Нижче ви знайдете приклади вхідних даних та відповідей, які має вивести ваша програма.
# Вхідні дані №1
# 4 5 3
# 1 5
# 2 4
# 4 2
# 3 4
# Відповідь №1
# 1 3 3 2 0 0 0 0 0 0

# Опис ідеї
# Задача H. Квадрати. Будемо динамічно додавати точки та оновлювати відповіді. Спочатку відповіді на
# всі t рівні нулю, крім t = 0, бо точок немає. При t = 0 відповідь (n − k + 1)**2
# . Будемо також зберігати
# кількість чорних точок у кожному квадраті. Коли ми додаємо певну точку, нам потрібно знайти всі
# квадрати k × k, у яких розташована ця точка. Таких квадратів буде не більше k**2
# . Нехай кількість чорних
# точок для певного квадрата буде d. Тоді відповідь при t = d зменшиться на 1, а для t = d + 1 збільшиться
# на один. Сумарна асимптотика: O(nk**2* log(nk**2 ))