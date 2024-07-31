# Functions

## Learning Goals

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=e6e5f787-22a4-4ab5-a8ee-ad65007aa519&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

At the end of this lesson we will be able to:

- Define functions
- Return values from functions
- Call functions

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1e8CaljqZrKJyFm7Ry5qHynp7GdoVHFLk?usp=sharing)

In this section we will be building on the Guess the Number game that we wrote in the [Conditionals](./conditionals.md) lesson.  [Here](resources/src/conditionals/games_conditional.md) is an example solution to the game. 

## What is a Function?

* **Function**: a named block of code that encapsulates a specific task that can be invoked. 

Functions must be defined in order to be invoked. A function definition contains a signature and a body. Function signatures are comprised of 2 parts: the name and parameters. In the function signature, the `def` keyword indicates the start of the function definition followed by its name. The parenthesis of a function signature may contain zero or more parameters that represent pieces of data to be provided as input(s).  

```Python
# Start Function Signature
def function_name(some_parameter, another_parameter): # End of Function Signature
    # Start of Function Body
    print(some_parameter, another_parameter)
    # End of Function Body
```

There are a variety of ways to describe 'using a function' such as '*calling* a function', '*invoking* a function', '*executing* a function', etc. All of these phrases describe the same action of "executing the code inside this function". For consistency, **call** will be used throughout this lesson. To call a function, we need to provide the function name and the function's arguments (values to be passed into the function). 

```Python
function_name(some_argument, another_argument)
```

Here are additional examples:

```python

# This line defines the new function and assigns it a name
def my_new_function():
    # code block here
    # note that each line is indented compared to the definition
    x = 1
    y = 2
    sum = x + y
    print(sum)

# This line calls the function
my_new_function()


# Example function with arguments
def my_func_with_args(arg1, arg2):
    x = arg1
    y = arg2
    difference = arg1 - arg2
    print(difference)

# Calling the function with arguments
my_func_with_args(3, 2)

```

### Why Write and Use Functions?

In the "Conditionals" lesson we wrote a series of conditionals to validate and test user input for the "Guess the Number" game.  At this point, we may be looking at the code and thinking, "this looks good, it works, why do we need functions"?  

Imagine we'd like a user to be able to play the game more than once. Without functions, the code as it is currently written requires that we copy the logic every time a user plays the game. If we want to allow the user to play the game 5 times, then we would need to write the same block of code 5 times. 

### !callout-info

## Encapsulating Code With Functions
Functions encapsulate code blocks into re-usable chunks that we can call whenever we want and as many times as we want.  Functions enable us to avoid repeating code because we can invoke the function by name and and pass it data as arguments, instead of writing the same block of code again in another part of our program.

### !end-callout

## Guess the Number

Let's start working with functions by adding a `guess_the_number` function to our "Guess the Number" game.  Open up your `game.py` in VSCode and let's jump right in!

The "Guess the number" function will:

1.  Read in a number from the user
2.  If the user entered a number:
    1.  Inform the user if their number is lower, higher, or the same as the random number
3.  Otherwise if the user entered a non-number, tell them they need to enter a number

Lets write this code and place it in a function called `guess_the_number`.  Then call the function at the bottom of the file.

Try writing `guess_the_number` in VS code and then compare your answer to ours below.

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
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number! Good job!")
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")
        
    else:
        print("You must input a number!")

# invoke the function to play the game
guess_the_number()

```
</details>

Now that we have a `guess_the_number` function, we can call this function multiple times so that the user can play the game more than once.

Add multiple function calls in VS code, play the game, and then view our solution below.


<details>
<summary>Our version with multiple function calls</summary>

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
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number! Good job!")
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")
        
    else:
        print("You must input a number!")

guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()
```

</details>

With this example, we can see that calling a function allows us to run the same code multiple times without repeating a large block of code, which makes our code more concise.  This code could be even more concise by using a loop, which we'll cover in a future lesson.  Run `game.py` to play the Guess the Number game.

