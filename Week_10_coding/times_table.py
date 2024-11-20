# Modify the code to make a more functional times table program.
print("Welcome to the times table generator")
# Change times table so the user needs to input the value instead
times_table = input("Please enter what times table you want to use: ")
answer = 0
# Use try and except to ensure users only give whole values
try:
    print("A number must be given")
    times_table = int(input())
except ValueError:
    print("It only excepts numbers!")
    times_table = int(input())
# Create a new variable to enter the maximum value for the times table to go to
max_value = input("Enter the max value you would like it to go up to: ")
try:
    print("You can't use a string")
    max_value = int(input())
except ValueError:
    print("A number must be used")
    max_value = int(input())
print(f"Here is the {times_table} times table")
# Enter code to increase the value by 1 and add the new variable to the range
for x in range(1, max_value + 1):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")