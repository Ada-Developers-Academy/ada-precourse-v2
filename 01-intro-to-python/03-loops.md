# Loops

## Learning Goals

At the end of this lesson students will be able to:

- Understand and use `while` loops
- Understand and use `for` loops

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1m9h053kS6bjAeiHnEHIP39fqbyOO7glc?usp=sharing)

In this section we will be building on the code that you wrote in the previous lesson [Functions](02-functions.md).  If you would like to look at our example code version for that lesson, you can find it [here](resources/src/02-functions/games_function.md).  

## Vocabulary and Syntax

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| while loop|  A loop that repeats a code block inside it as long as a boolean conditional statement is true.  The statement is tested before executing the code block inside loop. | pre-test loop | "The code in the while loop will run until the test is false." |
| for loop| A loop that _iterates_ or repeats over a sequence.  In python it is often used to iterate over a `list` data structure.  It is also commonly paired with the `range` function[link to range function], which returns a list of numbers.  The `for` loop repeats n times, where n is the length of the sequence being looped over. | iterate | "To repeat the code five times we will use a for loop." |
| flag | A variable that is used to indicate that a condition has been met.  Usually a flag is a boolean variable and the value is changed to indicate that the goal or target (whatever the condition is) has been achieved. | signal | "The while loop will stop when the flag is changed." |


```python

# while loop
test = 0
while test < 10:
    test = test + 2
    print(f"The value of test is {test}")

# When run, this code chunk will output:
# The value of test is 2
# The value of test is 4
# The value of test is 6
# The value of test is 8

# for loop
for num in range(3):
    print(f"The value of num is {num}")

# When run, this code chunk will output:
# The value of num is 0
# The value of num is 1
# the value of num is 2

for num in range(2, 5):
    print(f"The value of num is {num}")

# When run, this code chunk will output:
# The value of num is 2
# The value of num is 3
# the value of num is 4

# flag example
flag_var = True
counter = 0
while flag_var:
    counter = counter + 3
    if(counter > 10):
        flag_var = False
    print(f"The value of counter is {counter}")

# When run, this code chunk will output:
# The value of num is 3
# The value of num is 6
# the value of num is 9
# the value of num is 12

```

## Guess The Number

### Validating User input

In the previous lesson, we pulled the user input into it's own function, while acknowledging that we weren't actually doing the work of validating the input.  We let the user know that the input is not good, but then we just return it:

```python

def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input

```

What we really want to do in this function is to compel the user to give us valid input, and only return our input when it is valid.  We can't really force the user to give us valid input, but what we can do is repeat the process of asking for input until we get something that is valid (or just keep asking forever).  In cases like this, where we need to repeat a process but there is uncertainty about how many times we will do so, a while loop is the ideal tool to use.  

To solve this problem we are going to use a flag controlled while loop.  A "flag" is a term for a boolean variable that is set before we enter the loop, and then at some point will be flipped inside the loop to signal that the loop should end (and that the whatever action the loop was trying to accomplish has been completed).  

<details>
<summary>Add a while loop with a flag to the get_number_from_user function to continue to loop until the user gives valid input.  Once you have finished, click here to compare your solution to ours</summary>

```python

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

```

