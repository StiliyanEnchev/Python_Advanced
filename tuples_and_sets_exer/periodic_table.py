period_table_set = set()

for _ in range(int(input())):
    for x in input().split():
        period_table_set.add(x)

print(*period_table_set, sep='\n')