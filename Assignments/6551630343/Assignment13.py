import sys
sys.path.append('../../libs/')

import print_utils as printu
import random

MAXROUND = 5
LOW = 1
HIGH = 99

def main():
    
    printu.print_repeat_str("*", 5)
    print(" Welcome to the game of guessing number ", end="")
    printu.print_repeat_str("*", 5, "\n")

    # Game states
    round = 1
    low = LOW
    high = HIGH
    answer = random.randint(low, high)
    
    game(answer, round, low, high)

    return


def game(answer, round, low, high):

    if (round > MAXROUND):
        printu.print_repeat_str("#", 50, "\n")
        printu.print_centered(
            f"!!!SORRY!!! The secret number is {answer}", 50, "\n")
        printu.print_repeat_str("#", 50, "\n")
        return
    
    printu.print_repeat_str("-", 22)
    print("round", round, end="")
    printu.print_repeat_str("-", 22, "\n")
    
    guess_input = input(f"Enter an integer from {low} to {high} : ")
    
    if not guess_input.isdigit():
        print("Please enter number")
        game(answer, round, low, high)
    else:
        guess = int(guess_input)
        
        if guess < low or guess > high:
            print(f"Please enter number from {low} to {high}")
            game(answer, round, low, high)
        elif guess > answer:
            print("Hint: Your guess is high")
            game(answer, round + 1, low, guess - 1)
        elif guess < answer:
            print("Hint: Your guess is low")
            game(answer, round + 1, guess + 1, high)
        else:
            printu.print_repeat_str("#", 50, "\n")
            printu.print_centered(
                "*** CONTRAGURATION *** Your guess is correct", 50, "\n")
            printu.print_repeat_str("#", 50, "\n")
            return


if __name__ == "__main__":
    main()
