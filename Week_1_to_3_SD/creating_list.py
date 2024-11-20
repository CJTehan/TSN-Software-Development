''' A Python list is a variable with many different values
The data is stored sequentially in list "elements" that
are index numbered starting at zero.
You use square brackets for it.'''

# Start a new Python script by initializing 3 elements
month = ['January', 'February', 'March']

# Next add statements to individually display the value
# contained in each list element
print('First Month:', month[0])
print('Second Month:', month[1])
print('Third month:', month[2])

# Add a statement to create a multidimensional 
# list of two elements
coords = [[1, 2, 3], [4, 5, 6]]

# Now add statements to display the values contained in two
# specific inner list elements
print('\nTop Left 0, 0:', coords[0][0])
print('Bottom Right 1, 2:', coords[1][2])
