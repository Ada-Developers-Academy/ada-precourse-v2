import random

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'

SNOWMAN_WRONG_GUESSES = 7

SNOWMAN_WORD = "broccoli"

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
def snowman():
    correct_guesses = 0
    wrong_guesses = 0
    while wrong_guesses < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user()
        if user_input in SNOWMAN_WORD:
            print("You guessed a letter that's in the word!")
            correct_guesses += 1
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses += 1
        print_snowman_graphic(wrong_guesses)


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

def print_snowman_graphic(wrong_guesses_count):
    
    for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count, SNOWMAN_WRONG_GUESSES + 1)
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)


guess_the_number()
snowman()
