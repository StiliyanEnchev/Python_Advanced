def print_numbers(numbers):
  positive_sum = sum(num for num in numbers if num > 0)
  negative_sum = sum(num for num in numbers if num < 0)

  print(negative_sum)
  print(positive_sum)

  if positive_sum < abs(negative_sum):
    print("The negatives are stronger than the positives")
  else:
    print("The positives are stronger than the negatives")

numbers = [int(x) for x in input().split()]

print_numbers(numbers)