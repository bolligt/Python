# This program plays the game of Higher Lower.  A player is presented with two people or Organizations and they are asked to guess which has the higher number of Instagram followers.
# If the player guesses correctly, their score increases by 1 and the item they guesses is then compared to a new 

# Modules needed for program
import random
from game_data import data

def determine_outcome(player_pick, first_item, second_item, score):
    '''
    This function determines if the player guessed correctly and then adjusts their score and prints appropriate messaging accordingly.
    Function is meant to return the value of the player's score and should be assigned score variable.
    '''

    if player_pick == "A" and first_item["follower_count"] > second_item["follower_count"]:
        score += 1
        print("Correct!")
        return score
    elif player_pick == "B" and second_item["follower_count"] > first_item["follower_count"]:
        score += 1
        print("Correct!")
        return score
    else:
        print("Incorrect!")
        print(f"Your final score is {score}.")
        # Returns False if the player guesses incorrectly in order to break out of loop in main game function 
        return False

def game(data):
    # Track player score
    score = 0

    # Randomly pick an item from the game data dictionary and remove this from being picked again
    first_item = random.choice(data)
    data.remove(first_item)

    # Randomly pick an item from the game data dictionary and remove it from being picked again
    second_item = random.choice(data)
    data.remove(second_item)

    # While Loop Control Variable
    game_on = True

    while game_on:
        # Obtain name of first and second items for display purposes
        first_item_name = first_item["name"]
        second_item_name = second_item["name"]
        
        # Testing Code
        #print(first_item)
        #print(second_item)

        # Ask the player to choose who/what they think has the higher amount of Instagram followers
        player_pick = input(f"Who has more followers?  Type 'A' for {first_item_name} or type 'B' for {second_item_name}. ").upper()

        # Determine if the player guesses correctly or incorrectly and display appropriate messaging and adjust score if needed
        score = determine_outcome(player_pick, first_item, second_item, score)

        # If they guess incorrectly, score becomes False to break from the loop
        if score == False:
            break
        # Otherwise the game continues
        else:
            print(f"Your current score is {score}.")

        # Check if there are any items left that haven't been chosen
        if len(data) > 0:
            if second_item["follower_count"] > first_item["follower_count"]:

                # Set to the first item to keep for the next round
                first_item = second_item

            # Assign a new second item for the next round and remove it from being picked again
            second_item = random.choice(data)
            data.remove(second_item)
            
        # If all items have been chosen then the game ends
        else:
            print("Congratulations!  You guessed everything correctly!")
            break

# Main Program Run

game(data)