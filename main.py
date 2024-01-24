def sum_nums(a, b, *args):
    total_sum = a + b
    for el in args:
        total_sum += el
    return total_sum

print(sum_nums(1, 2, 1, 5))