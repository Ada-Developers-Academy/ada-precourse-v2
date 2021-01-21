# Functions

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=9d7fa1b5-2551-4a68-934d-acb701843534&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson we will be able to:

- Understand and use functions

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1e8CaljqZrKJyFm7Ry5qHynp7GdoVHFLk?usp=sharing)

In this section we will be building on the code that you wrote in the previous lesson [Conditionals](./01-conditionals.md).  If you would like to look at our example code version for that lesson, you can find it [here](resources/src/01-conditionals/games_conditional.md)

## What is a Function?

* **function**: a named chunk of code that is callable and performs a task.  Functions can take in values called arguments and can have a return value.  

```python

# This line defines the new function and assigns it a name
def my_new_function():
    # code block here
    # note that each line is indented 
    # compared to the definition
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

### Why Functions?

In the last lesson we wrote a series of conditionals to validate and test user input for the "Guess the Number" game.  At this point, we may be looking at the code and thinking, this looks good, it works, why add functions?  

Lets say we want to play a different game after we finish playing Guess the Number.  We could just add the code for the new game after the code that's in the file right now, but then what if we want to change the order of the games?  

We're now looking at moving around big code blocks.  Then if we change our minds and want to move it back, or add another game (and so on) things quickly get messy.  Functions encapsulate code blocks into re-usable chunks that we can then call in whatever order we want.  They also help us reuse these blocks of code in other programs.

## Guess the Number



Lets build a "Guess the number" function.  This function will:

1.  Read in a number from the user
1.  If the user entered a number:
    1.  Inform the user if their number is lower or higher than the random number at the top of the code above:
1.  Otherwise if the user entered a non-number, tell them it wasn't a number

Lets write this code and place it in a function called `guess_the_number`.  Then call the function at the bottom of the file.

Try writing this in VS code and then compare your answer to ours below.

<details>
<summary> Our version at this point </summary>

```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)


def guess_the_number():
    user_input_string = input("Guess the number: ")
    user_input = None

    if user_input_string.isnumeric():
        user_input = int(user_input_string)

        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number!  Good job!")
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")
        
    else:
        print("You must input a number!")

guess_the_number()

```

</details>

## Helper Functions

A helper function is a function that does part of the work for another function.  They make our code easier to read by breaking long functions up into smaller pieces.  We recommend giving helper functions descriptive names, to help with readability.

Imagine we want to build a tool that will convert a temperature in fahrenheit to celsius, and a temperature in celsius to fahrenheit. There are two different rules that the temperature converter must know about. It would be reasonable to place these conversion formulas into two separate helper functions `convert_to_celsius` and `convert_to_fahrenheit`.

```python

def convert_to_fahrenheit(temp):
    return 9/5*temp + 32

def convert_to_celsius(temp):
    return 5/9*(temp-32)

```

Then, we could write another function `temp_converter` that takes the temperature and the unit of measurement as parameters, and calls `convert_to_celsius` or `convert_to_fahrenheit` depending on the unit.

```python

def temp_converter(temp, unit)
    if unit == "fahrenheit":
           return convert_to_celsius(temp)
   elif unit == "celsius"
           return convert_to_fahrenheit(temp)

```

### The `return` Keyword

Notice the `return` keyword in the functions above.  This means that these functions calculate a value and return it to the calling function.

So:

```py
fahrenheit_temp = convert_to_fahrenheit(100)
print(f"The temp is 212.0 degrees fahrenheit")
```

Will print "The temp is  degrees fahrenheit".  This way you can call a function and get a value or an answer sent back after the function completes.  We can use this to simplify `guess_the_number`.


## Exercise:  Breaking Up `guess_the_number`

The function `guess_the_number` can be broken up into two conceptual pieces, getting user input, and then processing the user input.  

1.  Start by writing a function called `get_number_from_user`
    * Then pull all of the pieces of code in `guess_the_number` that have to do with getting user input into `get_number_from_user`.  
    * Include any conditional statement that validate user input as a number.  
    * This function should ask the user for a number and then give an error message if the user inputs anything other than a number.  
    * Last, it should return the valid user input, or None if there was no valid input.  
    * In `guess_the_number`, call this function and store the result in user_input.
1.  Then the `guess_the_number` function can use the previous `if...else` statements to tell the user if their guess was too high or too low.
 
<details>
<summary> Our version at this point </summary>

```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)


