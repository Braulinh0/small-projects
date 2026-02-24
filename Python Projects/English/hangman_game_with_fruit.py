# Import choice to randomly select fruits

from random import choice

# ---------------------------------------------------------------

# We create multiple fruit options to select randomly

def selection():
    options = ["apple", "strawberry", "peach", "orange", "kiwi", "banana", 
               "mango", "pomegranate", "melon", "watermelon", "tangerine", "lemon", "grape",
               "cherry", "pineapple", "passionfruit", "blackberry", "raspberry", "plum", 
               "papaya", "pear", "coconut", "cherimoya", "fig", "mulberry", "grapefruit",
               "apricot"]
    return choice(options)  # Return a randomly chosen word.

# ---------------------------------------------------------------

# We check whether the letter selected by the user has already been used before.

def already_chosen(c, used_list):
    if c in used_list:
        return True
    else:
        used_list.append(c)
        return False

# ---------------------------------------------------------------

# Then, we check if the letter selected by the user appears in the hidden word.

def check_letter(word, c, progress):
    found = False  # <- Used to check if the letter appears at least once in the word.
                   # If it does not appear at all, the player will lose one life.
                       
    new_progress = list(progress)  # <- Stores the discovered letters of the hidden word.
    counter = 0  # <- Number of characters that will be subtracted from the remaining hidden letters.
    
    for i in range(len(word)):
        if word[i] == c and progress[i] == '_':
            new_progress[i] = c
            found = True
            counter += 1
            
    # Return whether at least one match was found, the updated progress string,
    # and how many letters were revealed.
    return found, "".join(new_progress), counter
    
# ---------------------------------------------------------------

word = selection()
progress = '_' * len(word)
used_letters = []  # <- Record of letters already used by the player.
lives = 6  # <- You can edit this to make the game longer or shorter.
remaining_letters = len(word)  # <- Total number of letters still hidden.

while lives != 0:
    print(f"\nWord: {progress}")  # <- Shows the current discovered progress of the mystery word.
    print(f"Lives: {lives} | Used letters: {sorted(used_letters)}")  # <- Player lives and used letters.
    print(f"Remaining letters: {remaining_letters}")  # <- Total letters still hidden.
    
    letter = input("Enter a letter: ").lower()
    
    if already_chosen(letter, used_letters):
        print("You have already chosen this letter, select another one.")
        continue

    correct, progress, subtract = check_letter(word, letter, progress)
    
    if correct:  # <- If at least one letter was guessed correctly.
        print("You got it right!")
        remaining_letters -= subtract
    else:  # <- If the guess was incorrect.
        print("This letter is not in the word...")
        lives -= 1
        
    if "_" not in progress:  # <- Check if there are no more hidden characters.
        print(f"Congratulations, you won! The word was: {word}")
        break
    
if lives == 0:
    print(f"You lost! The word was: {word}")
