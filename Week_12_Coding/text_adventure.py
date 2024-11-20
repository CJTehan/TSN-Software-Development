# Start creating a text based adventure game
# Introduction
def show_intro():
    '''Displays the game's introduction'''
    print("\nWelcome to the Adventure of the Hidden Treasure!")
    print("You are an intrepid explorer seeing a legendary treasure hidden deep within an ancient temple.")
    print("Your journey will be fraught with peril, but the rewards are immeasurable.")
    print("Good luck!\n")
# Show the current location
def show_current_location(location, locations):
    print(f"\nYou are in {locations[location]["name"]}.")
    print(locations[location]["description"])
    if "items" in locations[location] and locations[location]["items"]:
        print("You see the following items:")
        for item in locations[location]["items"]:
            print(f"- {item}")

# Get the users input
def get_player_input(locations, location, items):
    '''Gets and validates player input'''
    while True:
        action = input("> ").lower()
        if action in ["go north", "go south", "go east", "go west", "take", "inventory", "quit"]:
            return action
        else:
            print("Invalid action. Try again")
    player_input = input().lower()
    if player_input == "north":
        return locations[location]["hallway"]
    if player_input == "east":
        return locations[location]["temple garden"]
    if player_input == 
    
def move_player(location, direction, locations):
    '''Moves the player to a new location if possible'''

# Adds an item to the player's inventory
def take_item(location, item, locations, inventory):
    '''Adds an item to the player's inventory if possible'''
# Shows the player's inventory
def show_inventory(inventory):
    # --- The Main Game Loop ---

def play_game():
    '''Main game loop'''
    locations = {
        "entrance":{
            "name": "The Castle Entrance",
            "description": "A grand archway leads into a dark and mysterious castle.",
            "directions":{"north": "hallway"}, {"south": "entrance"}
        }
        "hallway":{
            "name": "Castle Hallway",
            "description": "A stone hallway, dimly lit. You can see two doors, one on either side of the hallway.",
            "directions":{"north": "Grand Hall"}, {"east": "Temple Garden"}, {"west": "Banquet Hall"}, {"south": "entrance"}
        }
        "temple garden":{
            "name": "Temple Garden"
            "description": ""
        }
    }
        current_location = "entrance"
        inventory = []

        show_intro()

        while True:
            show_current_location(current_location, locations)
            action = get_player_input()

            if action == "quit":
                print("Thanks for playing!")
                break

            elif action.startswitch("go"):
            
            elif action == "take":

            elif action == "inventory":

    if __name__ == "__main__":
        play_game()