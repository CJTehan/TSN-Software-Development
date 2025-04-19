continue_calculator = 'Y'

# Put it into a while loop to carry on till the person is finished
while continue_calculator == 'Y':
    # Get the student’s score as input
    students_score = int(input("Enter the score for the student: "))
    # Use if-elif-else to determine the grade 
    if students_score >90 <=100: # 90 – 100 is A # Excellent
        mark = "A, Excellent work - Already showing a high standard"
    elif students_score >= 80: # 80 – 90 is B # Good 
        mark = "B, Good - Keep at it"
    elif students_score >= 70: # 70 – 80 is C # Satisfactory
        mark = "C, Satisfactory - Can do better"
    elif students_score >= 60: # 60 – 70 is D # Needs improvement
        mark = "D, Needs improvement - More work to be done"
    else: #	0 – 60 is F # Fail
        mark = "F, Fail - Need to work on it"
    # Print the calculated grade
    
    print(students_score, mark)
    continue_calculator = input("Are you finished with the calculator? (Y/N): ")

print("You are now finished with the session, Goodbye!")