### The `return` Keyword

Functions can either be designed to return a specific value, or to execute blocks of code _without_ returning a value. For the former scenario, a function with a `return` keyword returns a value. The `return` keyword ends the execution of the function. This is referred to as "returning from the function," or "returning out of the function." 

#### Return values and Variables 

Because functions can return a value, they're often used in variable assignments. In the example below, and the other examples which follow, we will store the value returned by a function in a variable `result` and then print the value of `result`. This will allow us to analyze the behavior and the return value of each function.

```Python
# an example function that returns a value
def greeting():
    return "Hello"

result = greeting()
print(result) # "hello"
```

We can use `return` without providing it a value. This is usually done if we need to exit a function before reaching its end, but the function doesn't need to return a value. If we don't provide a value after `return`, the function implicitly returns `None`. Even if a function does not have the `return` keyword, a function will execute its function body and then implicitly return `None`. We can demonstrate this with the code below, which executes the function call and implicitly returns `None`. We then print the returned value, which displays `None`.

```Python
# an example function that prints Goodbye 
# and returns None (implicit return)
def farewell():
    print("Goodbye")

result = farewell() # prints "Goodbye"
print(result) # None
```

Sometimes we need to write a function that returns `None` under certain conditions. In this case, it is best practice to return `None` explicitly rather than rely on Python's default behavior. This is especially true if we return non-`None` values elsewhere in the function, as the omission of the explicit `return None` looks like an oversight.

```Python
# an example function that returns a temperature in celsius converted to fahrenheit 
# for numeric arguments and returns None for non-numeric arguments.
def convert_celsius_to_fahrenheit(temp):
    if not isinstance(temp, int) and not isinstance(temp, float):
        return None

    return 9 / 5 * temp + 32


result = convert_celsius_to_fahrenheit(0)
print(result) # 32

result = convert_celsius_to_fahrenheit("non numeric value")
print(result) # None
```

To further motivate using functions, let's review some example code that makes use of the `convert_celsius_to_fahrenheit` function. Note that by encapsulating the functionality of converting a temperature from Celsius to Fahrenheit in a function, we can call this function with different arguments. 

```Python
# Temperatures in Celsius
mumbai_temp = 28
tokyo_temp = 20
paris_temp = 21
madrid_temp = "madrid"

# Output temperature in Fahrenheit
print("The temperature in Mumbai is", convert_celsius_to_fahrenheit(mumbai_temp), "°F")
print("The temperature in Tokyo is", convert_celsius_to_fahrenheit(tokyo_temp), "°F")
print("The temperature in Paris is", convert_celsius_to_fahrenheit(paris_temp), "°F")
print("The temperature in Madrid is", convert_celsius_to_fahrenheit(madrid_temp), "°F")

# Output
# The temperature in Mumbai is 82.4 °F
# The temperature in Tokyo is 68.0 °F
# The temperature in Paris is 69.80000000000001 °F
# The temperature in Madrid is None °F
```

Expand the section below to look at the length of the code required if we did not write the function `convert_celsius_to_fahrenheit`. Notice the amount of repeated code. 

<details>
<summary>Code without a function</summary>

```Python
# Temperatures in Celsius
mumbai_temp = 28
tokyo_temp = 20
paris_temp = 21
madrid_temp = "madrid"

# Convert temperatures
if not isinstance(mumbai_temp, int) and not isinstance(mumbai_temp, float):
    mumbai_temp_fahrenheit = None
else: 
    mumbai_temp_fahrenheit = 9 / 5 * mumbai_temp + 32

if not isinstance(tokyo_temp, int) and not isinstance(tokyo_temp, float):
    tokyo_temp_fahrenheit = None
else: 
    tokyo_temp_fahrenheit = 9 / 5 * tokyo_temp + 32

if not isinstance(paris_temp, int) and not isinstance(paris_temp, float):
    paris_temp_fahrenheit = None
else: 
    paris_temp_fahrenheit = 9 / 5 * paris_temp + 32

if not isinstance(madrid_temp, int) and not isinstance(madrid_temp, float):
    madrid_temp_fahrenheit = None
else: 
    madrid_temp_fahrenheit = 9 / 5 * madrid_temp + 32


# Output temperature in Fahrenheit
print("The temperature in Mumbai is", mumbai_temp_fahrenheit, "°F")
print("The temperature in Tokyo is", tokyo_temp_fahrenheit, "°F")
print("The temperature in Paris is", paris_temp_fahrenheit, "°F")
print("The temperature in Madrid is", madrid_temp_fahrenheit, "°F")

# Output
# The temperature in Mumbai is 82.4 °F
# The temperature in Tokyo is 68.0 °F
# The temperature in Paris is 69.80000000000001 °F
# The temperature in Madrid is None °F
```

