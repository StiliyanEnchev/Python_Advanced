first_set = set()
second_set = set()

first_num, second_num = input().split()
for num in range(int(first_num)):
    first_set.add((input()))
for num in range(int(second_num)):
    second_set.add((input()))

repeated_numbers = first_set.intersection(second_set)
for num in repeated_numbers:
    print(num)