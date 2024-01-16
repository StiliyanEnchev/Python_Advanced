longest_inter = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(',') for el in input().split('-')]

    first_set = set(range(int(first_data[0]), (int(first_data[1]) + 1)))
    second_set = set(range(int(second_data[0]), (int(second_data[1]) + 1)))
    print(first_set, second_set)


# print(f"Longest intersection is [{longest_inter}] with length {length}")