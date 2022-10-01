import sys

def main(argv):
    if argv[1] != "-it":
        print("Usage: python script.py [-it]{--rm}")
    if len(argv) == 3 and argv[2] != "--rm":
        print("Usage: py script.py [-it]{--rm}")
    elif len(argv) == 3 and argv[2] == "--rm":
        print("Bye")
        
    sys.exit()

main(sys.argv)