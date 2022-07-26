# Dictionary Lesson Sample Code

```python
import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

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
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH,
                          word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    #print(f"debug info: {snowman_word}")
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    all_guessed = False
    get_word_progress(snowman_word, snowman_dict)
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and not all_guessed:
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            snowman_dict[user_input] = True
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman(len(wrong_guesses_list))
        all_guessed = get_word_progress(snowman_word, snowman_dict)
        print("Wrong guesses: " + " ".join(wrong_guesses_list))

    if all_guessed:
        print("Congratulations, you win!")
    else:
        print(f"Sorry, you lose!  The word was {snowman_word}")


def build_word_dict(word):
    word_dict = {}
    for letter in word:
        word_dict[letter] = False
    return word_dict
    
def print_word_progress_string(word, word_dict):
    output_string = ""
    for elem in word:
        if word_dict[elem]:
            output_string += elem
        else:
            output_string += "_"
        output_string += " "
    print(output_string)

def get_word_progress(word, word_dict):
    for elem in word:
        if not word_dict[elem]:
            return False
    return True

def get_letter_from_user(word_dict, list2):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in word_dict and word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in list2:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])



#guess_the_number()
snowman()
```
