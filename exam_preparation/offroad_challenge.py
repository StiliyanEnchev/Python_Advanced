from collections import deque


fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
needed_quantity = deque([int(x) for x in input().split()])

reached_altitudes = []
all_altitudes = len(needed_quantity)

for altitude in range(1, len(needed_quantity) + 1):
    if fuel[-1] - consumption[0] >= needed_quantity[0]:
        fuel.pop()
        consumption.popleft()
        needed_quantity.popleft()
        reached_altitudes.append(f'Altitude {altitude}')
        print(f'John has reached: Altitude {altitude}')

    else:
        print(f'John did not reach: Altitude {altitude}')

        break

if len(reached_altitudes) == 0:
    print("John failed to reach the top. \nJohn didn't reach any altitude.")

if all_altitudes > len(reached_altitudes) > 0:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join([number for number in reached_altitudes])}")

if len(reached_altitudes) == all_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")
