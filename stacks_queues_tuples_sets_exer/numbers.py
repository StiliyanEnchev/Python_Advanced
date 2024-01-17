first_set = set(input().split())
second_set = set(input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + ' ' + second_command

    if command == 'Add First':
        [first_set.add(el) for el in data]
    elif command == 'Add Second':
        [second_set.add(el) for el in data]
    elif command == 'Remove First':
        [first_set.discard(el) for el in data]
    elif command == 'Remove Second':
        [second_set.discard(el) for el in data]
    elif command == 'Check Subset':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')