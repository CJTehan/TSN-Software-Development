def find_max(numbers):
  """
  This function takes a list of numbers and returns the maximum value.
  """
  max_num = numbers[0]  # Initialize max_num with the first number
  for number in numbers:
    if number > max_num:
      max_num = number
  return max_num

# Example usage
numbers = [4, 2, 9, 7, 1]
max_value = find_max(numbers)
print(f"The maximum value is: {max_value}")