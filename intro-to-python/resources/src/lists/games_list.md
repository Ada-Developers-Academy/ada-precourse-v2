# List Lesson Sample Code

```python

import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100
MAX_GUESSES = 20

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

SNOWMAN_MAX_WRONG_GUESSES = len(SNOWMAN_GRAPHIC)
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    waiting_for_correct_guess = True
    num_guesses = 0

    while (waiting_for_correct_guess and num_guesses <= MAX_GUESSES):
        num_guesses += 1
        user_input = get_number_from_user()

        if user_input == random_number:
            print("You guessed the number! Good job!")
            waiting_for_correct_guess = False
        elif user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")

    if waiting_for_correct_guess:
        print(f"You ran out of guesses! The correct answer was {random_number}.")

def get_number_from_user():
    attempting_valid_input = True
    user_input = None

    while attempting_valid_input:
        user_input_string = input("Guess the number: ")

        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            attempting_valid_input = False
        else:
            print("You must input a number!")

    return user_input

# Snowman Section
def snowman():
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(
      word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
      word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    print(f"debug info: {snowman_word}")

    correct_guesses_list = []
    wrong_guesses_list = []

    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list, correct_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
            
        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

def get_letter_from_user(wrong_guesses_list, correct_guesses_list):    
    valid_input = False
    user_input_string = None
    
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in wrong_guesses_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter")
        else:
            valid_input = True

    return user_input_string

def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count,
                   SNOWMAN_MAX_WRONG_GUESSES):
            print(SNOWMAN_GRAPHIC[i])

# guess_the_number()
snowman()

```