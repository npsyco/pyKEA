import argparse
from pickle import FALSE

p = argparse.ArgumentParser(add_help=False)
p.add_argument("--input", action="store", type=int, required=True)
p.add_argument("--id", action="store", type=int)

args = p.parse_args()

print(args.input)