# Start creating a text based adventure game
# Introduction
def show_intro():
    '''Displays the game's introduction'''
    print('\nWelcome to the Adventure of the Hidden Treasure!')
    print('You are an intrepid explorer seeing a legendary treasure hidden deep within an ancient temple.')
    print('Your journey will be fraught with peril, but the rewards are immeasurable.')
    print('Good luck!\n')
# Show the current location
def show_current_location(location, locations):
    '''Displays the description of the current location'''
    print(f'\nYou are in {locations[location]['name']}.')
    print(locations[location]['description'])
    if 'items' in locations[location] and locations[location]['items']:
        print('You see the following items:')
        for item in locations[location]['items']:
            print(f'- {item}')
# Get the users input
def get_player_input():
    '''Gets and validates player input'''
    while True:
        action = input('> ').lower()
        if action in ['go north', 'go south', 'go east', 'go west', 'take', 'inventory', 'quit']:
            return action
        else:
            print('Invalid action. Try again.')
def move_player(location, direction, locations):
    '''Moves the player to a new location if possible'''
    new_location = locations[location]['directions'].get(direction)
    if new_location:
        return new_location
    else:
        print('You cannot go that way.')
        return location
# Adds an item to the player's inventory
def take_item(location, item, locations, inventory):
    '''Adds an item to the player's inventory if possible'''
    if 'items' in locations[location] and item in location[location]['items']:
        inventory.append(item)
        locations[location]['items'].remove(item)
        print(f'You take the {item}.')
    else:
        print('There is no such item here.')
# Shows the player's inventory
def show_inventory(inventory):
    '''Displays the player's inventory'''
    if inventory:
        print('\nYour inventory:')
        for item in inventory:
            print(f'- {item}')
    else:
        print('\nYour inventory is empty.')
# --- The Main Game Loop ---
def play_game():
    '''Main game loop'''
    locations = {
        'entrance':{
            'name': 'The Temple Entrance',
            'description': 'A grand archway leads into a dark and mysterious temple.',
            'directions':{'north': 'hallway'},
        },
        'hallway': {
            'name': 'a dimly lit Hallway',
            'description': 'Torches flicker on the walls, casting long shadows. There are doors to the east and west.',
            'directions': {'east': 'chamber', 'west': 'treasury', 'south': 'entrance'},
        },
        'chamber': {
            'name': 'The Treasury',
            'description': 'This is where the legendary teasure is said to be hidden!',
            'directions': {'east': 'hallway'},
            # Add treasure and challenges here later
        },
    }
    current_location = 'entrance'
    inventory = []
    show_intro()
    while True:
        show_current_location(current_location, locations)
        action = get_player_input()
        if action == 'quit':
            print('Thanks for playing!')
            break
        elif action.startswith('go'):
            direction = action.split()[-1]
            current_location = move_player(current_location, direction, locations)
        elif action == 'take':
            item = input('What do you want to take? ').lower()
            take_item(current_location, item, locations, inventory)
        elif action == 'inventory':
            show_inventory(inventory)
if __name__ == '__main__':
    play_game()