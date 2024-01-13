codes = set()

for guest in range(int(input())):
    codes.add(input())

code = input()
while code != 'END':
    if code in codes:
        codes.remove(code)

    code = input()

print(len(codes))

for code in sorted(codes):
    print(code)