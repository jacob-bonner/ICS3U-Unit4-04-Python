#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This is a guess the number program with a random number generator


import random


def main():
    # This function allows the user to try and guess the number

    # Variables
    correct_number = random.randint(1, 10)

    # Process
    while True:
        # Input
        user_guess = input("Guess the number between 1 & 10 (integer): ")

        try:
            user_guess = int(user_guess)
            if user_guess == correct_number:
                # Output 1
                print("You correctly guessed the number!")
                break
            else:
                # Output 2
                print("Wrong number, try again!")
                print("")
        except Exception:
            print("That is not an integer.")
            print("")


if __name__ == "__main__":
    main()
