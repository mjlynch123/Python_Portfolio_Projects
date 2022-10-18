from random import randint
from os import system, name
from time import sleep
import sys

def clear():
        # for windows
            if name == 'nt':
                _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

def rollDice():
    score = 0
    started = False

    starting = input("type 'y' to start: ")

    if starting.lower() == 'y':
        started = True
    else:
        print("Goodbye")
        sys.exit()

    while starting:
        roll = randint(1, 6)
        second_roll = randint(1, 6)
        

        clear()
        sleep(.2)
        print(f"Score: {score}")
        print(f"First Roll: {roll}")
        print(f"Second Roll: {second_roll}")

        score_added = roll + second_roll
        score += score_added

        if roll and second_roll == 6:
            score = score // 2

        if score == 21:
            print("Congrats you have won")
            sleep(3)
            sys.exit()
        elif score > 21:
            print("You have gone over 21. Try again!")
            sleep(5)
            sys.exit()

        input("Press 'Enter' for another roll: ")

def how_to_play():
    clear()
    print("This is the help page!")
    print()
    print("1. Once the game has started, you cannot exit until the game ends.")
    print()
    print("2. If you roll double 6's, your score will be divided by 2.")
    print()

rollDice()