#Task 1: if

#print("Enter name:")
#name = input()
#if name == "Harry":
#    print("Are you a prince?")

#print("Enter age:")
#age = int(input())
#if age > 25:
 #   print("Wow that is old!")


# Task 2: if-else

#print("Enter birth month (e.g. September):")
#month = input()
#if month == "June":
 #   print("That is my favourite month")
#else:
 #   print("My birth month is June")

#print("Guess a number between 1 and 10:")
#number = int(input())
#if number == 7:
#    print("You got it!")
#else:
#    print("Incorrect")


# Task 3: if-elif-else

#print("Guess a number between 1 and 10:")
#number = int(input())
#if number == 7:
#    print("You got it!")
#elif number < 7:
#    print("Higher")
#else:
#    print("Lower")


print("Enter a number:")
odd_even = int(input())
odd_even = odd_even % 2
if odd_even == 1:
    print("Your number is odd")
elif odd_even == 0:
    print("Your number is even")