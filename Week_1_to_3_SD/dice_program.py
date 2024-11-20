print('Press the enter key to roll a dice, to receive a random roll')
from random import randint

input('')
dice_roll = randint(1,6)
print(dice_roll)
print(f'The dice rolled a {dice_roll}')