Notice that our solution uses a not in the while test.  We could use a flag that is set it to true, and then when we get valid input set it to false.  Think about the readability of our code in that case.  It would not make sense to have a variable named valid_input set to true, if we are trying to get a valid input at the end (starting true then setting to false makes it seem like we're not getting valid input).  Changing the variable name to something like `attempting_valid_input` would work better to make the code readable.  In that case, the code would look like this:

```python

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

```

**As an aside, variable names can make or break the readability of code!**

</details>

### Keep The Guessing Game Going!

Now that we have a way to get valid input from the user, it's time to take a look at the guess_the_number function.  There are two ways to play this type of guessing game, the first is with unlimited guesses and the second is with a max number of guesses.  Let's start with the first version with unlimited guesses.  The current version of the function is:

```python
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


```

Add a while loop with a flag that tests to see if the user has guessed the correct number.

<details>
<summary>When you are finished, compare your code to our version here</summary>

```python

def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    waiting_for_correct_guess = True
    while waiting_for_correct_guess:
        user_input = get_number_from_user()
        
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")    
        elif user_input == random_number:
            print("You guessed the number!  Good job!")
            waiting_for_correct_guess = False
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")
        
```

</details>

Now let's work on the version with a maximum number of guesses.  At first glance this seems like a good candidate for a for loop because we have a max number of times we're going to run the loop, but let's dig into the actual sequence.  

We want to run the loop at most the max guesses number of times, but if the user guesses the number correctly we want to end the loop early.  In this case, a more complex while loop conditional statement along with a counter variable will result in a loop that does exactly what we want and also is easy to read and understand.  

1.  Start by adding a counter variable `num_guesses` and increment inside of the while loop:

    ```python

    def guess_the_number():
        # ...
        num_guesses = 0
        while waiting_for_correct_guess:
            # if the += operator is unfamiliar, 
            # it is the same as num_guesses = num_guesses + 1
            num_guesses += 1 
            # ...

    ```

1.  Next, add a max guesses constant to the other constants at the top of the file and set it to any integer value (in our example we will use 20.)  Then add a comparision in the while loop to check to see if the current number of guesses is greater than or equal to the max guesses (on our first time through the loop the number of guesses starts at 0, so by the time we get to the max number of guesses we've already guessed that many times):


    ```python

    # ...
    MAX_GUESSES = 20
    # ...
    def guess_the_number():
        # ...
        
        num_guesses = 0
        while (waiting_for_correct_guess or 
                   num_guesses <= MAX_GUESSES):
            num_guesses += 1 
            # ...

    ```

1.  Last, let's add some feedback to the user to let them know what's going on!

    ```python

    MAX_GUESSES = 20

    def guess_the_number():
        random_number = random.randint(RANGE_LOW, RANGE_HIGH)

        waiting_for_correct_guess = True
        num_guesses = 0
            while (waiting_for_correct_guess or
                    num_guesses <= MAX_GUESSES):
                num_guesses += 1 
            num_guesses += 1
            user_input = get_number_from_user()
            if user_input == random_number:
                print("You guessed the number!  Good job!")
                waiting_for_correct_guess = False
            elif user_input > random_number:
                print("Your guess is too high")
            elif user_input < random_number:
                print("Your guess is too low")
            elif user_input < RANGE_LOW or user_input > RANGE_HIGH:
                print(f"Your guess is out of bounds.")
                print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        
        # At this point, there are two options.  
        #    1, the user ran out of guesses or 
        #    2. they got the correct answer.  
        # We need to let them know if they ran out of guesses, 
        # but if we check if num_guesses is >= MAX_GUESSES we could
        # be wrong, because they might have gotten the correct answer 
        # on the last try!  If we check waiting_for_correct_guess
        # we will get the answer we want - did they ever guess the 
        # correct answer before they were booted out of the loop.  Also, if they
        # got the correct answer, they were given feedback about that 
        # inside the loop, so there's no need to do anything here in that case.
        if waiting_for_correct_guess:
            print(f"You ran out of guesses!  The correct answer \
was {random_number}.")

    ```

    Check the last assumption that we made that we only need to check `waiting_for_correct_guess` to give the user the "You ran out of guesses" feedback.  It seems like we're checking the wrong variable!  In cases like this it can be useful to "be the computer" and run through the code manually.  Write down the state of the variables at each pass through the loop and make sure that the loop is doing what we think it is doing.  Does the waiting_for_correct_guess variable give us the information that we think it does in every situation?  Walk through the code with various possibilities (we call these test cases, a possible list is first, the user guesses correctly, second, the user doesn't guess and runs out of guesses, and last, the user guesses correctly on the last try) and confirm that the code works.

### Guess the Number is Done..?

You have built a fully functional command line game!  If this is the first time you've done something like this, congratulations!  Go bug everybody you know and make them play it!  We will not be expanding the game further in these lessons, but if you are looking for a project to work on, this game can be a great jumping off point.  Consider adding options for the user to set the range for random number or the number of guesses.  What would be involved in turning it into a two player game where each player has a limited number of guesses?  

## Snowman

### Same Problem, New Context

In programming many problems that look different are at the core the same problem, just with different details.  We can use this to our advantage in our work!  If we identify that a problem is similar to one we have already solved, we can take the solution we've already written and modify it for the new problem.

We're going to switch now to working on Snowman.  First, let's take a look at the current version of our user input function `get_letter_from_user`:

```python

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")
    if not user_input_string.isalpha():
        print("You must input a letter!")
    elif len(user_input_string) > 1:
        print("You can only input one letter at a time!")

    return user_input_string

```

The problem here is the same as `get_number_from_user`, except instead of a number we want to continue to ask the user for a letter until they give us a single letter.  

<details>
<summary>Add a while loop to this function.  When you are finished compare your version with ours</summary>

```python

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

```
</details>

### Tracking User Input 

<!-- Loop Challenge -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: b10f595e-5a13-4f56-9f41-43ce92e08242
* title: Loops Exercise
### !question

Imagine we are playing a game of Snowman with a group of children.  We would probably keep track of the letters that they guessed, and with correct letters we would add to the word and with incorrect we would add to the snowman drawing.  In this version we are going to keep track of the number of correct and incorrect guesses from the user.  If the user guesses the same incorrect letter multiple times we'll count it as a new wrong guess every time.  

1.  Add a loop to the main snowman similar to the loop in `guess_the_word`.  
1.  Add two counters `correct_guesses` and `wrong_guesses`.
1.  Adjust the loop to allow the user to continue to guess until they reach `SNOWMAN_WRONG_GUESSES` wrong guesses.
1.  Track the number of correct and incorrect guesses, adding one to the proper counter when the user makes a guess.

When finished print out, "You made X correct and Y incorrect guesses" where X and Y are the number of correct and incorrect guesses.

Submit your code here:

### !end-question
### !placeholder
```python
SNOWMAN_WORD = "snowman"

SNOWMAN_WRONG_GUESSES = 7

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

def snowman():
    # Add code to repeat guesses until the total wrong guesses 
    # equals SNOWMAN_WRONG_GUESSES or number of correct guesses
    # equals the length of SNOWMAN_WORD.
    
    
```
### !end-placeholder
### !tests
```python
import sys
import unittest
import user_input
import io
from unittest.mock import patch
import re

from main import *

class TestChallenge(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_will_print_out_out_of_guesses_if_number_of_guesses_is_exhasted(self, mock_stdout):
        # Arrange
        input_letters = [
            'a',
            'z',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g'
            'h',
            'i',
            'j',
            'k'
        ]
        with unittest.mock.patch('builtins.input', side_effect=input_letters):
            # Act
            snowman()

        # Assert
        assert re.match(f"You made 1 correct and {SNOWMAN_WRONG_GUESSES} incorrect guesses",
                        mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_will_repeat_until_guesses_exhasted_even_if_word_guessed(self, mock_stdout):
        # Arrange
        input_letters = [
            's',
            'n',
            'o',
            'w',
            'm',
            'a',
            'n',
            'b'
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
        ]
        with unittest.mock.patch('builtins.input', side_effect=input_letters):
            # Act
            snowman()

        # Assert
        assert re.match(f"You made 7 correct and {SNOWMAN_WRONG_GUESSES} incorrect guesses",
                        mock_stdout.getvalue(), flags=re.IGNORECASE)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_will_will_output_0_correct_for_all_invalid_guesses(self, mock_stdout):
        # Arrange
        input_letters = [
            'b'
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
        ]
        with unittest.mock.patch('builtins.input', side_effect=input_letters):
            # Act
            snowman()

        # Assert
        assert re.match(f"You made 0 correct and {SNOWMAN_WRONG_GUESSES} incorrect guesses",
                        mock_stdout.getvalue(), flags=re.IGNORECASE)

```
### !end-tests
### !explanation
An example of a working implementation:
```python
SNOWMAN_WORD = "snowman"

# Add a constant SNOWMAN_WRONG_GUESSES here
SNOWMAN_WRONG_GUESSES = 7

def snowman():
    correct_guesses = 0
    wrong_guesses = 0
    while (wrong_guesses < SNOWMAN_WRONG_GUESSES):
        guessed_letter = input('Please enter a letter')
        if (guessed_letter in SNOWMAN_WORD):
            correct_guesses += 1
        else:
            wrong_guesses += 1
    
    print(f"You made {correct_guesses} correct and {wrong_guesses} incorrect guesses")

```
### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### Drawing Pictures

Add these ASCII snowman drawing constants to the top of the file.  Notice that the number of elements in the drawing is the same as SNOWMAN_WRONG_GUESSES.  For each wrong guess, we will want to add a new element to the drawing:

```python

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'

```

Our end goal is to have a function that we can pass the current `wrong_count` value to and it will draw the appropriate amount of the snowman.  Let's start by writing a function which will draw a specific element of the snowman based on a passed value.  For example, if we pass the function 7, we want the function to draw SNOWMAN_7.  This will seem slightly contrived, but it is just a starting place.  

<details>
<summary>Once you've written the function, compare what you have to our version.</summary>

```python

def print_snowman_graphic(id): 
    if id == 1:
        print(SNOWMAN_1)
    elif id == 2:
        print(SNOWMAN_2)
    elif id == 3:
        print(SNOWMAN_3)
    elif id == 4:
        print(SNOWMAN_4)
    elif id == 5:
        print(SNOWMAN_5)
    elif id == 6:
        print(SNOWMAN_6)
    elif id == 7:
        print(SNOWMAN_7)

```
</details>

Now we're going to add a loop inside this function to make it draw not just one element of the snowman, but all of the elements.  Unlike all of our other loops so far, we're not going to use a `while` loop, this time we're going to use a `for` loop.  A `for` loop is a great tool when we know exactly how many times we're going to be executing our loop.  

1. Start by adding a `for` loop that prints the entire snowman.  
    * Use the `range()` function with the `for` loop.  
    * With the `range()` function, remember that the number of items in the drawing is the same as the constant SNOWMAN_WRONG_GUESSES.  

    *Warning* the range function is _exclusive_, which means it goes up to but does not include the last element of the given range.  This means that `range(2, 7) = [2, 3, 4, 5, 6]`

    <details>
    <summary>When you have added the `for` loop to the function, compare what you have to our version.</summary>

    ```python

    def print_snowman_graphic():
        
        for i in range(1, SNOWMAN_WRONG_GUESSES + 1)
            if i == 1:
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
            elif i == 7:
                print(SNOWMAN_7)

    ```

    </details>

1. The next step is to modify the range of our for loop to only print the elements that we want.  For Snowman, we want to draw our snowman from the ground up, so if we have only 1 incorrect guess, we want to print the last element, 2 incorrect guesses means the last two elements, and so on.  Our function should take in the number of incorrect guesses and use that value in the range to draw the elements of the snowman in the order that we want.  

    <details>
    <summary> When you have updated the your function, compare what you have to our version.</summary>

    ```python

    def print_snowman_graphic(wrong_guesses_count):
        
        for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count, SNOWMAN_WRONG_GUESSES + 1)
            if i == 1:
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
            elif i == 7:
                print(SNOWMAN_7)

    ```

    </details>

1. Finally, inside of the `snowman` function, add the `print_snowman_graphic` function call to the game loop to print out the current state of the snowman to the user after each guess.

    ```python

    def snowman():
        correct_guesses = 0
        wrong_guesses = 0
        while wrong_guesses < SNOWMAN_WRONG_GUESSES:
            user_input = get_letter_from_user()
            if user_input in SNOWMAN_WORD:
                print("You guessed a letter that's in the word!")
                correct_guesses += 1
            else:
                print(f"The letter {user_input} is not in the word")
                wrong_guesses += 1
            print_snowman_graphic(wrong_guesses)
    ```

## Summary

Loops are incredibly powerful.  By adding a few loops we have transformed our Guess the Number code into a fully functional game!  We have also added core functionality to Snowman.  In the next lesson we will use the `list` data structure to add functinality to our Snowman game. 
