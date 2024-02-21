def rec_drawing(n):
    if n == 0:
        return

    print('*' * n)
    rec_drawing(n - 1)
    print('#' * n)


n = int(input())
rec_drawing(n)