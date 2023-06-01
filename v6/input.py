import argparse
import os
import datetime
import db
import main

clear = lambda: os.system('clear')

parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-r", "--red", type=str,
                    help="output table with date")
group.add_argument("-n", "--new", action="store_true", help="ee")
# args = parser.parse_args()

args, rest = parser.parse_known_args()
if args.new:
    console_parser = argparse.ArgumentParser(parents=[parser], add_help=False)
    console_parser.add_argument(
            'note',
            type=str,
        )
    console_parser.add_argument(
            'date',
            type=lambda s: datetime.datetime.strptime(s, '%d.%m.%Y').date()
        )
    console_parser.add_argument(
            'type',
            nargs='?',
            type=str,
            default='No'
        )
    args = console_parser.parse_args()
elif rest:
    parser.error("unexpected arguments: " + str(rest))
print(args.__dict__)
print(args.new)
if args.new:
    print('создание новой записи')
    db.new(args.__dict__)
if not args.new and not args.red:
    DATE = datetime.date.today()
    CATEGORY = 'all'
    print(DATE)
    main.show(DATE, CATEGORY)
    while(1):
        a = input(">>> ")
        if a == 'category':
            clear()
            print('Category:')
            list_category = db.get_category()
            # print(list_category)
            for item in list_category:
                print('* ', item)
            while(1):
                CATEGORY = input('Input category:\n')
                if CATEGORY not in list_category and CATEGORY != 'all':
                    print('There is no such category, try again')
                else:
                    break
        elif a == 'today' or a == 'now':
            DATE = datetime.date.today()
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'next day' or a == 'nd':
            DATE += datetime.timedelta(days=1)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'next' or a == 'next week' or a == 'nw':
            DATE += datetime.timedelta(days=7)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'next month' or a == 'nm':
            DATE += datetime.timedelta(days=30)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'prev day' or a == 'pd':
            DATE -= datetime.timedelta(days=1)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'prev' or a == 'prev week' or a == 'pw':
            DATE -= datetime.timedelta(days=7)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'prev month' or a == 'pm':
            DATE -= datetime.timedelta(days=30)
            clear()
            main.show(DATE, CATEGORY)
        elif a == 'exit':
            break
        else:
            try:
                d = datetime.datetime.strptime(a, "%d.%m.%Y").date()
                DATE = d
                clear()
                main.show(DATE, CATEGORY)
            except:
                print("You're so stupid")
    
# if args.red:
#     print("table with date")
# else:
#     print("usual table")