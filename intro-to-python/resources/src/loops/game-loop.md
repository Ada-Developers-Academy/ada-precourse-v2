# Loop Lesson Sample Code

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100
MAX_GUESSES = 20

SNOWMAN_0 = '*   *   *  '
SNOWMAN_1 = ' *   _ *   '
SNOWMAN_2 = '   _[_]_ * '
SNOWMAN_3 = '  * (")    '
SNOWMAN_4 = '  \\( : )/ *'
SNOWMAN_5 = '* (_ : _)  '
SNOWMAN_6 = '-----------'

SNOWMAN_MAX_WRONG_GUESSES = 7
SNOWMAN_WORD = "broccoli"

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

# Main Snowman function
def snowman():
    correct_guesses = 0
    wrong_guesses = 0

    while wrong_guesses < SNOWMAN_MAX_WRONG_GUESSES and correct_guesses < len(SNOWMAN_WORD):
        user_input = get_letter_from_user()
        if user_input in SNOWMAN_WORD:
            print("You guessed a letter that's in the word!")
            correct_guesses += 1
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses += 1

        print_snowman(wrong_guesses)

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

def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        if i == 0:
            print(SNOWMAN_0)
        elif i == 1:
            print(SNOWMAN_1)
        elif i == 2:
            print(SNOWMAN_2)
        elif i == 3:
            print(SNOWMAN_3)
        elif i == 4:
            print(SNOWMAN_4)
        elif i == 5:
            print(SNOWMAN_5)
        elif i == 6:
            print(SNOWMAN_6)

guess_the_number()
snowman()
```