import argparse

my_parser = argparse.ArgumentParser(fromfile_prefix_chars="@")

my_parser.add_argument("a",
                        help="first arg")

my_parser.add_argument("b",
                        help="2nd arg")

my_parser.add_argument("c",
                        help="THIRD arg")


my_parser.add_argument("-v",
                        "--verbose",
                        action="store_true",
                        help="optional arg")

#Exe parse

args = my_parser.parse_args()

print("THIS MEANS all params were provided")