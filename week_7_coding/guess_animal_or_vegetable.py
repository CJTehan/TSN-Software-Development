# Modify the guessing game to make it so the user can choose an animal or vegetable
print("Hello I am going to guess ")
print("Please select whether you want to choose an animal or vegetable")
animal_or_vegetable = input().lower()

# Use a nested IF statement to combine the 2 sets of code
if animal_or_vegetable == "animal":
    print("Pick either Ostrich, Lion, Whale or Fish")
    print("I will now guess the animal")
    input()
    print("Does the animal live in the water? Y/N")
    answer = input().lower()
    if answer == "n":
        print("Does the animal have wings? Y/N")
        answer = input().lower()
        if answer == "y":
            print("It must be an Ostrich!")
        elif answer == "n":
            print("It must be a Lion!")
    else:
        if answer == "y":
            print("Is the animal a mammal? Y/N")
            answer = input().lower()
            if answer == "y":
                print("It must be a Whale!")
            else:
                print("It must be a fish!")

# Using else to seperate the sets of code so a choice is made between the two
else:
    print("Pick a vegetable out of Peas, Broccoli, Carrots or Sweetcorn")
    print("I'm going to attempt to guess the vegetable you're thinking of")


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