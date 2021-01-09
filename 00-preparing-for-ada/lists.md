# Lists

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand lists
    * Create new lists
    * Add elements to lists
    * Access elements of lists
    * Search lists for elements
* Combine lists and loops

## Introduction

### Textbook for this section: [link to ada built lists]

### Why Lists?

[todo: talk about why the need to add data strutures]

## Vocabulary

__TODO__
* list
* index
* package

## Snowman

### Adding A Random Word

So far our Snowman game has used a constant as the secret word (`SNOWMAN_WORD = 'broccoli'), but a game that always uses the same word is not a great game.  The code to generate a random English word is outside of the scope of these lessons, although it is an interesting problem and worth spending some time thinking about.  We are going to use a _package_ to come up with a random word.  We are going to use the wonderword package.  

* Before we can use it in our code, we will need to install the package using the command line `pip3 install wonderwords`.
* Once that's done, add the line `from wonderwords import RandomWord` to the top of our file.
    * This will import the class `RandomWord` for us to use in our code.
* Next, add the constants `SNOWMAN_MAX_WORD_LENGTH = 8` and `SNOWMAN_MIN_WORD_LENGTH = 5` with the other constants at the top of the file.    
* Last, add the following lines of code to the top of the `snowman` function:

```python

    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)

```

The first line `r = RandomWord()` gives us a RandomWord object to work with.  We will not cover classes and objects in the pre-course material, but they will be a topic we will cover at Ada.  The next line, `snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)` will call the function `word` on the the RandomWord object `r` and give us a random word.  We are passing two arguments (word_min_length and word_max_length) using keyword arguments.  Again, we will not be covering these topics further in the pre-course, but they will come up later in the Ada curriculum.  The arguments that we are passing to the function `word` will instruct `word` to give us an English word where the length is between the SNOWMAN_MIN_WORD_LENGTH and SNOWMAN_MAX_WORD_LENGTH.  Feel free to experiment with setting different values for the constants.  The last piece of adding our new random word is replacing the constant `SNOWMAN_WORD` in the conditional test inside of the `snowman` function with the new `snowman_word` variable.

### Tracking User Input

So far all we have done with our user input is check to see if it is in our word, but if we go back to the hypothetical game of snowman with a group, we would want to keep track of the letters that had been guessed.  We would also not accept guesses of the same letter that had been guessed before.  Let's start with tracking incorrect guesses.  We know we are going to have a max of SNOWMAN_WRONG_GUESSES, so we could make that many variables and store our incorrect guesses in those variables.  This solution could be made to work, but every time we change the value of the constant we would have to rewrite our code.  Using a `list` gives us a way to store as many or as little wrong guesses as we want and will allow us to make the code flexible and easy to modify.  Start by addding an incorrect guesses list variable to the top of the `snowman` function:

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    wrong_guesses_list = []
    
    # ...

```

Next we need to add each incorrect guess to the list.  We are going to do this with the list function `append` which adds elements to the end of the list:

```python

# ...
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
# ...

```

In the previous version, we were incrementing a variable `wrong_guesses` each time the user guessed a letter that was not in the word, and then using that variable in the test for our while loop.  We can continue to use this variable, but we can use our list instead and simplify our code.  The number of elements in `wrong_guesses_list` is the number of incorrect guesses, so we can use the length of the list instead of the counter variable.  We get the length of the list by using the len() function.  We can also use the length of the list when we call the print_snowman_graphic function.  Here's the updated version of the function:

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user()
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))

```

###  Using `wrong_guesses_list` in `get_letter_from_user`

Now that we have a list incorrect guesses, we can use them in `get_letter_from_user` to prevent our user from inputting the same incorrect letter multiple times.  
* The first step is to pass the variable `wrong_guesses_list` to `get_letter_from_user` as an argument.  
* Next, We will need to update our function definition of `get_letter_from_user` with a new parameter.  
* Last, we need to use the new information inside of `get_letter_from_user`.  
    * Python lists provide us with a handy `in` operator (syntax `item in list`) that returns `True` if the item is in the list and `False` if it is not.

```python

# ...
def snowman():
    # ...
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list)
    # ...

