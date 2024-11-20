# Start initializing two variables with integer value
a = 2
b = 4

# Display the result of adding the variable values
print('Addition:\t', a, '+', b, '=', a + b)

# Now display the result of subtracting the variable values
print('Subtraction:\t', a, '-', b, '=', a - b)

# Display the result of multiplying the variable values
print('Multiplication:\t', a, '*', b, '=', a * b)

# Display the result of dividing the variable values both with and without
# the floating-point value
print('Float_Division:\t', a, '/', b, '=', a / b)
print('Floor_Division:\t', a, '//', b, '=', a // b)
print(f'Dividing (integer):\t {a} / {b} = remainder {a / b}')
print(f'Dividing (integer):\t {a} // {b} = remainder {a // b}')


# Next, display the remainder after dividing the values
print('Remainder:\t', a, '%', b, '=', a % b)

# Finally, display the result of raising the first operand
# to the power of the second operand
print('Raising:\t', a, '**', b, '=', a ** b)