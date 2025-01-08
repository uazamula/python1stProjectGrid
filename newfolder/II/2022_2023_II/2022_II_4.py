# D. (4) Транспортна дилема
# Всеукраїнська олімпіада з інформатики ІІ етап 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/4
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2022i.pdf (розбір)

# Петрик запізнюється на сеанс в кінотеатр, тому хоче вибрати найшвидший шлях до необхідного йому торгового центру.
# Оскільки він стоїть прямо поруч зупинок публічного транспорту, то знає, що найближчий автобус приїде через db​ хвилин, дорога на ньому займає tb​ хвилин, а дорога пішки від зупинки приїзду до торгового центру wb​ хвилин.
# Петрику також доступне метро, очікування потягу у якому займає dm​ хвилин, поїздка tm​ хвилин, а дорога пішки від станції прибуття до торгового центру wm​ хвилин.
# З врахуванням нагальності поїздки хлопець розглядає і варіант таксі, очікування якого згідно з мобільною програмою займе dt​ хвилин, а час поїздки становить tt​ хвилин.
# Підкажіть, будь ласка, Петрику, який транспорт йому краще використовувати, щоб потрапити у торговий центр як можна скоріше.
# Якщо у Петрика є кілька можливих варіантів потрапити у торговий центр як можна скоріше, то він вибере найдешевший варіант. Автобус є дешевшим за метро, а метро є дешевшим за таксі.

db = 5
tb = 6
wb = 2

dm = 6
tm = 3
wm = 5

dt = 10
tt = 3

total_tb = db + tb + wb
total_tm = dm + tm + wm
total_tt = dt + tt
s = ''


def transport():
    if total_tb <= total_tm:
        if total_tb <= total_tt:
            return 'Bus'
        else:
            return 'Taxi'
    else:
        if total_tm <= total_tt:
            return 'Metro'
        else:
            return 'Taxi'


print(transport())
