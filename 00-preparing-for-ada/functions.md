# Functions

## Learning Goals

At the end of this lesson students will be able to:

- Understand and use functions

## Introduction

### Textbook for this section: [link to ada build functions]

In this section we will be building on the code that you wrote in the previous lesson [Conditionals].  If you would like to look at our example code version for that lesson, you can find it [here]

### Why Functions?

In the last lesson you a series of conditionals to validate and test user input for the "Guess the Number" game.  You may be looking at the code and think, this looks good, it works, why add functions?  Lets say we want to play a different game after we finish playing Guess the Number.  We could just add the code for the new game after the code that's in the file right now, but then what if we want to change the order of the games?  We're now looking at moving around big code blocks.  Then if we change our minds and want to move it back, or add another game (and so on) things quickly get messy.  Functions encapsulate code blocks into re-usable chunks that we can then call in whatever order we want.  

## Vocabulary

* function: a named chunk of code that is callable and performs a task.  Functions can take in values called arguments and can have a return value.  

```python

# This line defines the new function and assigns it a name
def my_new_function:
    # code block here
    # note that each line is indented compared to the definition
    x = 1
    y = 2
    z = x + y

# This line calls the function
my_new_function()


# Example function with arguments
def my_func_with_args(arg1, arg2):
    x = arg1
    y = arg2

# Calling the function with arguments
my_func_with_args(1, 2)

```

## Guess the Number

Start by taking all of the code (excluding the import statement at the top of the file and the constant declarations) and place it in a function called `guess_the_number`.  Then call the function at the bottom of the file


<details>
<summary> Our version at this point </summary>
```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100

def guess_the_number:

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)

    user_input_string = input("Guess the number: ")
    user_input = None

    if user_input_string.isnumeric():
        user_input = int(user_input_string)
        if user_input == random_number:
            print("You guessed the number!  Good job!")
        if user_input > random_number:
            print("Your guess is too high")
        if user_input < random_number:
            print("Your guess is too low")
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")
    else:
        print("You must input a number!")

guess_the_number()

```
</details>

## Helper Functions

A helper function is a function that does part of the work for another function.  They make your code easier to read by breaking long functions up into smaller pieces.  We recommend giving your helper functions descriptive names, to help with readability.

The function `guess_the_number` can be broken up into two conceptual pieces, getting user input, and then processing the user input.  Start by writing a function called `get_number_from_user` and then pull all of the pieces of code in `guess_the_number` that have to do with getting user input into `get_number_from_user`.  Include any conditional statement that validate user input as a number.  This function should ask the user for a number and then give an error message if the user inputs anything other than a number.  Last, it should return the valid user input, or None if there was no valid input.  In `guess_the_number`, call this function and store the result in user_input.

<details>
<summary> Our version at this point </summary>
```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100

def guess_the_number():

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)

    user_input = get_number_from_user()
        
    if user_input == random_number:
        print("You guessed the number!  Good job!")
    if user_input > random_number:
        print("Your guess is too high")
    if user_input < random_number:
        print("Your guess is too low")
    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")
        

def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input

```
</details>

### !callout-info

## None and potential Errors

Notice that in our version, if the user does not give a valid input, the return value will be None.  This will cause an error in the conditionals in `guess_the_number`, because None can not be compared to a number.  That's ok, we're building to a full solution.  Many times when writing code, it is useful to write and test a small portion, and then when you're confident that it works, moving on to build the next portion.

### !end-callout

## Snowman!

It's time to add a new game!  The new game is a word guessing game called Snowman.  In Snowman, the user guesses letters for a word, but for every wrong guess we are going to add a new element to our snowman.  When the snowman is finished, the user is out of guesses and they lose the game.  We are going to start by building just a small piece of this game.  To start, for debugging purposes, we're always going to use the same word.  Add it as a constant at the top of your file.  Here's our version:

```python

SNOWMAN_WORD = "broccoli"

```

Next, we're going to follow the same pattern as `guess_the_number`.  We will start with a function named `snowman` and a helper function `get_letter_from_user`.  

###  get_letter_from_user

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: c751d441-f566-4ab7-acc1-390b8710213e
* title: get_letter_from_user
* points: 1
* topics: python, python-functions

