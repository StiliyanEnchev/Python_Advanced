def math_operations(*nums, **operations):
    keys = list(operations.keys())

    for i in range(len(nums)):
        key = keys[i % 4]

        if key == 'a':
            operations[key] += nums[i]
        elif key == 's':
            operations[key] -= nums[i]
        elif key == 'd':
            if nums[i] != 0:
                operations[key] /= nums[i]
        elif key == 'm':
            operations[key] *= nums[i]

    operations = sorted(operations.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f'{k}: {v:.1f}' for k, v in operations)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))