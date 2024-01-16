odd_set = set()
even_set = set()
sum_odd = 0
sum_even = 0


for row in range(1, int(input()) + 1):
    name = input()
    sum = 0

    for char in name:
        sum += ord(char)

    divided = int(sum / int(row))

    if divided % 2 == 0:
        even_set.add(divided)
        sum_even += divided
    else:
        odd_set.add(divided)
        sum_odd += divided

if sum_odd == sum_even:
    print(*odd_set.union(even_set), sep=', ')
elif sum_odd > sum_even:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
