continue_choice = 'Y'

# Put into a while loop till the person has finished
while continue_choice == 'Y':

# Get the students score as input
    score = int(input("Enter the student's score (0-100): "))

# Use if-elif-else to determine the grade
    if score >= 90 <= 100:
        grade = "A" 
        comment = "Excellent!"
    elif score >= 80:
        grade = "B" 
        comment = "Good Performance!"
    elif score >= 70:
        grade = "C" 
        comment = "Satisfactory"
    elif score >= 60:
        grade = "D" 
        comment = "Needs improvement"
    else:
        grade = "F" 
        comment = "Fail"

    # Print the calculated grade
    print(score , grade, comment)

    # Ask if the user wants to continue
    continue_choice = input('Calculate another Grade (Y/N): ').upper()


print("Leaving the Grade Calculator. Goodbye!")