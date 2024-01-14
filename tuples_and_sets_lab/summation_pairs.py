import time


numbers = [int(x) for x in input().split()]
result = int(input())

start = time.time()
second_list = numbers.copy()

for num in range(len(numbers)):
    current_num = numbers.pop()
    second_list.pop()
    for index in range(len(second_list)):
        second_num = second_list[index]

        if current_num + second_num == result:
            print(f"{current_num} + {second_num} = {result}")

end = time.time()
print(f'{end-start}')