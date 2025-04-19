# 1. Create an empty list to store the grocery items.
leave_list = "Y"

def grocery_list():
    list = []
# 2. Start an infinite loop to continuously prompt the user for input.
while leave_list == "Y":
    # 3. Inside the loop, get the item name from the user
    item = input("Enter the items you'd like on your list: ")
    # 4. Check if the user wants to stop adding items. If so, break the loop.
    if item.lower() == "quit":
        print("Are finished with your list? (Y/N): ")
        input()
        print("You have now finished your list")
        break
    else:
        item = input("Next item.")
        print(item)
# 12. After the main loop ends, print a heading for the grocery list.
print(grocery_list)
price = float(input())
print("Now enter the price for each item")
def item_value():
    price = float(input())
    # 5. Start another infinite loop to get the item price.
    while item_value >= 0:
        # 6. Inside the price loop, try to convert the user's input to a float (decimal number).
        price = float(input())
        # 7. Check if the price is positive. If not, raise a ValueError with an appropriate message.
        try: 
            price = float(input())
            print("The given value is accepted")
            if price <0:
                print("The value can only be positive")
            # 8. If the price is valid, break the price loop.
            elif price >0:
                break
            else:
                continue
        except ValueError:
            print("The number must be positive")
            price = float(input())
            # 9. If there's a ValueError, print the error message and continue the price loop.
            continue
        # 12. After the main loop ends, print a heading for the grocery list.
        print(list)
    grocery_list.join(item_value)
# 10. Create a dictionary to represent the item with its name and price.
item_dictionary = {item, price}
# 11. Add the item dictionary to the grocery list.
print(item_dictionary)
# 13. Initialize a variable to keep track of the total cost.
total_item_cost = price * item
# 14. Iterate through the grocery list.
grocery_list = [item * price for item in grocery_list]
# 15. For each item, print its name and price in a formatted way.