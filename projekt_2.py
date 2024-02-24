"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Soukop
email: midasasa5757@gmail.com
discord: miso5757 (engeto server: Michal S.)
"""
import random
import time

separator = "-" * 48
play = True
numbers = []
tips = 0
bulls = 0
cows = 0

print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(separator)

# Function to generate the secret number
def generate_secret_number():
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == 4 and str(number)[0] != "0": # Check if the number does not repeating digits, not start with zero
            return number
        
target_number = generate_secret_number() # Generate the secret number

# Function to get the correct form of the word "bull" based on the count
def get_bull(num):
    if num == 1:
        return "bull"
    else:
        return "bulls"

# Function to get the correct form of the word "cow" based on the count
def get_cow(num):
    if num == 1:
        return "cow"
    else:
        return "cows"
    
# Save the start time of the game
start = time.time()
while play:

    numbers.clear()
    guess = input("Enter a number: ") # User input
    numbers = [number for number in guess] # Convert the input to a list of characters
    print(separator)
    tips += 1

    # Check if the guess contains only numbers
    if not guess.isnumeric():
        print("Your entry must contain numbers only!")
        continue

    # Check if the guess does not start with zero
    if str(guess).startswith("0"):
        print("Your entry must not start with a zero!")
        continue

    # Check if the guess is of length 4
    if len(guess) != 4:
        print("Your entry must be four numbers only!")
        continue

    # Check if the guess does not contain repeating digits
    if len(guess) != len(set(guess)):
        print("Your entry must not contain duplicates!")
        continue

    # Compare the secret number with the guess and count the bulls and cows
    for num_secret, num_guess in zip(str(target_number), numbers):

        if num_secret == num_guess:
            bulls += 1

        elif num_guess in str(target_number):
            cows += 1

    # If all numbers are in the right positions, the player wins
    if bulls == 4:
        print(target_number)
        print(f"in {tips} guesses!")
        print()
        end = time.time()
        game_time = end - start
        print(f"Game time {int(game_time)} seconds")
        print(separator)

        # Print a message based on the number of guesses
        if 0 < tips <= 4:
            print("That's amazing!")
            quit()

        if 4 < tips <= 7:
            print("That's average.")
            quit()

        if 7 < tips:
            print("Not so good...")
            quit()

    print(bulls, get_bull(bulls), ",", cows, get_cow(cows))
    print(separator)

    bulls = 0
    cows = 0