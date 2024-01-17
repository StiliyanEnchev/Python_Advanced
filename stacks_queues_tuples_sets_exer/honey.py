from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

functions = {
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: a / b if b != 0 else 0,
}

while working_bees and nectar:
    curr_bee = working_bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < curr_bee:
        working_bees.appendleft(curr_bee)
    else:
        total_honey += abs(functions[symbols.popleft()](curr_bee, curr_nectar))

print(f'Total honey made: {total_honey}')

if working_bees:
    print(f"Bees left: {', '.join(str(bees) for bees in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(nec) for nec in nectar)}")