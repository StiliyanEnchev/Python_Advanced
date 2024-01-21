from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshales = 0

while chocolates and cups_of_milk:

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
    current_choc, current_milk = chocolates.pop(), cups_of_milk.popleft()

    if current_choc == current_milk:
        milkshales += 1
        if milkshales == 5:
            print('Great! You made all the chocolate milkshakes needed!')
            break
    else:
        cups_of_milk.append(current_milk)
        chocolates.append(current_choc - 5)

if milkshales < 5:
    print("Not enough milkshakes.")

if chocolates:
    print(f'Chocolate: {", ".join([str(number) for number in chocolates])}')
else:
    print("Chocolate: empty")

if milkshales:
    print(f'Milk: {", ".join([str(number) for number in cups_of_milk])}')
else:
    print("Milk: empty")

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55