# Create a program that is able to work out what the bill would be
# per person with a tip percentage involved
print('---Welcome to Split My Bill---')

print('What is the total bill?')
try:
    bill_total = float(input())
except ValueError:
    print("It must be a value!")
    bill_total = float(input())
    
print('How many people are sharing?')
try:
    people = int(input())
except ValueError:
    print("You must enter a number.")
    people = int(input())
print('What percentage tip would you like to leave?')
try:
    tip_percentage = int(input())
except ValueError:
    print("It needs to be a number")
    tip_percentage = int(input())

percentage_decimal = tip_percentage / 100

#grand_total = (bill_total * percentage_decimal / 100) + (bill_total / people)
tip_total = round((bill_total * percentage_decimal), 2)
bill_total = round((bill_total), 2) + tip_total
cost_per_person = round((bill_total / people), 2)

print(f'Total bill including tip is £{bill_total:.2f}')
print(f'Total cost per person is £{cost_per_person:.2f}')
#print(grand_total)