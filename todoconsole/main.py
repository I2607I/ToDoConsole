import os
import datetime
import db
import main_table

TITLE = '\033[1;4m'
BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE1 = '\033[34m'     # голубой
VIOLET = '\033[35m'
BLUE2 = '\033[36m'     # синий
END = '\033[0m'

clear = lambda: os.system('clear')

def instrucrion():
    clear()

    print(f'{TITLE}This console to-do list shows your plans in the calendar{END}')

    print(f'{BOLD}list of commands:{END}')

    print(f'{BOLD}* {END}{YELLOW}dd.mm.yyyy{END}')
    print(f'  shows a to-do list of 7 days starting from dd.mm.yyyy, where dd - day, mm - month, yyyy - year')

    print(f'{BOLD}* {END}{YELLOW}help{END} or {YELLOW}instruction{END}')
    print(f'  shows this page')

    print(f'{BOLD}* {END}{YELLOW}exit{END}')
    print(f'  terminates the programm or cancels the entry of a new category or a new note')

    print(f'{BOLD}* {END}{YELLOW}now{END} or {YELLOW}today{END}')
    print(f'  shows a to-do list of 7 days starting from today')

    print(f'{BOLD}* {END}{YELLOW}next day{END} or {YELLOW}nd{END}')
    print(f"  shows a to-do list of 7 days with a day's shift ahead")

    print(f'{BOLD}* {END}{YELLOW}prev day{END} or {YELLOW}pd{END}')
    print(f"  shows a to-do list of 7 days with a day's shift back")

    print(f'{BOLD}* {END}{YELLOW}next week{END} or {YELLOW}nw{END}')
    print(f"  shows a to-do list of 7 days with a 7-day shift ahead")

    print(f'{BOLD}* {END}{YELLOW}prev week{END} or {YELLOW}pw{END}')
    print(f"  shows a to-do list of 7 days with a 7-day shift back")

    print(f'{BOLD}* {END}{YELLOW}next month{END} or {YELLOW}nm{END}')
    print(f"  shows a to-do list of 7 days with a 30-day shift ahead")

    print(f'{BOLD}* {END}{YELLOW}prev month{END} or {YELLOW}pm{END}')
    print(f"  shows a to-do list of 7 days with a 30-day shift back")

    print(f'{BOLD}* {END}{YELLOW}category{END}')
    print(f"  You can select a category to display")

    print(f'{BOLD}* {END}{YELLOW}create category{END}')
    print(f"  You can create new category for notes (you cannot create a category all or exit)")

    print(f'{BOLD}* {END}{YELLOW}create note{END}')
    print(f"  You can create a new note by entering the category of the note, the date of the note and the text of the note")


def create_note():
    clear()
    print(f'{BOLD}CREATE NEW NOTE{END}')
    list_category = db.get_category()
    flag_next = True
    while(1):
        category = input('Input category:\n> ')
        if category == 'exit':
            flag_next = False
            break
        elif category not in list_category:
            print('There is no such category, try again')
        else:
            break
    if flag_next:
        while(1):
            date = input('Input date:\n> ')
            if date == 'exit':
                flag_next = False
                break
            else:
                try:
                    date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
                    break
                except:
                    print('Error in date, try again')
    if flag_next:
        while(1):
            note = input('Input note:\n> ')
            if note == 'exit':
                flag_next = False
                break
            elif len(note) >= 38:
                print('too long note, try again')
            else:
                break
    if flag_next:
        db.new(note, date, category)
        print('Success!')

    


DATE = datetime.date.today()
CATEGORY = 'all'
instrucrion()
while(1):
    a = input(">>> ")
    if a == 'category':
        clear()
        print('Category:')
        list_category = db.get_category()
        list_category.append('all')
        for item in list_category:
            print('*', f'{YELLOW}{item}{END}')
        while(1):
            CATEGORY = input('Input category:\n> ')
            if CATEGORY == 'exit':
                CATEGORY = 'all'
                break
            elif CATEGORY not in list_category:
                print('There is no such category, try again')
            else:
                break
    elif a == 'create category':
        clear()
        input_category = input("Input category name:\n> ")
        if input_category == 'all' or input_category == 'exit':
            print("You cannot use a keyword for the category name")
        elif db.create_category(input_category) == db.Error:
            print("This category already exist")
        else:
            print(f"Good! Category {BLUE1}{input_category}{END} created")
    elif a == 'create note':
        create_note()
    elif a == 'today' or a == 'now':
        DATE = datetime.date.today()
        main_table.show(DATE, CATEGORY)
    elif a == 'next day' or a == 'nd':
        DATE += datetime.timedelta(days=1)
        main_table.show(DATE, CATEGORY)
    elif a == 'next' or a == 'next week' or a == 'nw':
        DATE += datetime.timedelta(days=7)
        main_table.show(DATE, CATEGORY)
    elif a == 'next month' or a == 'nm':
        DATE += datetime.timedelta(days=30)
        main_table.show(DATE, CATEGORY)
    elif a == 'prev day' or a == 'pd':
        DATE -= datetime.timedelta(days=1)
        main_table.show(DATE, CATEGORY)
    elif a == 'prev' or a == 'prev week' or a == 'pw':
        DATE -= datetime.timedelta(days=7)
        main_table.show(DATE, CATEGORY)
    elif a == 'prev month' or a == 'pm':
        DATE -= datetime.timedelta(days=30)
        main_table.show(DATE, CATEGORY)
    elif a == 'exit':
        break
    elif a == 'instruction' or a == 'help':
        instrucrion()
    else:
        try:
            d = datetime.datetime.strptime(a, "%d.%m.%Y").date()
            DATE = d
            clear()
            main_table.show(DATE, CATEGORY)
        except:
            print("You're so stupid")