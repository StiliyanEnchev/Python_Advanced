numbers = input().split()
result = ""
for _ in range(len(numbers)):
  result += numbers.pop() + ' '

print(result)