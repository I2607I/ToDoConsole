import argparse
import datetime
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
        'date',
        type=lambda s: datetime.datetime.strptime(s, '%d.%m.%Y'),
)
    args = console_parser.parse_args()
elif rest:
    parser.error("unexpected arguments: " + str(rest))
print(args.__dict__)
print(args.new)

# print(args.date)
if args.red:
    print("table with date")
else:
    print("usual table")