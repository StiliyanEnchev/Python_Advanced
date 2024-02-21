def factorial_rec(number):
    if number == 0:
        return 1

    return number * factorial_rec(number - 1)


number = int(input())
print(factorial_rec(number))