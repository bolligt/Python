# My Original Version - Revisit later for possibly functionalization

# Players select a difficulty level which determines how many guesses they get.
# The program will pick a random number from 1 to 100 and the player gets only so many guesses to pick the correct number.

import random
from game_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print()

# Generate random number
answer = random.randint(1,100)

# Set difficulty level
difficulty_level = input("Select your difficulty level.  Type 'easy' or 'hard'. ").lower()

# Set number of turns left based on difficulty level
if difficulty_level == 'easy':
    guesses_remaining = 10
else:
    guesses_remaining = 5

print(f"You have selected {difficulty_level} mode.  You have {guesses_remaining} guesses.  Good luck!")

game_on = True

while game_on:
    # Prompt player for guess
    player_guess = int(input("Guess a number from 1 to 100 "))

    # Compare guess to actual number
    # Determine if guess was correct or not, print win message if correct
    # If guess is incorrect, minus 1 guess, if out of guesses print losing messages
    # If guesses still remain, determine if guess was high or low
    if player_guess == answer:
        print(f"Congratulations!  You guessed correctly!  The answer was {answer}.  You win!")
        game_on = False
    else:
        guesses_remaining -= 1

        if guesses_remaining == 0:
            print(f"Incorrect!  You have no guesses remaining.  You lose.  The correct answer was {answer}.")
            game_on = False
        else:
            if player_guess > answer:
                print(f"Incorrect!  You guessed too high. You have {guesses_remaining} guesses remaining. Guess again. ")
            else:
                print(f"Incorrect!  You guessed too low. You have {guesses_remaining} guesses remaining. Guess again. ")