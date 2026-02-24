# Import randint from the random library to generate random numbers

from random import randint

# ---------------------------------------------------------------

secret_number = randint(1, 100)  # -> Generate a random secret number between 1 and 100
lives = 8
found = False

# ---------------------------------------------------------------

while lives >= 0:
    guess = int(input("\nEnter a number: "))
    
    if guess < 1 or guess > 100:  # -> Check if the number entered is outside the allowed range
        print("The entered number is not allowed.")
    elif guess < secret_number:  # -> If the number is lower than the secret number
        print("Incorrect number.")
        print("The chosen number is lower than the hidden number.")
        lives -= 1
    elif guess > secret_number:  # -> If the number is greater than the secret number
        print("Incorrect number.")
        print("The chosen number is greater than the hidden number.")
        lives -= 1
    elif guess == secret_number:  # -> If the entered number matches the secret number
        print("You found the hidden number!")
        print(f"The hidden number was: {secret_number}")
        print(f"You finished with {lives} lives remaining!")
        found = True
        break
    
# ---------------------------------------------------------------

if found == False:  # -> If the loop ended and the player did not find the number
    print(f"\nYou lost! The hidden number was: {secret_number}")