def guess_the_number():

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


def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input

# Run the guess_the_number function to test it
guess_the_number()
```
</details>

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-secondary

## Each Function Does **One** Thing!

Notice in our code that now each function is doing exactly **one** thing.  `get_number_from_user` does just that, it reads in a number from the user.  Similarly `guess_the_number` now just processes the user's guess.  This makes each step *much* easier to read and test.

### !end-callout

### !callout-info

## None and potential Errors

Notice that in our version, if the user does not give a valid input, the return value will be `None`.  This will cause an error in the conditionals in `guess_the_number`, because `None` can not be compared to a number.  That's ok, we're building to a full solution.  Many times when writing code, it is useful to write and test a small portion, and then when we're confident that it works, moving on to build the next portion.

### !end-callout

## Snowman!

It's time to add a new game!  The new game is a word guessing game called Snowman.  

In Snowman:

1.  The user is presented with a list of underscores "_".  Each Underscore represents one letter in a word.
1.  The user guesses letters for the hidden word
    * For each correct guess, a letter will be replace the corresponding underscore.
    * For every wrong guess we are going to remember the number of wrong guesses and print out more and more of a snowman drawing.  
1.  When the snowman is finished and the user is out of guesses, they lose the game.  

We are going to start by building just a small piece of this game.  To start, for debugging purposes, we're always going to use the same word.  Add it as a constant at the top of the file.  Here's our version:

```python

SNOWMAN_WORD = "broccoli"

```

### Step 1:  Guess a letter

We will start our game by reading in a letter from the user, similar to how we read in numbers with `guess_the_number`.  We will call this function `get_letter_from_user`.

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
1.  Second, we need to check to see if the input is valid.  
    * In `get_number_from_user`, we used `isnumeric()` to ensure that the input was a number.  In this function, we need to check to see if the input is a letter, and if the input contains only one letter.
      - `letter_from_user.isalpha()` will return `True` if the string variable `letter_from_user` contains only alphabetical characters
      - `len(letter_from_user)` will tell us the length of the string
2. Lastly, we need to return the input string
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
    # Your code goes here
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
* title: snowman
* points: 1
* topics: python

##### !question

We are now going to work on the main `snowman` function (the function we will call when we want to play the game Snowman).  This function is structurally similar to `guess_the_number`, but will be shorter for now.  

The only check we have to do on the letter is check if it's in the word or not.  To do that, we're going to use the python keyword `in`.  The syntax for `in` is `thing1 in thing2`.  This expression evaluates to `True` if `thing2` contains `thing1`, and false otherwise.  We can use it in a conditional expression as `if thing1 in thing2:`.

1.  First, use `get_letter_from_user` to get a letter
1.  Check if the letter is in `SNOWMAN_WORD` 
    - print "Letter found" if the letter is in `SNOWMAN_WORD`.
    - print "Letter not found" if it's not in `SNOWMAN_WORD`.
1.  If the letter is in `SNOWMAN_WORD` return `True` otherwise return `False` if it's not in `SNOWMAN_WORD`.

##### !end-question

##### !placeholder

```py
SNOWMAN_WORD = "pasta"

def get_letter_from_user():
    letter = input("Please enter a letter > ")
    if len(letter) > 1 or not letter.isalpha():
        print("Invalid letter please enter a single character.")
    
    return letter


def snowman():
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
            answer = p.snowman()

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
            answer = p.snowman()

        # Assert
        assert re.match('Letter found', mock_stdout.getvalue(), flags=re.IGNORECASE)
        assert answer # True if it's in the snowman word

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_p_four(self, mock_stdout):
        # Arrange
        input_letter = "e"
        with unittest.mock.patch('builtins.input', return_value=input_letter):
            # Act
            answer = p.snowman()

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

Let's go back to the questions proposed in the introduction to this lesson.  What do functions add to our code?  

Now that we have broken the various sections into functions, we can easily swap the order of the games, play a game multiple times, or add new games in new functions and insert them in any order we want.  

Functions add flexibility and structure to our code, and make code easier to maintain and read.  In the next lesson we will work on adding more functionality to our functions with loops. 
