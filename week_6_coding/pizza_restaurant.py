print("Welcome to pizza planet")

total_cost = 0.00
voucher_code = "FunFriday"

print("Would you like thin or thick crust?")
crust = input().upper
print("Next what size would you prefer 8, 10, 12, 14 or 18 Inch?")
size = int(input())
print("Do you want cheese? (Y/N)")
cheese = input()
print("What type of pizza would you like?")
print("The choices are:\n Margarita, Vegetable, Vegan, Hawaiian or Meat Feast")
type_of_pizza = input().lower()
print("If you have a voucher code please enter it now: ")
voucher = input()

if crust == "thick":
    total_cost = total_cost + 8.00
else:
    total_cost = total_cost + 10.00
if size > 10:
    total_cost = total_cost + 2.00
if cheese == "No":
    total_cost = total_cost - 0.50
if type_of_pizza == "vegan" or "vegetarian":
    total_cost = total_cost + 1.00
elif type_of_pizza == "hawaiian" or "meat feast":
    total_cost = total_cost + 2.00
else:
    total_cost = total_cost + 0.00


if voucher == voucher_code and size == 18:
    total_cost = total_cost - 2.00
else:
    input("Press enter to skip")
   
print(f"The order we have is a {size} inch {type_of_pizza} with a {crust} crust with {cheese} cheese")
print(f"The total cost for the order is: {total_cost:.2f}")


print("Thank you for your order")
