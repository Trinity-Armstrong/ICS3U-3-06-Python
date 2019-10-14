#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This is the guess the number program


import random


def main():
    # this function runs the guess the number program

    # variables
    random_number = random.randint(0, 9)

    # input
    user_guess = input("Guess a number between 0 and 9 (integer): ")

    # process & output
    try:
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("")
            print("You are correct!!!")
        else:
            print("")
            print("Sorry, try again :)")
    except Exception:
        print("")
        print("That is not an integer.")


if __name__ == "__main__":
    main()
