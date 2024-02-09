def print_triangle(number):
    print_top(number)
    print_down(number)


def print_top(number):
    for row in range(1, number+1):
        for num in range(1, row+1):
            print(num, end=' ')

        print()


def print_down(number):
    for row in range(number, 0, -1):
        for num in range(1, row):
            print(num, end=' ')

        print()
