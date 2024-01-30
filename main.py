command = input()

while command != 'End':

    try:
        print(int(command))

    except ValueError:
        print('It is not an integer')

    else:
        print("Everything is alright")

    finally:
        print('The End')

    command = input()

