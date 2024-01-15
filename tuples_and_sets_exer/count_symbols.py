text = input()
dictionary = {}

for index in range(len(text)):
    symbol = text[index]
    if symbol not in dictionary:
        dictionary[symbol] = 0
    dictionary[symbol] += 1

for symb, number in sorted(dictionary.items()):
    print(f"{symb}: {number} time/s")