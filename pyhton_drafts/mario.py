def main():
    size = int(input("enter the height: "))
    print_square(size)


def print_square(n):
    for i in range(n):
        print("#" * (i + 1))


main()
