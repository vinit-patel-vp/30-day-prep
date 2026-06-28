##########################################################################
# Your task:
# Build a number guessing game that:

# Picks a random number between 1 and 100
# Asks user to guess
# Says "too high" or "too low"
# Keeps asking until correct
# Counts how many guesses it took
##########################################################################
import random

number_to_guess = random.randint(1,100)

print(number_to_guess)

number_guessed = 0
counter = 0

while True:

    counter = counter+1
    number_guessed = int(input("Enter your number"))
    if number_guessed < number_to_guess:
        print("Higher")
    elif number_guessed > number_to_guess:
        print("Lower")
    elif number_guessed == number_to_guess:
        print("Correct")
        break
    else:
        print("Invalid Input")



print(f"It took you {counter} number of tries to guess the correct answer")
