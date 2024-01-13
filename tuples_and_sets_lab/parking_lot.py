parking_lot = set()

for _ in range(int(input())):
    command, number = input().split(', ')
    if command == 'IN':
        parking_lot.add(number)
    elif command == 'OUT':
        parking_lot.remove(number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
        print("Parking Lot is Empty")