##### !question

This function is very similar to `get_number_from_user`.  

1.  First, we will need to use `input` to get a string from the user and store it in a variable.  
1.  Second, we need to check to see if the input is valid.  In `get_number_from_user`, we used isnumeric() to ensure that the input was a number.  In this function, we need to check to see if the input is a letter, and if the input contains only one letter.  Use the functions below to write these conditionals:
    - [string variable name].isalpha() will return true if the string contains only alphabetical characters
    - len([string variable name]) will tell us the length of the string
1. Lastly, we need to return the input string
    - If the user gives bad input: 
      - We print "Invalid letter please enter a single character." 
      - Then return the input.  
    - If the user gives valid input:
      - Then we just return the input.

We will expand this to a full solution in the next lesson.


##### !end-question

##### !placeholder

```py
def get_letter_from_user():
  
#   return 1
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

class TestPython1(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_one(self, mock_stdout):
        # Arrange
        input_letter = "a"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.get_letter_from_user()

        # Assert
        assert re.match('', mock_stdout.getvalue())
        assert answer == input_letter


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_two(self, mock_stdout):
        # Arrange
        input_letter = "!"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.get_letter_from_user()

        # Assert
        assert re.match('invalid letter please enter a single character', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer == input_letter

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_three(self, mock_stdout):
        # Arrange
        input_letter = "223"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.get_letter_from_user()

        # Assert
        assert re.match('Invalid letter please enter a single character.', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer == input_letter

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_four(self, mock_stdout):
        # Arrange
        input_letter = "z"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.get_letter_from_user()

        # Assert
        assert re.match('', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer == input_letter

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->


### snowman

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 2604b524-92e8-43fb-adc3-de4b29f0b451
* title: letter_in_snowman_word
* points: 1
* topics: python

##### !question

We are now going to work on the main `snowman` function (the function we will call when we want to play the game Snowman).  This function is structurally similar to `guess_the_number`, but will be shorter for now.  The only check we have to do on the letter is check if it's in the word or not.  To do that, we're going to use the python keyword `in`.  The syntax for `in` is `thing1 in thing2`.  This expression evaluates to `True` if thing2 contains thing1, and false otherwise.  We can use it in a conditional expression as `if thing1 in thing2:`.

1.  First, use `get_letter_from_user` to get a letter
2.  Check if the letter is in `SNOWMAN_WORD` 
    - print "Letter found" if the letter is in `SNOWMAN_WORD`.
    - print "Letter not found" if it's not in `SNOWMAN_WORD`.
3.  If the letter is in `SNOWMAN_WORD` return `True` otherwise return `False` if it's not in `SNOWMAN_WORD`.

##### !end-question

##### !placeholder

```py

SNOWMAN_WORD = "pasta"

def get_letter_from_user():
    letter = input("Please enter a letter > ")
    if (len(letter) > 1 or not letter.isalpha()):
        print("Invalid letter please enter a single character.")
    
    return letter


def letter_in_snowman_word():
    # Your code is here

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

class TestPython2(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_one(self, mock_stdout):
        # Arrange
        input_letter = "a"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.letter_in_snowman_word()

        # Assert
        assert re.match('Letter found', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer # True if it's in the snowman word


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_two(self, mock_stdout):
        # Arrange
        input_letter = "z"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.snowman()

        # Assert
        assert re.match('Letter not found', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer == False
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_three(self, mock_stdout):
        # Arrange
        input_letter = "p"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.letter_in_snowman_word()

        # Assert
        assert re.match('Letter found', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer # True if it's in the snowman word

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_four(self, mock_stdout):
        # Arrange
        input_letter = "e"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.letter_in_snowman_word()

        # Assert
        assert re.match('Letter not found', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer == False

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->
## Summary

Let's go back to the questions proposed in the introduction to this lesson.  What do functions add to our code?  Now that you have broken the various sections into functions, you can easily swap the order of the games, play a game multiple times, or add new games in new functions and insert them in any order you want.  Functions add flexibility and structure to our code, and make code easier to maintain and read.  In the next lesson we will work on adding more functionality to our functions with loops. 
