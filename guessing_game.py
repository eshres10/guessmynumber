#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Created By  : Ena Shrestha
# Created Date: 27/02/2022 
# =============================================================================
"""
This is a simple guessing game where the coomputer generates a random number between 1-10 and the user has to guess within 3 tries.
The computer provides hints if the number you've guessed it lower or higher than the its chosen number.

"""
# =============================================================================



# =============================================================================
#Imports
# =============================================================================

import random
import sys
# =============================================================================


# =============================================================================
#Functions
# =============================================================================

#Main Function
def play():
    print("Welcome to the guessing game! I will think of a random number between 1-10 and you'll need to find out what it is in three tries!")
    attempts = 0
    attempts_provided = 5
    random_number = random.randint(1, 10)

    while attempts < attempts_provided:
        attempts_left = attempts_provided - attempts
        print()
        print("Number of attempts left: ", attempts_left)
        print("I've thought of a number between 1 to 10." )
        try:
            attempts += 1
            user_input = int(input("What's your guess? "))
        
            if user_input > 10:
                print()
                print("Sorry that's not a valid number. Please enter number between 1 - 10")
     
            elif user_input < random_number:
                print()
                print("That's not correct! Guess higher")
            elif user_input > random_number:
                print()
                print("That's not correct! Guess lower")
            elif user_input == random_number:
                print()
                print("That's correct! Winner winner chicken dinner.")
                attempts = attempts_provided + 1
                play_again()
                break    
        except ValueError:
            print("Wrong Input! You can only enter integers between 1-10")

    else:

        print("Sorry, you're out of attempts.")
        print("The number I was thinking of was: ", random_number)
        play_again()

def play_again():
    print("Want to play again?")
    yes_no = input("Type 'Y' for yes and 'N' for no: ")
    try: 
        if yes_no.upper() == "Y":
            play()
        elif yes_no.upper() == "N":
            print("Thanks for playing")
            sys.exit()
        else:
            print("Invalid input. Type 'Y' for yes and 'N' for no ")
            play_again()
    except Exception as e:
        print("F#$#$ ERROR")
        print(e)

play()
exit()
            

    




 
    