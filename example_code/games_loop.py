import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100

HANGMAN_1 = '________'
HANGMAN_2 = '|       |'
HANGMAN_3 = '|       O'
HANGMAN_4 = '|       |'
HANGMAN_5 = '|      /|\ '
HANGMAN_6 = '|       |'
HANGMAN_7 = '|      / \ '

HANGMAN_WRONG_GUESSES = 7

def guess_the_number():

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)
    correct_guess = False
    while not correct_guess:
        user_input = get_number_from_user()
            
        if user_input == random_number:
            print("You guessed the number!  Good job!")
            correct_guess = True
        if user_input > random_number:
            print("Your guess is too high")
        if user_input < random_number:
            print("Your guess is too low")
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")
        

# Hooray, it works now!
def get_number_from_user():
    valid_input = False
    user_input = None
    while not valid_input:
        user_input_string = input("Guess the number: ")
        
        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            valid_input = True
        else:
            print("You must input a number!")

    return user_input

# 
def hangman():
    r = RandomWord()
    hangman_word = r.word(word_min_length=5, word_max_length=8)
    print(f"debug info: {hangman_word}")
    correct_guesses = 0
    wrong_guesses = 0
    while wrong_guesses < HANGMAN_WRONG_GUESSES:
        user_input = get_letter_from_user()
        if user_input in hangman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses += 1
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses += 1
        print_hangman_graphic(wrong_guesses)


def get_letter_from_user():
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        else:
            valid_input = True

    return user_input_string

def print_hangman_graphic(wrong_guesses_count):
    for i in range(wrong_guesses_count):
        if(i == 0):
            print(HANGMAN_1)
        if(i == 1):
            print(HANGMAN_2)
        if(i == 2):
            print(HANGMAN_3)
        if(i == 3):
            print(HANGMAN_4)
        if(i == 4):
            print(HANGMAN_5)
        if(i == 5):
            print(HANGMAN_6)
        if(i == 6):
            print(HANGMAN_7)



guess_the_number()
hangman()
