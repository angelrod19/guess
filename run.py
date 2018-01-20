# Guess the Number Game
# Developed on December 8th, 2017
# by Angel Rodriguez
# Last modified on: December 8th, 2017

# This program uses the Colorama API to make it clearer to read in the console
# by using colored text. To install this API, go to the console and type:
# "pip install colorama"

import time
import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.RED + "\nWelcome to Guess the Number Game!")
print(Fore.RED + "You have 10 tries to guess a number between 1 and 100, good luck!")

randomNumber = random.randint(1,100)

win = False
count = 1

while (win == False and count < 11):
    print("\nTry #{0}: What is your guess?: ".format(count) )

    try:
        guess = int(input())
    except ValueError:
       print ("Invalid input. Exiting program.")
       exit()

    if (guess < 1 or guess >100):
        print(Fore.RED + "This number is out of range! Remember the real number is between 1 and 100")

    elif (guess > randomNumber):
        print(Fore.RED + "Your number is too high!")
        count += 1

    elif (guess < randomNumber):
        print(Fore.RED + "Your number is too low!")
        count += 1

    else:
        print(Fore.GREEN + "\nCongrats, you got it!")
        exit()

print("\nSorry, try again!")
