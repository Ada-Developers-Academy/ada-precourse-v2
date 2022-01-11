# Functions

## Learning Goals

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=e6e5f787-22a4-4ab5-a8ee-ad65007aa519&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

At the end of this lesson we will be able to:

- Define functions
- Return values from functions
- Call functions

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1e8CaljqZrKJyFm7Ry5qHynp7GdoVHFLk?usp=sharing)

In this section we will be building on the code that you wrote in the previous lesson [Conditionals](./02-conditionals.md).  If you would like to look at our example code version for that lesson, you can find it [here](resources/src/01-conditionals/games_conditional.md)

## What is a Function?

* **Function**: a named chunk of code that is callable and performs a task. 

Functions must be defined in order to be invoked. A function definition contains a signature and a body. Function signatures are comprised of 2 parts: the name and parameters. In the function signature, `def` indicates the start of the function definition followed by its name. The parenthesis of a function signature may contain zero or more parameters that represent pieces of data to be provided as input(s).  

```Python
# Start Function Signature
def function_name(some_paramater, another_parameter): # End of Function Signature
    # Start of Function Body
    print(some_parameter, another_parameter)
    # End of Function Body
```

There are a variety of ways to describe 'using a function' such as '*calling* a function', '*invoking* a function', '*executing* a function', etc. All of these phrases describe the same action of "performing the code inside this function". (For consistency, **call** will be used throughout this lesson). To call a function, all that needs to be provided are the function name and arguments (values to be passed into the function). 

```Python
function_name(some_argument, another_argument)
```

Here are additional examples:

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

We're now looking at moving around big code blocks.  Then if we change our minds and want to move it back, or add another game (and so on) things quickly get messy.  

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Why Functions?
Functions encapsulate code blocks into re-usable chunks that we can then call in whatever order we want.  They also help us reuse these blocks of code in other programs.

### !end-callout

## Guess the Number

Let's start working with functions by adding a "Guess the number" function to our `Guess the Number` project.  Open up your `game.py` in VSCode and let's jump right in!

The "Guess the number" function will:

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




### The `return` Keyword

Functions can be designed to either return a specific value or execute blocks of code without returning a value. For the former, functions with a `return` keyword will return a value or data structure to its calling function. The `return` keyword ends the execution of the function. We will sometimes hear it referred to as "returning out of the function."

#### Return values and Variables 

Because functions can return a value, they're often used in variable assignments. In each of the example below, and subsequnt examples, we will store the return value of the function in a variable `result` and then print the value of `result`. This will allow us to analyze the behavior and the return value of each function.

```Python
# an example function that returns a value
def greeting():
    return "Hello"

result = greeting()
print(result) # "hello"
```

If we don't provide a value after `return`, the function will return `None`. Furthermore, without the `return` keyword, a function will execute the function body and then return `None`. We can demonstrate the values below by using `print()` which will execute the function call and then return `None`. 

```Python
# an example function that prints Goodbye 
# and returns None (implicit return)
def farewell():
    print("Goodbye")

result = farewell() # prints "Goodbye"
print(result) # None
```

Sometimes we will want to write a function that returns `None`. In this case, it is best practice to explicitly return `None` rather than rely on Python's default behavior. This is especially true if we return non-`None` values elsewhere in the function, as the omission of the explicit `return None` looks like an oversight.

```Python
# an example function that returns a temperature converted to fahrenheit 
# for numeric arguments and returns None for non-numeric arguments.
def convert_to_fahrenheit(temp):
    if not isinstance(temp, int) / and not isinstance(temp, float):
        return None

    return 9/5*temp_in_celsius+32

result = convert_to_fahrenheit(0)
print(result) # 32

result = convert_to_fahrenheit("non numeric value")
print(result) # None
```

## Practice Problems

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 16e0108f-727f-43f7-a2a7-3561f4368239
* title: Compare Two Items
* points: 1
* topics: python, functions

##### !question

Write a function `compare` that takes two arguments, two numbers.  The function has the following behavior:
* If the first item is greater than the second, the function returns `True`.
* If the first argument is smaller or equal to the second, the function returns `False`.

Example inputs and outputs:

|input|output|
|--|--|
| `first = 3` <br/> `second = 7`|`False`|
| `first = 7` <br/> `second = 3`|`True`|
| `first = 7` <br/> `second = 7`|`False`|

##### !end-question

##### !placeholder

```python

def compare(first, second):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import compare


class TestCompare(unittest.TestCase):
    def test_less(self):
        self.assertEqual(compare(3, 7),False)

    def test_greater(self):
        self.assertEqual(compare(7, 3),True)

    def test_equal(self):
        self.assertEqual(compare(7, 7),False)

```
##### !end-tests

<!--optional-->
##### !explanation

A working implementation:

```python

def compare(first, second):
    if first > second:
        return True
    else:
        return False

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: aa042095-db32-442b-bbb3-a05da7a7616e
* title: Convert Miles to Kilometers
* points: 1
* topics: python, functions

##### !question

Write a function `convert_mi_to_km` that takes one argument, a number `miles`.  The function has the follwing behavior:
* The function converts the length in miles to kilometers and returns the length in kilometers.
* The formula for converting miles to kilometers is `miles * 1.6`.
* _The actual conversion rate is 1.609344 but for this problem please use 1.6._

Example inputs and outputs:

|input|output|
|--|--|
| `miles = 1` |`1.6`|
| `miles = 0` |`0`|
| `miles = 3.5` |`5.6`|

##### !end-question

##### !placeholder

```python

def convert_mi_to_km(miles):
    pass

```

##### !end-placeholder

##### !tests
```python

from main import convert_mi_to_km
import unittest


class TestConversion(unittest.TestCase):
    def test_one(self):
        self.assertAlmostEqual(convert_mi_to_km(1),1.6)

    def test_zero(self):
        self.assertAlmostEqual(convert_mi_to_km(0),0)

    def test_float(self):
        self.assertAlmostEqual(convert_mi_to_km(3.5),5.6)

```

##### !end-tests

<!--optional-->
##### !explanation

A working implementation:

```python

def convert_mi_to_km(miles):
    km = miles * 1.6
    return km

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman!

It's time to add a new game!  The new game is a word guessing game called Snowman.

Before getting started, create a new file in your precourse directory called `snowman.py` and open it in VSCode.

In Snowman:

1.  The user is presented with a list of underscores "_".  Each Underscore represents one letter in a word.
1.  The user guesses letters for the hidden word
    * For each correct guess, a letter will be replace the corresponding underscore.
    * For every wrong guess we are going to remember the number of wrong guesses and print out more and more of a snowman drawing.  
1.  When the snowman is finished and the user is out of guesses, they lose the game.  

We are going to start by building just a small piece of this game.  To start, for debugging purposes, we're always going to use the same word.  Add it as a constant at the top of the `snowman.py` file.  Here's our version:

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
