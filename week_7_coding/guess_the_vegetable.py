# Make a guess the vegetable game that consists of 4 vegetables
print("Pick a vegetable out of Peas, Broccoli, Carrots or Sweetcorn")
print("I'm going to attempt to guess the vegetable you're thinking of")

# Using a choice of Peas, Broccoli, Carrots or Sweetcorn come up with Y/N questions to ask
print("Is the vegetable you're thinking of green? Y/N: ")
answer = input().upper()
if answer == "Y":
    print("Does the vegetable have a stem? Y/N")
    answer = input().upper()
    if answer == "Y":
        print("The vegetable you're thinking of is Broccoli!")
    else:
        print("You're thinking of Peas!")
elif answer == "N":
    print("Is the vegetable Orange? Y/N")
    answer = input().upper()
    if answer == "Y":
        print("The vegetable is a carrot!")
    else:
        print("The answer must be sweetcorn!")