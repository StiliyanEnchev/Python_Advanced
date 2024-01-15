unique_names = set()

for _ in range(int(input())):
    unique_names.add(input())

print(f"{*unique_names}")