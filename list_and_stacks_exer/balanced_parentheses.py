from collections import deque

parentheses = deque(input())
opening = ['[', '{', '(']
closing = [']', '}', ')']

while parentheses:

    if len(parentheses) == 1:
        break

    first, second = parentheses.popleft(), parentheses.pop()

    if first not in opening or second not in closing:
        print("NO")
        break
        
    for index in range(len(opening)):
        if first == opening[index] and second == opening[index]:


