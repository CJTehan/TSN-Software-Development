# Print welcome message 
print('Welcome to Shopease, what would you like to add to your wishlist?')

wish_list = []

while True:
    item_name = input("Enter your item, or type quit to exit: ")
    if item_name.lower() == "quit":
        print("Exiting the program")
        break

    while True:
        try:
            item_price = float(input(f"Enter the item price for {item_name}: "))
            if item_price <= 0:
                raise ValueError("Price must be a positive number")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            item_quantity = int(input(f'Enter quantity of {item_name}: '))
            if item_quantity <= 0:
                raise ValueError("Quantity must be a positive number")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            product_id = input(f'Enter product ID of {item_name} (6 digits): ')
            # Check if the product ID is numeric and has exactly 6 digits
            if not product_id.isdigit() or len(product_id) != 6:
                raise ValueError('Product ID must be exactly 6 digits long and numeric')
            break
        except ValueError as e:
            print(e)

    item = {"name": item_name, "price": item_price, "quantity": item_quantity, "product_ID": product_id}
    wish_list.append(item)

    print("\nWish List:")

total_cost = 0

for item in wish_list:
    print(f'Item: {item["name"]}, Price: £{item["price"]:.2f}, Quantity: {item["quantity"]}, Product ID: {item["product_ID"]}' )
    total_cost += item["price"]  * item['quantity']  # this will correctly calculate cost

print(f"\nTotal cost: £{total_cost:.2f}")