total_cost = 0.00
sugar_tax = 0.50
print("Sandwich or Wrap?")
bread_type = input().lower()
print("Meat, Vegetarian or Vegan?")
filling_type = input().lower()
print("Do you want any sauce?")
sauce = input().lower()
print("Would you like any salad?")
salad = input().lower()
print("Cookie, Crisps, Fruit or None")
pudding = input().lower()
print("Fizzy drink, Water, Juice or None")
drink = input().lower()
if bread_type != "sandwich":
  total_cost = 2.00
else:
  total_cost = 3.00
if filling_type == "vegetarian" or filling_type == "vegan":
  total_cost = total_cost + 1.00
else:
  total_cost = total_cost + 1.50
if sauce == "Yes":
  total_cost = total_cost + 0.75
if salad == "Yes":
  total_cost = total_cost + 0.25
if salad == "Yes" and sauce == "Yes":
  total_cost = total_cost + 1.00
if pudding == "cookie" and drink == "fizzy drink":
  total_cost = total_cost + sugar_tax
if pudding == "none" and drink == "none":
  total_cost = total_cost - 0.50
print(f"Your total cost is: £{total_cost}")