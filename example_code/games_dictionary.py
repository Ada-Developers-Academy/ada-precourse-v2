import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_GRAPHIC = ['*   *   *  ', ' *   _ *   ', '   _[_]_ * ', '  * (")    ', '  \( : )/ *', '* (_ : _)  ', '-----------']

SNOWMAN_WRONG_GUESSES = len(SNOWMAN_GRAPHIC)

SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

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


def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    #print(f"debug info: {snowman_word}")
    snowman_list = build_word_list(snowman_word)
    correct_guesses_list = []
    wrong_guesses_list = []
    all_guessed = False
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and not all_guessed:
        user_input = get_letter_from_user(correct_guesses_list, wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
            all_guessed = update_and_check_word_list(snowman_list, user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))
        print_word_feedback(snowman_list)
        print("Wrong guesses: " + " ".join(wrong_guesses_list))

    if all_guessed:
        print("Congratulations, you win!")
    else:
        print(f"Sorry, you lose!  The word was {snowman_word}")


def build_word_list(word):
    word_list = []
    for letter in word:
        letter_dict = {"letter": letter, "guessed": False}
        word_list.append(letter_dict)
    return word_list

def update_and_check_word_list(word_list, letter):
    word_finished = True
    for elem in word_list:
        if elem["letter"] == letter:
            elem["guessed"] = True
        if not elem["guessed"]:
            word_finished = False
    return word_finished
    
def print_word_feedback(word_list):
    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)



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
