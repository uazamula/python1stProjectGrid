from tkinter import *;
from random import *;
from time import *

root = Tk()
root.geometry('400x600')
root.option_add('*Font', 'Arial 28')
N = 5
i = 0
counttime = 0
start = None
x1, x2, answers = 0, 0, [0, 0]
active_btn = False
counter = Label(text='Лічильник: 0')
counter.pack(pady=10)
question = Label(text='питання')
question.pack(pady=30)
button1 = Button(text='відповідь1')
button1.pack()
button2 = Button(text='відповідь2')
button2.pack()
btn_start = Button(text='Press me')
btn_start.pack(pady=20)


def key_num(event, btn, btn_num):
    global x1, x2, answers, active_btn, counttime
    if active_btn:
        if x1 * x2 == answers[btn_num]:
            btn['text'] = ':)'
        else:
            button1['text'] = ':('
            counttime += 3  # penalty
        counttime += time() - start

    print(counttime)
    active_btn = False


root.bind('1', lambda event: key_num(event, btn=button1, btn_num=0))
root.bind('2', lambda event: key_num(event, btn=button2, btn_num=1))


def values(event):
    global x1, x2, answers, active_btn, start, i
    if not active_btn:
        i += 1
    active_btn = True
    start = time()
    x1, x2 = randint(2, 9), randint(3, 9)
    answers = [x1 * x2, x1 * x2 + randint(1, 4) * choice([-1, 1])]
    shuffle(answers)
    question['text'] = f'{x1}*{x2}=?'
    button1['text'] = f'{answers[0]}'
    button2['text'] = f'{answers[1]}'
    counter['text'] = f'Лічильник: {i}'


btn_start.bind('<1>', values)
# root.bind('<Activate>', values)
root.mainloop()