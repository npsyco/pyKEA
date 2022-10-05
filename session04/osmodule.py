# os_exercise.py
# Do the following task using the os module

# 1. create a folder and name the folder 'os_exercises.'                                                  
# 2. In that folder create a file. Name the file 'exercise.py'                                                                            
# 3. get input from the console and write it to the file.                                                 
# 4. repeat step 2 and 3 (name the file something else).                                                  
# 5. read the content of the files and and print it to the console.

import argparse

import os
import sys

# Create parser

my_parser = argparse.ArgumentParser(prog="I AM CHANGING",
                                #usage="%(prog)s [ble] path",
                                description="List content of dir",
                                add_help=True,
                                allow_abbrev=False,
                                epilog="ENJOY ME")
                                #prefix_chars="0")

# Add args

my_parser.add_argument("Path",
                    metavar="path",
                    type=str,
                    help="the PATH to list",)
my_parser.add_argument("-l",
                    "--long",
                    action="store_true",
                    help="enable DOOM list format")


# Exe parse_args() method

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("Path specfied does not exist")
    sys.exit()

for line in os.listdir(input_path):
    if args.long: # simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = "%10d  %s" % (size, line)
    print(line)

#print("\n".join(os.listdir(input_path)))