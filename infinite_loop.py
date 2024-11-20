# Create an infinite loop
leave_loop = 'quit'

while leave_loop == 'quit':

# Get user input (number or ‘quit’)
# Handle potential errors when converting input to an integer
    selected_number = int(input("Enter a positive number or leave the program!\n"))
# Exit the loop if the user enters ‘quit’ (case-insensitive)
    if selected_number == 'quit':
        # Print appropriate messages based on the input
        print('this will exit the loop, please restart the loop')
        break
    # If the input is a valid number, check if it is positive
    elif selected_number < 0:
        print('The number is negative, try again')
    elif selected_number > 0:
        print ('The number is positive, well done')
    elif selected_number % 2 == 0:
        print("You've selected an even number")
    
    else:
        print(selected_number)


# Print an exit message after the loop ends
print('The loop has ended. Type a new number to restart')


