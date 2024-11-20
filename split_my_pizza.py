# create a new app called ‘Split my pizza’.
print("---Welcome to Split My Pizza, the best pizza in town---")
# Ask the customer for the number of slices they would like
print("How many slices of pizza would you like? ")

try:
    slices = int(input())
except ValueError:
    print("You can only enter a number here.")
    slices = int(input())
# Ask how many people are sharing the pizza
print("How many people are sharing their pizza?")
try:
    people = int(input())
except ValueError:
    print("You need to enter the Number of people.")
    people = int(input())
# Reveal the number of slices each are having
number_of_slices = slices // people
# Give the number of slices remaining
slices_remaining = slices % people
# work out how much each person needs to pay for their share of the pizza
cost_per_slice = 3.80
price_per_person = (cost_per_slice * slices) // people


print(f"The total number of slices each will have is {number_of_slices}")
print(f"The number of slices remaining will be {slices_remaining}")
print(f"The total cost per person will be £{price_per_person:.2f}")