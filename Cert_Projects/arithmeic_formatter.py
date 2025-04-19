def arithmetic_arranger(problems, show_answers=False):
    # Check the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists for each line of the output
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        # Split each problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Incorrect problem format.'

        num1, operator, num2 = parts

        # Check for valid operator
        if operator not in ['+', '-']:
            return 'Error: Operator must be '+' or '-'.'
        
        # Check if numbers are digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check the length of the numbers
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the length of the result line
        width = max(len(num1), len(num2)) + 2 # 2 for operator and space
        
def arithmetic_arranger(problems, show_answers=False):
    # Check the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists for each line of the output
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        # Split each problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Incorrect problem format.'

        num1, operator, num2 = parts

        # Check for valid operator
        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        
        # Check if numbers are digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check the length of the numbers
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the length of the result line
        width = max(len(num1), len(num2)) + 2  # 2 for operator and space
        
        # Format the numbers
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)
        
        # Calculate answer if requested
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:  # operator is '-'
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))

    # Join the rows with four spaces in between
    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(bottom_row) + '\n' + \
                        '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems
