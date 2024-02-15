from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes != 5:

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    current_choc, current_milk = chocolates.pop(), cups_of_milk.popleft()

    if current_choc == current_milk:
        milkshakes += 1

    else:
        cups_of_milk.append(current_milk)
        chocolates.append(current_choc - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
elif milkshakes < 5:
    print("Not enough milkshakes.")

print(f'Chocolate: {(", ".join(str(number) for number in chocolates) or "empty")}')
print(f'Milk: {(", ".join(str(number) for number in cups_of_milk) or "empty")}')
