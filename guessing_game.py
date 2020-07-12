# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:26:39 2020

@author: Janu

Random Number Generated

Player instructed to guess a number between 1 and 10

If the guess is incorrect the player is told to guess again and
whether the number is higher or lower

The player will keep getting chances to guess until 5 opportunities have passed

If the player guesses the number they get a message congratulations you guessed correctly

If the player faiels to guess the number they get a message saying Sorry you did not
 guess the nubmer
The correct Nubmer is ____

"""
from random_number_generator import generate_secret_number

def main():
    """This runs the game"""
    print('Welcome to the jungle!')
    print(f'this is the secret number is {generate_secret_number()}')
    user_guess = input("Please guess the secret number between 1 and 10: ")
    if user_guess.isdigit():
        ug_number = int(user_guess)
        print(ug_number, type(ug_number))

    else:
        print("Please enter a number only")

if __name__ == '__main__':
    main()
    