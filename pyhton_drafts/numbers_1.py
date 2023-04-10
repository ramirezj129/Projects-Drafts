def main():
    x = getint("What is x: ")
    print(f"x is {x}")


def getint(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number!")
            pass


main()
