print("Welcome to HealthLite, your companion for keeping you fit!")
# Use a list to store meal entries, where each entry is a dictionary
# containing meal name, calories and timestamps.
meal_plan = []

meal = {}

def log_meal(meal_name, calories): # log_meal(meal_name, calories): Adds a new meal entry to the list.
    counter = 0
    while counter < 4:
    # Use input() to get user input for meal name and calories
        meal_name = input("What did you eat?\n")
    # Use print() to display logged meals.
        calories = int(input("How many calories?\n"))
    
        meal[meal_name] = calories
        counter += 1
        
    meal_plan.append(meal)

log_meal("", 0) # view_meals(): Displays all logged meals

def view_meals():
    for i in meal_plan:
        for meal_name, calories in i.items():
            print(f"These are the logged meals, {meal_name} and the calories {calories}")

view_meals()