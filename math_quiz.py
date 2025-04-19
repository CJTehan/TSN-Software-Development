# Welcome message to the maths quiz
print("Hello and welcome to the Calculation checker")

def calc_checker():
    # Ask the user to input 2 seperate numbers for the sum
    num1 = int(input("Enter your first desired number: "))
    num2 = int(input("Enter your second desired number: "))
    
    # Ask the user to select the sum
    selected_arithmetic = input("Which operand do you want to use (+, -, *, /): ")
    
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
        if num2 != 0:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
        else:
            print("You can't divide by 0")
    else:
        print("No arithmetic matching that symbol")
    
    # Introduce iteration to the program
    while True:
        continue_calc = input("Do you wish to continue (Y/N)").upper()
        if continue_calc == "Y":
            print("Let's continue then")
            return calc_checker()
        else:
            print("Exiting the program")
            break

print("Leaving the calculator, goodbye")
calc_checker()