import settings as sts
import datetime
import os
import db

clear = lambda: os.system('clear')

def show(DATE, CATEGORY):
    list_date =[]
    for i in range(7):
        list_date.append(DATE + datetime.timedelta(days=i))
    list_task = []
    for i in range(7):
        list_task.append(db.get_any_notes(list_date[i], CATEGORY))
    count_task = 3
    for item in list_task:
        if len(item) > count_task:
            count_task = len(item)
    days = len(list_task)
    ROWS = days//sts.COLUMN
    if days%sts.COLUMN != 0:
        ROWS+=1
    clear()
    print(f'\033[1;35mCategory: {CATEGORY}\033[0m')
    for row in range(ROWS):
        if row == days//sts.COLUMN:
            r = days%sts.COLUMN
        else:
            r = sts.COLUMN
        for j in range(r):
            res_date = list_date[j+sts.COLUMN*row].strftime("%a %d.%m.%Y")
            print(f'\033[33m{res_date}\033[0m', end="")
            print(' '*31, end="")
        print()
        for j in range(r):
            print(sts.SYMB*40, end="")
            print(' '*5, end="")
        print()
        for i in range(count_task):
            for j in range(r):
                if i < len(list_task[j+sts.COLUMN*row]):
                    task = list_task[j+sts.COLUMN*row][i]
                else:
                    task = ""
                len_space = 40 - 2 - len(task) - 1
                print(sts.SYMB, ' ', f'\033[41m\033[32m{task}\033[0m', " "*len_space, sts.SYMB, sep="", end="")
                print(' '*5, end="")
            print()
        for j in range(r):
            print(sts.SYMB*40, end="")
            print(' '*5, end="")
        print()
        print()