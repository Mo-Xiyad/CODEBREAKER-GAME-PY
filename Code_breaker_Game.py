from art import *
import random
print('''Enter a 3 digit number to guess what the computer is think.

HINTS:-
    Close: You've guessed a correct number but in the wrong position
    Match: You've guessed a correct number in the correct position
    Nope: You haven't guess any of the numbers correctly
''')

# GET GUESS


def user_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("What is your guess? "))


# GENERATE COMPUTER CODE 123

def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits = []  # [str(num) for num in range(10)]

    for num in range(10):
        digits += str(num)

    # Shuffling the digits
    random.shuffle(digits)
    # grabing the first three numbers
    return digits[:3]


# GENERATE THE CLUES
def generate_clue(code, userGuess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and
    creates a list of clues according to the matching parameters.
    '''

    win = "YOU GENIUS, YOU HAVE CRACKED THE CODE!"

    if userGuess == code:
        return win

    clues = []

    # Compare guess to the code
    for indx, num in enumerate(userGuess):
        if num == code[indx]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues


# RUN GAME LOGIC

# Create a Secret Code to start the Game
computer_code = generate_code()
print("Welcome to code breaker 1.1!")

tprint("Code Breaker", font='random-small')

# Empty Clue Report to Start with
clue_report = []

# Keep asking until the user has gotten it right!
while clue_report != "YOU GENIUS, YOU HAVE CRACKED THE CODE!":

    # Ask for guess
    guess = user_guess()

    # Give the clues
    clue_report = generate_clue(guess, computer_code)

    print("Here is your guess: ")
    for clue in clue_report:
        print(clue)
