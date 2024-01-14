numbers = [int(x) for x in input().split()]
result = int(input())

for num in range(len(numbers)):
    current_num = numbers.pop()
    for index in range(len(numbers)):
        if current_num + numbers[index] == result:
            print(f"{current_num} + {numbers[index]} = {result}")
