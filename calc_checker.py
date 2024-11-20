# Welcome message to the maths quiz
print("Hello and welcome to the Calculation checker")

def calc_checker(num1, num2, selected_arithmetic):
 # Calculate the result based on the chosen operation
    if selected_arithmetic == "+":
        answer = num1 + num2        
        print(f"{num1} + {num2} = {answer}")
    elif selected_arithmetic == "-":
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
    elif selected_arithmetic == "*":
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
    elif selected_arithmetic == "/":
        if 2 != 0:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
        else:
            print("You can't divide by 0")
    else:
       ("Symbol not recognized, please try again")

# Introduce iteration to the program
def continue_loop():
    while True:
 # Ask the user to input 2 separate numbers for the sum
        num1 = int(input("Enter your first desired number: "))
        num2 = int(input("Enter your second desired number: "))

        # Ask the user to select the sum
        selected_arithmetic = input("Which sum do you want to use (+, -, *, /): ")

        # Call the calculator function
        calc_checker(num1, num2, selected_arithmetic)

        # Prompt for continuation
        more_questions = input("Do you want to answer more questions? (Y/N): ").upper()
        if more_questions != "Y":
            print("Leaving the calculator, goodbye")
            break

# Start the program
continue_loop()