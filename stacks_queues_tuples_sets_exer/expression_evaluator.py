from collections import deque
from math import floor

expression = deque(input().split())

while len(expression) > 1:
    index = 0

    for char in expression:

        if char in '-+*/':
            for numbers in range(index - 1):
                num1, num2 = int(expression.popleft()), int(expression.popleft())

                if char == '-':
                    result = num1 - num2
                elif char == '+':
                    result = num1 + num2
                elif char == '*':
                    result = num1 * num2
                elif char == '/':
                    result = num1 / num2

        else:
            index += 1
