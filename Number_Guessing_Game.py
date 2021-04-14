# Number Guessing Game

import random


def get_result(guessed_num, random_num):
    if guessed_num == random_num:
        print("You Guessed the number correctly!")
        print("Random Number: ", random_num)
    elif guessed_num > random_num:
        print("You need to guess lower. Try Again!")
        all_guesses.append(guessed_num)
    else:
        print("You need to guess higher. Try Again!")
        all_guesses.append(guessed_num)


randomNum = random.randrange(1, 51, 1)  # random selection of a number
userGuess = -1
all_guesses = []    # stores all wrong guesses by the user in a list
while userGuess != randomNum:
    userGuess = int(input("Guess a number between 1 and 50: "))
    get_result(userGuess, randomNum)

print("Your wrong guesses: {}".format(all_guesses))
