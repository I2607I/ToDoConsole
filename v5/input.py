import argparse
import datetime
import db
import main
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
    main.show(DATE)
    while(1):
        a = input(">>> ")
        if a == 'next day':
            DATE += datetime.timedelta(days=1)
            main.show(DATE)
        elif a == 'next' or a == 'next week':
            DATE += datetime.timedelta(days=7)
            main.show(DATE)
        elif a == 'next month':
            DATE += datetime.timedelta(days=30)
            main.show(DATE)
        elif a == 'prev day':
            DATE -= datetime.timedelta(days=1)
            main.show(DATE)
        elif a == 'prev' or a == 'prev week':
            DATE -= datetime.timedelta(days=7)
            main.show(DATE)
        elif a == 'prev month':
            DATE -= datetime.timedelta(days=30)
            main.show(DATE)
        elif a == 'exit':
            break
        else:
            try:
                d = datetime.datetime.strptime(a, "%d.%m.%Y").date()
                DATE = d
                main.show(DATE)
            except:
                print("You're so stupid")
    
# if args.red:
#     print("table with date")
# else:
#     print("usual table")