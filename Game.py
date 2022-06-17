# Random Integer Game

    # How to play:
        # A radnom integer is selected from 1 to 100 and a the player begins by guessing a number.
        # Based the the player's guess the program will say higher or lower till the player gets it right.


# ------------------------------

# Importing the proper packages
import random

class Game:
    target = random.randint(1,100)
    num_of_tries = 1


guess = int(input('Guess a number between 1 and 100: '))


while guess != Game.target:
    if guess < Game.target:
        guess = int(input('Your guess was too low. Try again: '))
    else:
        guess = int(input('Your guess was too high. Try again: '))
    Game.num_of_tries += 1

print('Well done! You got the answer in {} tries.'.format(Game.num_of_tries))