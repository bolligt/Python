import random
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

print(stages[lives])

game_on = True
while game_on:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.  You lose a life.")
        lives -= 1
    else:
        index = 0
        for letter in chosen_word:
            if letter == guess:
                display[index] = letter
            index += 1

    print(' '.join(display))
    print(stages[lives])

    if lives == 0:
        game_on = False
        print("You lose.")
    elif "_" not in display:
        game_on = False
        print("You win!")