</details>

### !callout-info

## The DRY Principle

DRY stands for "Don’t Repeat Yourself" and it is a software development principle that aims to reduce code repetition. Less repeated code helps make our projects more readable and easier to maintain. If we find ourselves copy and pasting lines of code in our program, we should exam our code and see if we can write a function that we can call instead so that our code follows the DRY principle. <br>

<br>Functions are one of our most powerful tools for writing DRY code.

### !end-callout

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

Write a function `compare` that takes two arguments that are both integers.  The function has the following behavior:
* If the first argument is greater than the second, the function returns `True`.
* If the first argument is less than or equal to the second, the function returns `False`.

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
    return first > second
```

We could write an `if`/`else` statement, but remember, a comparison expression like `first > second` results in a `Boolean` value. If the function needs to return a `Boolean` result, there's no need for an extra conditional check. We should just return the `Boolean` created by the comparison!

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

Write a function `convert_mi_to_km` that takes one argument `miles`, which is an integer.  The function has the following behavior:
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
    return miles * 1.6

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman!

It's time to add a new game!  The new game is a word guessing game called Snowman.  We will run some commands in the terminal to set up this project.  At this moment, we will not go into detail about all the commands we need to run to set up a Python project, but rest assured that we will spend time going over project setup later in Unit 1.  For now, you can run the given commands and focus on writing the logic for the Snowman game.

### Snowman Setup

Before getting started, we'll want to make sure we're in our Precourse directory by running `pwd` in the terminal. We should see some output like `/ada/precourse`. 

To keep our projects organized, we usually create a unique folder for each project we work on. By running the following commands, one at a time, we will create a new directory in our Precourse directory called `snowman_project`, change directories so that we are in our newly created directory, and then create two files.

```sh
$ mkdir snowman_project
$ cd snowman_project
$ touch snowman.py requirements.txt
```

<!-- prettier-ignore-start -->
| Terminal Command | Notes |
| ------------- | ----- |
| `mkdir snowman_project` | Create a directory called `snowman_project` |
| `cd snowman_project` | Change the current working directory to be `snowman_project` |
| `touch snowman.py requirements.txt` | Create a file called `snowman.py` and another file called `requirements.txt`. At the moment we will only be using `snowman.py` and can ignore `requirements.txt` for now |
<!-- prettier-ignore-end -->

### Snowman Gameplay

In Snowman:

1.  The user is presented with a list of underscores "_".  Each Underscore represents one letter in a word.
1.  The user guesses letters for the hidden word 
    * For each correct guess, a letter will replace the corresponding underscore.
    * For every wrong guess we are going to remember the number of wrong guesses and print out more and more of a snowman drawing.  
2.  When the snowman is finished and the user is out of guesses, they lose the game.  

We are going to start by building just a small piece of this game.  To start, for debugging purposes, we're always going to use the same hidden word each time the game is played.  Open up the file `snowman.py` and add a constant variable that represents the hidden word to the file.  Here's our version:

```python

# Constant variable that references the hidden word 
SNOWMAN_WORD = "broccoli"

