print('---Welcome to Split My Bill---')
# Add a function to a program to check if a value is an integer
def check_integer():
    not_valid = True
    while not_valid:
        try:
            print("Enter the number of people you're with: ")
            people = int(input())
            not_valid = False
        except ValueError:
            print("You must enter the NUMBER of people")
            people = int(input())
            return people
people = check_integer()
print('What is the total bill?')
bill_total = float(input())
print('How many people are sharing?')
people = int(input())
print('What percentage tip would you like to leave?')
tip_percentage = int(input())
percentage_decimal = tip_percentage / 100

tip_total = bill_total * percentage_decimal
bill_total = bill_total + tip_total
cost_per_person = bill_total / people

print(f'Total bill including tip is £{bill_total:.2f}')
print(f'Total cost per person is £{cost_per_person:.2f}')