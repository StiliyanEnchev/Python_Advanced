import time

numbers = [int(x) for x in input().split()]
result = int(input())
start = time.time()
numbers_to_remove = []

for num in range(len(numbers)):
    current_num = numbers.pop()
    second_list = numbers.copy()

    for index in range(len(second_list)):
        second_num = second_list[index]
        found = False
        if current_num + second_num == result:
            print(f"{current_num} + {second_num} = {result}")
            break



end = time.time()
print(f'{end-start}')
print(numbers)