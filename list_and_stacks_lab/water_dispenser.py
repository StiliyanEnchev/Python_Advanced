from collections import deque

water = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        requested_water = int(data[0])
        person = people.popleft()

        if water >= requested_water:
            water -= requested_water
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    elif len(data) == 2:
        _, liters = data
        water += int(liters)

    command = input()

print(f"{water} liters left")