import sys


def main():
    check_comline()
    if len(sys.argv) < 2:
        sys.exit("Too few comm lines")


if len(sys.argv) > 2:
    sys.exit("Too few comm lines")
if ".py" not in sys.argv[1]:
    sys.exit("This is not a .py file")


def check_comline():
    try:
        f = open(sys.argv[1], "r")

    except FileNotFoundError:
        exit()


if __name__ == "main":
    main()
