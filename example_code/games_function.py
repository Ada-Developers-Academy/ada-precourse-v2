import random

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_WORD = "broccoli"

def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    user_input = get_number_from_user()

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number!  Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")


# This does not work, but it's temporary.  We will fix this in the next lesson
def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input


def snowman():
    user_input = get_letter_from_user()
    if user_input in SNOWMAN_WORD:
        print("You guessed a letter that's in the word!")
    else:
        print(f"The letter {user_input} is not in the word")


def get_letter_from_user():
    user_input_string = input("Guess a letter: ")
    if not user_input_string.isalpha():
        print("You must input a letter!")
    elif len(user_input_string) > 1:
        print("You can only input one letter at a time!")

    return user_input_string

guess_the_number()
snowman()
