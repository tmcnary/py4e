# This is a guess the number game.
import random
print('Hello! Welcome to the guess the number game. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('well, ' + name + ', I am thinking of a number between 1 and 20')

# Gives the player 6 guesses
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Too low.')
    elif guess > secretNumber:
        print('Too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '. You guessed my number in ' + str(guessesTaken) + ' tries!')
else:
    print('Sorry! The number I was thinking of was ' + str(secretNumber) + '.')