import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-d", "--date", action="store_true",
                    help="output table with date")
group.add_argument("-r", "--red", type=str,
                    help="output table with date")
group.add_argument("-n", "--new", action="store_true", help="ee")
args = parser.parse_args()
if args.red:
    print("table with date")
else:
    print("usual table")
print(args.new)