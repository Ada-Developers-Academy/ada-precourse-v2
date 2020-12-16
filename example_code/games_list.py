import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_GRAPHIC = ['*   *   *  ', ' *   _ *   ', '   _[_]_ * ', '  * (")    ', '  \( : )/ *', '* (_ : _)  ', '-----------']

SNOWMAN_WRONG_GUESSES = len(SNOWMAN_GRAPHIC)

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
    r = RandomWord()
    snowman_word = r.word(word_min_length=5, word_max_length=8)
    print(f"debug info: {snowman_word}")
    correct_guesses_list = []
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(correct_guesses_list, wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")


def get_letter_from_user(list1, list2):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in list1 or user_input_string in list2:
            print("You already guessed that letter")
        else:
            valid_input = True

    return user_input_string

def print_snowman_graphic(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
            print(SNOWMAN_GRAPHIC[i])



#guess_the_number()
snowman()