def get_letter_from_user(wrong_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string

```

### Tracking Correct letters

At this point we are keeping track of the incorrect letters guessed and using those to provide feedback to our user when they guess a new letter.  Now it is time to do the same thing but with correct letters!

* Add a `correct_guesses_list` to the `snowman` function
* Add correct guesses to the list

<details>
<summary>When you are finished, compare your code with ours</summary>

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    print(f"debug info: {snowman_word}")
    correct_guesses_list = []
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

```

</details>

### Using `correct_guesses_list` in `get_letter_from_user`

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: ca1d65d6-960e-4f58-af35-8b8663f8bcf7
* title: get_letter_from_user detecting duplicate entries
* points: 1
* topics: python python-lists

##### !question

Write a new version of `get_letter_from_user` that takes an additional argument (correct_guesses) and uses that along with `wrong_guesses` to print the "You have already guessed that letter" as feedback to the user.

##### !end-question

##### !placeholder

```py
def get_letter_from_user(wrong_list, correct_guesses):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string


```

##### !end-placeholder

##### !tests


```py
import sys
from unittest import mock
from unittest.mock import patch
import io
import unittest
import re

import main as p

class SimplisticTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_already_used_if_in_correct_guesses_list(self, mock_stdout):
        # Arrange
        input_letters = [
            'a',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert re.match('You have already guessed that letter', mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_already_used_if_in_wrong_guesses_list(self, mock_stdout):
        # Arrange
        input_letters = [
            'e',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert re.match('You have already guessed that letter', mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_returns_valid_letter_after_invalid_guess(self, mock_stdout):
        # Arrange
        input_letters = [
            'e',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert answer == input_letters[-1]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_only_one_letter_at_a_time_for_input_with_multiple_characters(self, mock_stdout):
        # Arrange
        input_letters = [
            'zzzzz',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert re.match('You can only input one letter at a time!', mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_you_must_input_a_letter_for_non_alpha_input(self, mock_stdout):
        # Arrange
        input_letters = [
            '3',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert re.match('You must input a letter!', mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_valid_input_the_1st_time_it_just_returns_the_input(self, mock_stdout):
        # Arrange
        input_letters = ['a']
        correct_guesses_list = ['b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert answer == input_letters[0]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_works_with_empty_lists(self, mock_stdout):
        # Arrange
        input_letters = ['a']
        correct_guesses_list = []
        wrong_list = []
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        assert answer == input_letters[0]

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
##### !explanation


A sample solution could be:

```python
def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string
```

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

## Using Lists to Improve Readability and Simplify Code

In the last lesson we wrote the function `print_snowman_graphic` that drew our snowman up to the height that corresponded to the number of incorrect guesses.  The code for that function was fairly long because our graphic was broken up into seven constants.  We will use a list to simplify and streamline this code.

The first step is to store all of the drawing constants in a list:

```python

SNOWMAN_GRAPHIC = ['*   *   *  ', ' *   _ *   ', '   _[_]_ * ', '  * (")    ', '  \( : )/ *', '* (_ : _)  ', '-----------']

```

The next step is to update our drawing function to use the list.  Here's the previous version:

```python

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

```

Now, instead of using SNOWMAN_1, we can use SNOWMAN_GRAPHIC[0], for SNOWMAN_2 we use SNOWMAN_GRAPHIC[1], and so on.  Reminder - the first index of a list is 0, not 1.  That means that for element number `x` in the list, the index will be `x - 1`.  Let's update our code to use this new way of accessing each element of the graphic:

```python

def print_snowman_graphic(wrong_guesses_count):
    
    for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count, SNOWMAN_WRONG_GUESSES + 1)
        print(SNOWMAN_GRAPHIC[i - 1])

```

Notice in the above code that we have `+ 1` and `- 1`.  This is because in the first version if we wanted to draw the whole snowman we needed the math to produce the sequence 1 to 7 becuase we were using the numbers 1-7 in our constants and this made the code easier to read.  Now, we're using a list, so to draw the whole snowman we need the sequence to be 0 to 6.  We can now simplify some of our math with that in mind.

```python

def print_snowman_graphic(wrong_guesses_count):
    
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES)
        print(SNOWMAN_GRAPHIC[i])

```

## Summary

Lists are powerful tools!  Being able to add data to a list and access all of the elements of the list means that one variable can do the work of many variables.  Pairing lists with tools like loops allows us to do complex operations with just a few concise lines of code.  