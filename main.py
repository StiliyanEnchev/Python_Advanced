pos_numbers = [-2, -1, 1, 2]
positions = [(x, y) for x in pos_numbers for y in pos_numbers if abs(x) != abs(y)]
print(positions)