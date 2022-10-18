from random import choice
from os import system, name
from time import sleep

hang = ["""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

limit = 5
word_split = []
word_progress = []
missed_letters  = []
guessed = []
word = ""

def clear():
        # for windows
            if name == 'nt':
                _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

def display_board(hang, missedLetters, correctLetters, secret_word):
    #print(hang[len(missedLetters)])
    print()

    print('Missed Letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print('\n')

    blank_spots = '_' *len(secret_word) # Creates the blank lines for the word

    for i in range(len(secret_word)):
        if secret_word[i] in correctLetters: # This loop changes the blank spots to the letter guessed if its the correct letter
            blank_spots = blank_spots[:i] + secret_word[i] + blank_spots[i+1:]

    for letter in blank_spots:
        print(letter, end=' ')
    print('\n')

def choose_word():
    words = ["bunny", "money", "ham", "list", "type"]
    word_choice = choice(words)
    
    for letter in word_choice:
        word_split.append(letter)

def player_word_choice():
    lives = 5
    while len(word_progress) < len(word_split):
        clear()
        print("Lives: {}".format(lives))
        display_board(hang, missed_letters, word_progress, word_split)
        player_input = input("Please enter one letter: ")

        if player_input in word_split:
            word_progress.append(player_input)
            guessed.append(player_input)
            sleep(1)
        elif player_input in guessed:
            print("You have already guessed this")
        elif player_input not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
            lives -= 1
            sleep(1)
        else:
            print("No such letter")
            guessed.append(player_input)
            lives = lives - 1
            sleep(1)

        if lives == 0:
            print("You are hanged. Would you like to play again: ")
            play_again = input("> ")
            if play_again.lower() == 'y':
                print("Playing again! One Second...")
                word_split.clear()
                word_progress.clear()
                sleep(1)
                clear()
                choose_word()
                player_word_choice()
            else:
                break
    
    print()
    print("Chosen Word: {}".format(word.join(word_split)))
    print()

clear()
print("Welcome to hangman. The point of the game is to guess a letter each turn to try and finish the word.")
print()
sleep(5)
clear()
print("Collecting Word...")
sleep(4)
clear()
choose_word()
player_word_choice()