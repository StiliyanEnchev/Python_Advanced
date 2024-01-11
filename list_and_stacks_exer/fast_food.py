from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if order <= food_quantity:
        food_quantity -= order
        orders.popleft()
    else:
        print(f'Orders left:', *orders)
        break

else:
    print("Orders complete")