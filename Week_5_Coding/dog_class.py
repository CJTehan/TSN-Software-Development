# Define a class named 'Dog’ 
class Dog:
    # Initialize the class with attributes 'name', 'breed', and 'age’
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


    # Create a method named 'bark' that prints "Woof!"
    def bark(self):
        print("Woof!") 
    # Create a method named 'fetch' that takes an argument 'item’
    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!") # and prints a message
    # Create a method named 'age_up' that increments the 'age' attribute by 1
    def age_up(self):
        self.age += 1

# Create two instances (objects) of the 'Dog' class with different names, breeds, and ages 
dog1 = Dog("Ronny", "Labrador", 3)
dog2 = Dog("Churchill", "Chihuahua", 5)
# Call the 'bark' method on one of the dog objects
dog1.bark()
# Call the 'fetch' method on the other dog object, passing an item as an argument
dog2.fetch("ball")
# Call the 'age_up' method on one of the dog objects
dog1.age_up()
# Print a message displaying the updated age of that dog
print(f"{dog1.name} is now {dog1.age} years old")