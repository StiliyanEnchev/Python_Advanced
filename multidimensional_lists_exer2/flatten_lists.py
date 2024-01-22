numbers = [string.split() for string in input().split('|')]
print(*[' '.join(sublist) for sublist in numbers[::-1] if sublist])