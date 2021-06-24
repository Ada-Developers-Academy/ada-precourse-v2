# Conditionals

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=ec78271e-6978-4ffe-8aa8-acb7007cbaea&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson we will be able to:

- Write `if...else` statements.
- Extend these with `elif` statements.

## Introduction

**[Textbook for this section:](https://colab.research.google.com/drive/1huE7PyavZSJIou4mh5G2e7yfG08Vb7da?usp=sharing)**

In this section we will be building on the code that you learned in the previous lesson [Variables and IO](./00-variables-and-io.md).  

Let's take a look at the following code and consider what's going on:
```python
>>> import random
>>> random.randint(1, 10) # pick a number from 1 to 10
7
>>> # pick another number from 1 to 10
>>> n = random.randint(1, 10) 
>>> if n < 5:
...     print(f"{n} is too small!")
...  elif n == 5:
        print("{n} is just right!")
...  else:
...     print("{n} is too large!")
...
5 is just right!
```

## Vocabulary

| Vocab                        | Definition                                                   | How to Use in a Sentence |
| ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------ |
| `random.randint` | A function that will generate a random integer in a range.  | We used `random.randint(5, 15)` to get a random integer between 5 and 15.  |
| `if...else`  | A statement to do one of two things based on a condition.  | We wrote an `if...else` statement to determine if the person was old enough to consume alcohol.  |
|  `if...elif...else` | A statement to conditionally do one of three or more things.  | We wrote an `if...elif...else` statement to print out if the person was too young, too old or just the right age | 


## Guess the Number

We're going to begin building a game called "Guess the Number".  The rules are simple.  The program will pick a number between 0 and 100, and you will need to guess it!

Right now, our goal is to accept a single guess and tell the user if it was too high, too low, or just right.  In future lessons, we'll extend it to make it a more interesting game.


Before we get started we need to set up the file that we're going to be working with.  Follow the instructions from the file setup lesson to navigate to the precourse directory that has your `hello.py` file.  Create a new file called `game.py` using the `touch` command and use the `code` command to open it in VSCode. 

### Generating Random Numbers

For this project we're going to need to generate random numbers between 0 and 100.  We can do this by using the `randint` function from the `random` module.

You can give this a try from inside of the Python command line:

```python
>>> import random
>>> random.randint(0, 100)
35
```

Your number probably won't be 35, though! Run it a few times to watch the number change.

Using this, we can start our game as follows (copy the following code into `game.py`):

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)
```

### Getting User Input

Now that we have our random number, we need to get information from the user.  To do this we can use the `input` function we learned in the previous lesson.

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")
```

This is where things get tricky, though!  In order to compare the user input to the random number generated, we need to convert it into a number as well.  We can use the `int` function for that, but if you pass it a badly formatted string, it will cause an error.

```python
>>> int("four")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'four'
>>>
```

To get around this, we are going to use the string method `isnumeric`.  This will allow us to check if the string is well formatted _before_ we attempt to convert it into an integer.

```python
>>> "four".isnumeric()
False
```

Note: `isnumeric` _should_ be named `is_numeric`, but Python doesn't always follow its own naming conventions everywhere.

### The `if`/`else` Statement

Now we're at the point where we need to have our program do one of two things:
- If the user has given us a numeric input, we can convert it to an integer safely.  
- But if they haven't, then we can't.

This is a perfect time to use the `if`/`else` statement!

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

## The `if...elif...else` Statement

Now that we have our input as an integer, we can compare it to the random number generated.  However, we want to have *three* outcomes, not just two!  We want to tell the user if the number is higher, lower, or exactly the same.

In fact, we want to add a *fourth* option, which tells the user that the number they picked was outside the range of allowed numbers!

We can do this by nesting `if...else` statements inside of eachother:

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

This winds up being pretty hard to read, though.  Look how far we have to indent that last `print` statement!

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

### !callout-info
## Take Note:

As with `if`, the `else` portion of the statement is optional.  That last branch could have simply been an `else` but we decided to explicitly state what was going on.  
<br/>
Let's take a look at an example when using only an `if` _without_ an explicit `else` might make sense:  

``` python
todays_date = "05/22"
users_bday = input("Enter your birthdate (mm/dd): ")

if todays_date == users_bday:
    print("Wow, that's today! Happy birthday!")

users_bday_year = input("What year were you born? ")
...
# other code goes on from here
```
<br/>
In this instance, the program only prints out a comment to the user _if_ their birthday is the same as today's date.  There's no need for an `else` because we have nothing _else_ we want to do with our information.  The code simply moves on from there.  

### !end-callout

## Check for Understanding

### !challenge

* type: multiple-choice
* id: 69b4e28e-3741-47c6-a09d-74648e7ee859
* title: Predict the Code's Behavior


##### !question

Consider the following code.  How many of the conditional statements will be _checked_?

``` python
pocket_change = 112

if pocket_change < 100:
    print("You have less than a dollar in change.")
if pocket_change > 100:
    print("You have more than a dollar in change.")
if pocket_change > 100 and pocket_change < 500:
    print("You have at least four dollars in change.")
if pocket_change > 500:
    print("That's a lot of change!!!")
```

##### !end-question

##### !options

* 1
* 2
* 3
* 4
* 0

##### !end-options

##### !answer

4

##### !end-answer

<!--optional-->
##### !hint

Remember, you are answering the question of how many conditional statements are being _checked_, not if their `print` statements are being executed.

##### !end-hint

##### !explanation

Each `if` statement is checked.

##### !end-explanation

### !end-challenge

### !challenge

* type: multiple-choice
* id: 1f30b54d-4b25-4772-ae0f-39c1d17068ef
* title: Predict the Code's Behavior


##### !question

Consider the following code.  How many of the conditional statements will be _checked_?

``` python
pocket_change = 112

if pocket_change < 100:
    print("You have less than a dollar in change.")
elif pocket_change > 100:
    print("You have more than a dollar in change.")
elif pocket_change > 100 and pocket_change < 500:
    print("You have at least four dollars in change.")
else pocket_change > 500:
    print("That's a lot of change!!!")
```

##### !end-question

##### !options

* 1
* 2
* 3
* 4
* 0

##### !end-options

##### !answer

2

##### !end-answer

<!--optional-->
##### !hint

Remember, in an `if...elif...else` block, only one of the conditional statements can ultimately be _executed_.

##### !end-hint

##### !explanation

In an `if...elif...else` block, once one conditional statement is true, then it stops looking at any other conditionals.  Doesn't matter how many _could_ be true.  The program executes the first true conditional it finds and then finishes the block.

##### !end-explanation

### !end-challenge


## Summary

We've learned how to choose random numbers and how to handle them using `if`, `elif`, and `else` to make conditional statements do what we want.

We also learned how to clean up the user's input into a more useful form for our programs.
