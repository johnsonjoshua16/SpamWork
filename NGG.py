print("Number Guessing game")
import random
import time

chars = '0123456789'

while True:
    num = ''
    for x in range(2):
        num += random.choice(chars)

    print("Guess the 2-digit number I am thinking of! (00-99)")
    print("You have 1 try to guess it.")

    guess = input("Enter your guess: ")
    if guess == num:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Sorry, that's not correct. The number was:", num)
        print("Better luck next time!")

    time.sleep(2)
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break