```

### Step 1:  Guess a letter

We will start our game by reading in a letter from the user, similar to how we read in numbers with `guess_the_number`.  We will call this function `get_letter_from_user`.

1.  First, we will need to use `input` to get a string from the user and store it in a variable.  
1.  Second, we need to check to see if the input is valid.  
    * In `guess_the_number`, we used `isnumeric()` to ensure that the input was a number.  In this function, we need to check to see if the input is a letter, and if the input contains only one letter.
      - If we have a variable which holds our input named `letter_from_user` then `letter_from_user.isalpha()` will return `True` if the string variable `letter_from_user` contains only alphabetical characters.
      - `len(letter_from_user)` will tell us the length of the string
1. Lastly, we need to return the input string
    - If the user gives bad input: 
      - We print "Invalid letter please enter a single character." 
      - Then return the input.  
    - If the user gives valid input:
      - Then we just return the input.

Use the outlined requirements for `get_letter_from_user` and write this function in `snowman.py`. After we've written our function we also need to call the function in order for Python to execute the logic we just wrote. Then, we can run the file with `python3 snowman.py` in the terminal to manually test that our code is working. 

We can add debugging print statements to our function so that we can see certain values in our terminal if our logic isn't working as expected. For example, if we are curious about what the length of the user input is, we could add `print (len(letter))` in our function. After we have debugged an issue, we should be sure to remove the debugging print statement so that our file doesn't become cluttered with debugging code.

<br/>

<details>
<summary>Once you've written <code>get_letter_from_user</code>, compare what you have to what we have in <code>snowman.py</code> so far.</summary>

```python

# Our hidden word 
SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    letter = input("Please enter a letter > ")
    if len(letter) > 1 or not letter.isalpha():
        print("Invalid letter please enter a single character.")
    
    return letter

# Invoke the function the we wrote
get_letter_from_user()

```
</details>

### Step 2:  Check for a letter in SNOWMAN_WORD

We are now going to work on the main `snowman` function (the function we will call when we want to play the game Snowman).  This function is  similar to `guess_the_number`.

The only check we have to do on the letter is check if it's in the word or not.  To do that, we're going to use the python keyword `in`.  The syntax for `in` is `thing1 in thing2`.  This expression evaluates to `True` if `thing2` contains `thing1`, and `False` otherwise.  We can use it in a conditional expression as `if thing1 in thing2:`.

Our requirements for the `snowman` function are:
1.  Use `get_letter_from_user` to get a letter
1.  Check if the letter is in `SNOWMAN_WORD` 
    - print "Letter found" if the letter is in `SNOWMAN_WORD`.
    - print "Letter not found" if it's not in `SNOWMAN_WORD`.
1.  Return `True` if the letter is in `SNOWMAN_WORD`, otherwise return `False` if it's not in `SNOWMAN_WORD`.

Use the outlined requirements above to write the `snowman` function in `snowman.py`. We should call the `snowman` function and execute the file to check that our logic is working as we expect it to.

<br/>

<details>
<summary>Once you've written <code>snowman</code>, compare what you have to our sample code in <code>snowman.py</code> so far.</summary>

```python

# Our hidden word 
SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    letter = input("Please enter a letter > ")

    if len(letter) > 1 or not letter.isalpha():
        print("Invalid letter please enter a single character.")
    
    return letter

def snowman():
    user_letter = get_letter_from_user()
    if user_letter in SNOWMAN_WORD:
        print("Letter found")
        return True
    else:
        print("Letter not found")
        return False

# Since the snowman function calls get_letter_from_user, we should test that snowman works as we expect it to by calling it
snowman()

```
</details>

## Summary

We learned that a function is a named block of code that encapsulates a specific task that can be invoked. When we create a function we should come up with a name that describes what the function does and also define the arguments that should be passed to the function. Additionally, functions keep our code DRY because we can call a function when we need the logic inside the function to run instead of needing to repeat what was already written. 

We also set up the Snowman project in our `snowman_project` directory and started writing functions for the Snowman game in `snowman.py`. We will continue adding to our game in future lessons.