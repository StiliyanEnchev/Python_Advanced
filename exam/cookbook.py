def cookbook(*receipes):

    all_receipes_collected_by_cuisine = {}

    for receipe in receipes:
        receipe_name, cuisine, ingredients = receipe[0], receipe[1], receipe[2]

        if cuisine not in all_receipes_collected_by_cuisine:
            all_receipes_collected_by_cuisine[cuisine] = []
        all_receipes_collected_by_cuisine[cuisine].append([receipe_name, ingredients])

    sorted_receipes = sorted(all_receipes_collected_by_cuisine.items(), key=lambda x: (-len(x[-1]), x[0]))
    result = ''

    for receipe in sorted_receipes:
        result += f'{receipe[0]} cuisine contains {len(receipe[1])} recipes:\n'

        sorted_by_names = sorted(receipe[1])

        for receipt in sorted_by_names:
            result += f'  * {receipt[0]} -> Ingredients: {", ".join(str(x) for x in receipt[1])}\n'

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))