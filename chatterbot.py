# Ask for user's name
print("What is your name?")
# Change all the letters of the name to lowercase
name = input().lower()
# If the name is "anakin" a specific message will be printed
if name == "harry":
    print("You're a wizard Harry!")
elif name == "legolas":
    print("We're taking the hobbits to Isengard!")
else:
    print(f"{name}, well that's an interesting name")
# print a query if hot or cold and input the answer, put it in capitals
print(f"So {name}, What is your favourite season?")
season = input().upper()
# If the answer is COLD, print "You must be freezing!"
# If the answer is HOT, print "Drink plenty of water!"
# Or else print "I can't advise you on that type of weather"
if season == "WINTER":
    print("Great choice for some lovely snow!")
elif season == "SUMMER":
    print("Always got to be able to sit and enjoy the sun by the pool!")
else:
    print("Sorry these are not seasons I find too interesting")
# Ask the user if they like the color blue and input the answer
print("Are dogs the best pets?")
best_dog = input().upper()
# If the user likes blue print "I like blue too!"
if best_dog == "YES":
    print("See, that just proves it they are amazing!")
else:
    print("That's just wrong, I'm dissappointed")

print("What is your favourite animal?")
favourite_animal = input().lower()

if favourite_animal == "dog":
    print("The really are the best aren't they!")
elif favourite_animal == "cat":
    print("Not my favourite but each to their own")
else:
    print(f"{favourite_animal} is nice but it's not the best")
# Print "Have a good day! Bye!"
print("Have a good day! Bye!")