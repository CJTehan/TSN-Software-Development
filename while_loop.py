#even_counter = 0
#odd_counter = 0
#counter = even_counter + odd_counter
#while counter >= 5:
    #number = input("Select a number: ")
    #user_number = int(number)
   # if number % 2 == 0:
       # print("That's an even number!")
      #  even_counter += 1
     #   counter += 1
    #else:
   #     print("That's an odd number!")
  #      odd_counter += 1
 #       counter += 1
#print(f"You've typed in {even_counter} even numbers and {odd_counter} odd numbers and you get {counter}")


# Initialise a counter variable to keep track of loop iterations
count = 0
# Start a while loop that runs 5 times
while count < 5:
    user_input = input('Enter a number: ')  # Prompt the user to enter a number
    number = int(user_input)    # Convert the user input (a string) to an integer
    
    # Check if the number is even or odd & print which it is
    if number % 2 == 0:
        print(f'The number {number} is even.') 
    else:
        print(f'The number {number} is odd.')

    # Increment the counter after each iteration
    count += 1