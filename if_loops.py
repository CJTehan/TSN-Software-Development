# In the coding intiate a variable
#Year = 2024
# Make an if statement with a print statement using if and else
# if Year <= 2024:
 #   print('Yes!')
#else:
   # print('No!')


# Using the given code
trial = int(input('Give me the verdict '))
if trial >= 22:
    print('\nTrue')
else:
    print('False!')

# Using elif
#number = int(input('Give a number!\n'))
#if number >= 150:
 #   print('The number is High')
#elif number == 125:
 #   print('The number is low')
#else:
   # print('You\'ve not got the right number!')

# using try and except to ensure the expected ValueErrors is picked up

#try:
    #pick_a_number = int(input('Pick a number between 1 and 10.\n')) # declaring a variable
    
    #if 10 > pick_a_number >= 5: # if it's less than 10 or more than/equal to 5
      #  print('That number rounds up!')
        
    #elif 5 > pick_a_number >= 1: # otherwise, if it's less than 5 but more than 0
     #   print('That number rounds down!')
    
    #elif pick_a_number < 1 or pick_a_number >= 10: # otherwise, if it less than 1 or more than 10
     #   print('That\'s not within our range.')
        
#except ValueError: # the expected error, with some user-friendly output
 #   print('That\'s not a number.')
