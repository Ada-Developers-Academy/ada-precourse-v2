# Variables and I/O

## Learning Goals

At the end of this lesson students will be able to:

- Be able to write `if`/`else` statements.
- Be able to extend these with `elif` statements.

## Introduction

**Textbook for this section: [link to ada build conditionals]**

In this section we will be building on the code that you learned in the previous lesson [Variables and IO].  

## Guess the Number

We're going to begin building a game called "Guess the Number".  The rules are simple.  The program will pick a number between 0 and 100 and you will need to guess it!

Right now our goal is to accept a single guess and tell the user if it was too high, too low or just right.  In future lessons we'll extend it to make it a more interesting game.

### Generating Random Numbers

For this project we're going to need to be able to generate random numbers between 0 and 100.  We can do this using the `randint` function from the `random` module.

You can give this a try from inside of the Python command line:

```python
>>> import random
>>> random.randint(0, 100)
35
```

Your number probably won't be 35 though!

Using this we can start our game as follows:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)
```

### Getting User Input

Now that we have our random number we need to get information from the user.  To do this we can use the `input` function we learned in the previous lesson.

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")
```

This is where things get tricky though.  To be able to compare the user input to the random number we've chosen we need to convert it into a number as well.  We can use the `int` function for that but if you pass it a badly formatted string it will cause an error.

```python
>>> int("four")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'four'
>>>
```

To get around this we are going to use the string method `isnumeric`.  This will allow us to check if the string is well formatted before we attempt to convert it into an integer.

```python
>>> "four".isnumeric()
False
```

Note: `isnumeric` _should_ be named `is_numeric` but Python unfortunately doesn't follow its own naming conventions everywhere.

### The `if`/else Statement

Now we're at the point where we need to have our program do one of two things.  If the user has given us numeric input we can convert it to an integer safely but if they haven't we can't.

This is a perfect time to use the `if`/`else` statement:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")

if user_input_string.isnumeric():
    user_input = int(user_input_string)
else:
    print("You must input a number!")
```

## The `if`/`elif`/`else` Statement

Now that we have our input as an integer we can compare it to the random number we've picked.  However we want to have three outcomes, not just two!  We want to tell the user if the number is higher, lower or exactly the same.

In fact, we even want to add a fourth option which is to tell the user that the number they picked was outside of the range of allowed numbers!

We can do this by nesting `if`/`else` statements inside of eachother:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")

if user_input_string.isnumeric():
    user_input = int(user_input_string)

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    else:
        if user_input == random_number:
            print("You guessed the number!  Good job!")
        else:
            if user_input > random_number:
                print("Your guess is too high")
            else:
                if user_input < random_number:
                    print("Your guess is too low")
                
else:
    print("You must input a number!")
```

This winds up being pretty hard to read though.  Look how far we have to indent that last `print`!

We can make this much easier to read by using the `elif` keyword, which is like an `else` followed by an `if` but without the extra lines and indentation:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")

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
```

As with `if` the `else` portion of the statement is optional.  (That last branch could have simply been an `else` but we decided to explicitly state what was going on.)

## Summary

We've learned how to choose random numbers and how to handle them using `if`, `elif` and `else` to make conditional statements to do what we want.

We also learned how to clean up the user's input into a more useful form for our programs.

## Vocabulary and Syntax

* `random.randint`: A function that will generate a random integer in a range.
* `if`/`else`: A statement to do one of two things.
* `if`/`elif`/`else`: A statement to do three or more things.

```python
>>> import random
>>> random.randint(1, 10) # pick a number from 1 to 10
7
>>>
>>> n = random.randint(1, 10) # pick another number from 1 to 10
>>> if n < 5:
...     print(f"{n} is too small!")
... elif n == 5:
        print("{n} is just right!")
... else:
...     print("{n} is too large!")
...
5 is just right!
```



