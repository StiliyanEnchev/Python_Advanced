dictionary = {}

for symbol in input():
    dictionary[symbol] = dictionary.get(symbol, 0) + 1

for symb, number in sorted(dictionary.items()):
    print(f"{symb}: {number} time/s")