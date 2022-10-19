from curses.ascii import isalpha, isdigit
from random import randint, shuffle
from secrets import choice
from os import system, name
from time import sleep
import sys

file = "coins.txt"

with open(file, 'r')as file:
    coin_value = file.read()

score = 0
coins = int(coin_value)
cards = []
chosen_card = []

def clear():
        # for windows
            if name == 'nt':
                _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

def card():
    for v in range(2, 11):
        for s in "Hearts Clubs Diamonds Spades".split():
            cards.append(str(v) + " of " + s)

    for v in "Ace King Queen Jack".split():
        for s in "Hearts Clubs Diamonds Spades".split():
            cards.append(str(v) + " of " + s)

def draw_card():
    card_pick = choice(cards)
    chosen_card.append(card_pick)
    print(chosen_card[-1])

def get_score():
    score_of_card = chosen_card[0].split()
    if score_of_card[0].isdigit():
        card_score = int(score_of_card[0])
    elif score_of_card[0].isalpha():
        card_score = score_of_card[0]

    if card_score == "Ace":
        global score
        if score + 11 > 21:
            card_score = 1 / 2
            score += card_score
        else:
            card_score = 11 / 2
            score += card_score
    
    if card_score == "Queen":
            card_score = 10 / 2
            score += card_score
    elif card_score == "Jack":
            card_score = 10 / 2
            score += card_score
    elif card_score == "King":
            card_score = 10 / 2
            score += card_score
    
    #print(score_of_card[0])
    score += card_score
    print("Score: {}".format(score))

def make_bet(player_score, bet):
    global coins
    global file
    if player_score == 21:
        bet *= bet
        coins += bet
    elif player_score > 21:
        bet *= bet
        coins -= bet

    print("Coins: {}".format(coins))
    with open("coins.txt", 'w') as file:
        file.write(str(coins))

def playAgain():
    global score
    play = input("Would you like to play again?: ")
    if play.lower().startswith("y"):
        playing()
    else:
        sys.exit()

def playing():
    clear()
    global score
    print("Welcome to BlackJack. Press 'Enter' when you're ready")
    input("> ")
    clear()
    print("Coins: " + str(coins))
    print()
    bet = input("How much would you like to bet: ")
    started = True
    card()

    while started:
        clear()
        chosen_card.clear()
        draw_card()
        get_score()

        if score == 21:
            print("You won!")
            make_bet(score, int(bet))
            play = input("Would you like to play again: ")
            if play.lower().startswith("y"):
                score = 0 
                playing()
        elif score > 21:
            clear()
            print("You lost!")
            print()
            print("Final Score: {}".format(score))
            make_bet(score, int(bet))
            play = input("Would you like to play again: ")
            if play.lower().startswith("y"):
                score = 0 
                playing()
            


        con = input("Would you like another card: ")
        if con.lower() == 'y':
            draw_card()
        else:
            break

playing()