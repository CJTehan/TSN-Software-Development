print("Welcome to the times table quiz")
# Ask the user what times table they would like to test
print("Which times table would you like to test yourself with today?")
times_table = int(input("Please enter the number you would like: "))

print("What is the maximum value you want to go up to?")
max_value = int(input())
print(f"Now to test yourself with the {times_table} times table, good luck!")
# Create the for loop to take into account the users max value
for x in range(1, max_value + 1):
    answer = x * times_table
    print(f"Enter your answer for {x} times {times_table}")
    # Create the user answer input for them to select the answer
    print("What is the answer?")
    # Add try and except to the user answer
    try:
        user_answer = int(input("Answer: "))
    except ValueError:
        print("You can only enter a number")
        user_answer = int(input())
    # Create an If statement to determine if the user answer is correct or incorrect
    if user_answer == answer:
        print("Correct")
    else:
        print("Incorrect")

# Incorporate a scoring system that tells the user how many they got right
scoring = int(user_answer / max_value)
print(f"You scored {scoring} out of {max_value}")
if scoring == max_value:
    print("Well done you aced it")
else:
    print("Try again, we know you can get the highest score")
    