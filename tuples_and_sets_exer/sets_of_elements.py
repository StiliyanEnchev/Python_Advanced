first_num, second_num = [int(x) for x in input().split()]

first_set = {input() for _ in range(first_num)}
second_set = {input() for _ in range(second_num)}

print(*first_set.intersection(second_set), sep='\n')
