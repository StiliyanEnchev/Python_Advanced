from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = [int(el) for el in input().split()]

items_resources = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}

crafted_items = {}

while medicaments and textiles:
    textile, medicament = textiles.popleft(), medicaments.pop()

    result = textile + medicament

    for item, resource_needed in items_resources.items():
        if result == resource_needed:
            if item not in crafted_items:
                crafted_items[item] = 0
            crafted_items[item] += 1
            break

    else:
        if result > 100:
            if 'MedKit' not in crafted_items:
                crafted_items['MedKit'] = 0
            crafted_items['MedKit'] += 1
            left_res = result - 100
            medicaments[-1] += left_res
        else:
            medicaments.append(medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

if crafted_items:
    sorted_crafted_items_by_values = dict(sorted(crafted_items.items(), key=lambda x: (-x[1], x[0])))
    for item, amount in sorted_crafted_items_by_values.items():
        print(f'{item} - {amount}')

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(med) for med in medicaments)}")

if textiles:
    print(f"Textiles left: {', '.join(str(text) for text in textiles)}")
