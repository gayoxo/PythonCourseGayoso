from argparse import ArgumentParser

parser = ArgumentParser(prog="hello")
parser.add_argument('-id','--user_id',type=int)

args = parser.parse_args()

# print(args.user_id)

from day_17 import read_data

print(read_data(user_id=args.user_id))