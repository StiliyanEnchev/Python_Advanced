from collections import deque

parentheses = deque(input())

while parentheses:
    first, second = parentheses.popleft(), parentheses.pop()
    if first == '[' and second != ']':
        print("NO")
        break
    elif first == '{' and second != '}':
        print("NO")
        break
    elif first == '(' and second != ')':
        print("NO")
        break
else:
    print('YES')