def accommodate_new_pets(total_capacity, weight_limit, *animals_data):

    accommodated_pets = {}
    are_all_accomodated = True

    for pet_type, pet_weight in animals_data:

        if total_capacity == 0:
            are_all_accomodated = False
            break

        if pet_weight > weight_limit:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        total_capacity -= 1

    result = ''

    if are_all_accomodated:
        result += f"All pets are accommodated! Available capacity: {total_capacity}.\n"
    else:
        result += f"You did not manage to accommodate all pets!\n"

    result += 'Accommodated pets:\n'

    if accommodated_pets:
        sorted_pets = sorted(accommodated_pets.items(), key=lambda kvp: kvp[0])

        for pet, weight in sorted_pets:
            result += f"{pet}: {weight}\n"

    return result[:-1]


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

