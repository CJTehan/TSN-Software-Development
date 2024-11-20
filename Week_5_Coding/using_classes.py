#class Critter:

  #  count = 0

  #  def __init__(self, chat):
      #  self.sound = chat
      #  Critter.count += 1

   # def talk(self):
   #     return self.sound

   
# Define a class called 'Cat' which acts as a blueprint for creating cat objects

class Cat:
    # Constructor method, called when a new cat object is created
    def __init__(self, name, colour): # 'self' refers to the specific instance of the Cat being created
        self.name = name # Assign the given 'name' to the cat's 'name'attribute
        self.colour = colour  # Assign the given 'color' to the cat's 'color' attribute
    # Method representing a cat's behavior (meowing)   
    def meow(self):
        print('Meow!') 

# Create an instance (object) of the Cat class  
my_cat = Cat('Whiskers', 'Ginger') # Pass the cat's name and color Ke constructor 

#Access the object's attributes using dot notation  
print(my_cat.name) #Output: Whiskers  
print(my_cat.colour) #Output: Ginger  
#Call the object's method  
my_cat.meow() #Output: Meow!  ABC