# F. (6) До чого ЗНО доводить...
# Всеукраїнська олімпіада з інформатики ІІ етап 2022-2023 н.р.

# https://uoi.eolymp.space/uk/problems/6
# https://www.kievoi.ippo.kubg.edu.ua/kievoi/1-2/2022i.pdf (розбір)

# Поки Петрик ходив розважався у кіно — інші студенти активно вчились. Так, після хвилі ностальгії по старим часам, Даня з Діаною вирішили позмагатись у вирішенні двох останніх та улюблених ними задач із ЗНО з математики: стереометрії та параметра. Для обох студентів випадковим чином були згенеровані набори завдань. Таким чином Даня отримав n наборів задач по ai​ задач в кожному, а Діана отримала m наборів задач по bi​ в кожному. За умовами змагання, учасники мають послідовно розв'язувати свої набори завдань починаючи від першого.
# Усе було б чудово, якби люди не мали фізичних обмежень, тож, на жаль, кожен з учасників має фіксовану максимальну ефективність e, яка дорівнює кількості задач, яку той може зробити за одну годину. Крім того, втомлюючись люди починають думати повільніше, тому щогодини ефективність учасника зменшується рівно на 1, поки не дійде до нуля.
# Щоб компенсувати цю несправедливість життя, кожен раз як учасник повністю вирішує набір задач, то він одразу наливає собі святковий келих "хербатки" (від пол. herbata, чай) та завдяки ньому відновлює свою ефективність до максимуму, а відлік години починається спочатку. Зверніть увагу, що якщо в цей момент мало відбутись зниження ефективності, то воно не відбувається. Переможцем змагання стає учасник, що розв'язав найбільшу кількість задач.
# Петрик послухав це все і вирішив зробити ставку на переможця. Допоможіть, будь ласка, Петрику визначитись, хто стане переможцем змагання, та, який буде фінальний рахунок вирішених задач, якщо обидва учасники хочуть перемогти.

#n,m = 3, 2
#lista = [4, 8,3]
#listb = [4, 2]
#e = 5

n,m = map(int,input().split())
lista = list(map(int,input().split()))
listb = list(map(int,input().split()))
e = int(input())

def solved_tasks(e, lists):
    di_tasks = 0
    for tasks in lists:
        e_current = e
        if (1+e)*e/2>=tasks:
            di_tasks+=tasks
        else:
            while tasks > 0 and e_current > 0:
                di_tasks += min(e_current, tasks)
                tasks -= e_current
                e_current -= 1
                # print(di_tasks, e_current, tasks)
        if e_current == 0 and tasks > 0:
            break
    return di_tasks
danya_tasks = solved_tasks(e, lista)
diana_tasks = solved_tasks(e, listb)
if danya_tasks > diana_tasks:
    print('Danya')
    print(f'{danya_tasks}:{diana_tasks}')
elif danya_tasks < diana_tasks:
    print('Diana')
    print(f'{diana_tasks}:{danya_tasks}')
else:
    print('Draw')
    print(f'{diana_tasks}:{danya_tasks}')

#print(solved_tasks(e, lista))
#print(solved_tasks(e, listb))