# Conditionals

<!-- PRECOURSE UPDATE -->
<!-- <iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=ec78271e-6978-4ffe-8aa8-acb7007cbaea&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe> -->

## Learning Goals

At the end of this lesson we will be able to:

- Write `if...else` statements.
- Extend these with `elif` statements.

## Introduction

**[Textbook for this section](https://colab.research.google.com/drive/1huE7PyavZSJIou4mh5G2e7yfG08Vb7da?usp=sharing)**

In this section we will be building on the concepts from [Variables and IO](./variables-and-io.md). This code snippet will form the basis of a game we will build in the following lessons.

Let's take a look at the following code and consider what's going on:

```python
import random

# pick a number from 1 to 10 and assign the number to the variable n
n = random.randint(1, 10) 
if n < 5:
    print(f"{n} is too small!")
elif n == 5:
    print(f"{n} is just right!")
else:
    print(f"{n} is too large!")
```

| <div style="width:200px"> Code </div>| Description |
| -- | -- | 
| `n = random.randint(1, 10) ` | Invoke the `randint` method from the `random` module that will generate a random integer between 1 and 10. The random integer returned from calling `randint` will be assigned to the variable `n`. |
| `if n < 5:`  | An if statement that checks if the random integer referenced by `n` is less than 5 |
| `print(f"{n} is too small!")` | If the condition from the if statement evaluates to `True`, then use the `print` method and string interpolation to print a string that tells a user the random number is too small. |
| `print(f"{n} is just right!")` | If the condition from the `elif` statement evaluates to `True`, then print a string that tells the user the random number `n` is just right. |
| `else:` | If none of the conditions from the `if` and `elif` statements evaluate to `True`, then the logic associated with the `else` will execute |
| `print(f"{n} is too large!")` | Print a string that tells a user that the random number `n` is too large. |

## Guess the Number

We're going to begin building a game called "Guess the Number".  The rules are simple.  The program will pick a number between 0 and 100, and the user will need to guess it!

Right now, our goal is to accept a single guess and tell the user if it was too high, too low, or just right.  In future lessons, we'll extend it to make it a more interesting game.


Before we get started we need to set up the file that we're going to be working with.  Navigate to the Precourse directory and create a new file called `game.py` using the `touch` command, then use the `code` command to open it in VSCode. We can have a look back at the Introduction and Getting Started lesson if we need to review these commands.

### Generating Random Numbers

For this project we're going to need to generate random numbers between 0 and 100.  We can do this by using the `randint` function from the `random` module.

You can give this a try by writing the following code in `game.py` then running the file in the terminal with the `python3` command:

```python
import random

print(random.randint(0, 100))
```

You should see a new number each execution! Run it a few times to watch the number change.

### !callout-info

### Constants

Before continuing, consider how you could use constants to hold the high and low values for the range.

<br/>

Give it a try, and then view our implementation.

<br/>

<details>
<summary><code>game.py</code> with constant variables for high and low values.</summary>

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)
```

</details>

### !end-callout

### Getting User Input

Now that we have our random number, we need to get information from the user.  To do this we can use the `input` function we learned in the previous lesson.

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")
```

This is where things get tricky, though!  In order to compare the user input to the random number generated, we need to convert `user_input_string` into a number.  We can use the `int` function for that, but if you pass it a badly formatted string, it will cause an error.

Let's try this out, what happens when you add the following line to a new python file and run it?

```python
int("four")
```

We should get a ValueError similar to what's shown below:

```sh
Traceback (most recent call last):
  File "path/to/game.py", line 9, in <module>
ValueError: invalid literal for int() with base 10: 'four'
```

To get around this, we are going to use the string method `isnumeric`.  This will allow us to check if the string is well formatted _before_ we attempt to convert it into an integer so that we can avoid running into errors.

```python
print("four".isnumeric()) # Outputs `False`
```

Note: according to convention `isnumeric` _should_ be named `is_numeric`, but Python doesn't always follow its own naming conventions everywhere.

### The `if`/`else` Statement

So far, we showed the user a prompt to guess a number. Then we took the user's guess and saved it to a variable. Now we're at the point where we need to have our program do one of two things:
- If the user has given us a numeric input, we can convert it to an integer safely.  
- But if the user hasn't given us a numeric input, then we can't convert the user's input to an integer.

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

Now that we have converted the user's input to an integer, we can compare it to the random number generated.  However, we want to have *three* outcomes, not just two!  We want to tell the user if their guess is higher, lower, or exactly the same as the randomly generated number

In fact, we want to add a *fourth* option, which tells the user that the number they picked was outside the range of allowed numbers!

We can do this by nesting `if...else` statements inside of each other:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")

if user_input_string.isnumeric():
    user_input = int(user_input_string)

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print("Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    else:
        if user_input == random_number:
            print("You guessed the number! Good job!")
        else:
            if user_input > random_number:
                print("Your guess is too high")
            else:
                if user_input < random_number:
                    print("Your guess is too low")
                
else:
    print("You must input a number!")
```

This winds up being pretty hard to read, though.  Look how far we have to indent that last `print` statement when we only use `if/else`.

We can make this much easier to read by using the `elif` keyword, which is like an `else` followed by an `if`. When we use `elif` we can reduce the levels of nesting conditional statements and as a result we reduce the amount of indentation:

```python
import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")

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
```

### !callout-info
## Take Note:

As with `if`, the `else` portion of the statement is optional.  That last branch <code>elif user_input < random_number</code> could have simply been an `else` but we decided to explicitly state what was going on to make our code more readable.

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

In this instance, the program only prints out a comment to the user <strong>if</strong> their birthday is the same as today's date.  There's no need for an <code>else</code> because we have nothing <strong>else</strong> we want to do with our information.  The code simply executes the lines of the program from there.  

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

In an `if...elif...else` block, once one conditional statement is true, then it stops looking at any other conditionals.  It doesn't matter how many _could_ be true.  The program executes the first true conditional it finds and then finishes the block.

##### !end-explanation

### !end-challenge


## Summary

We've learned how to generate random numbers and how to check if a user's guess is the same as the random number by using the `if`, `elif`, and `else` to make conditional statements.

We also learned how to process a user's input with `isnumeric` and `int` in order to convert a string to a number for use in our program.