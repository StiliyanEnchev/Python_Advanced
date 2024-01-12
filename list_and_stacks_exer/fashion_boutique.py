clothes = [int(x) for x in input().split()]
space = int(input())

racks_count = 1
current_rack_space = space

while clothes:
    cloth = clothes.pop()

    if cloth <= current_rack_space:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = space - cloth

print(racks_count)