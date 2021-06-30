# Variables and IO

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=411bb142-cb4e-4355-bf00-acb7006740a7&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson we will be able to...

- Identify variable definition statements.
- Capture user input in a variable.

## Introduction

**[Textbook for this section:](https://colab.research.google.com/drive/1kfE-bujlwiJoDxTWIXa8u1GPGDJAnjvS?usp=sharing)**

In this lesson we will have a quick refresher on variables, and then go into an explanation of IO.

## Vocabulary and Syntax

### Definitions

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| Variable |  Name for a piece of data we have stored. | Reference | We assigned 21 to the variable |
| IO | Input and Output | Recieved and sent data | Our IO was done by entering data into and printing things out on the terminal screen. |
| Input | A way to get information _in_ to a program. | Recieved data | Our input comes from a spreadsheet | 
| Output | A way to get _out_ of a program. | Sent data | We directed output to Google's website. |

### Syntax

We can start by running the Python repl by entering `python3` in the terminal and doing the following:

```python
>>> # Create a new variable named "ami", and store 
>>> #   the string "Sailor Mercury":
>>> ami = "Sailor Mercury"
>>>
>>> # Create a new variable named "cats" and store the 
>>> #   number 2:
>>> cats = 2
>>>
>>> # "print" using some variables and a format string.
>>> print(f"{ami} has {cats} cats!")
Sailor Mercury has 2 cats!
>>>
>>> # Ask the user what the cats are named.
>>> first_cat = input("Name of the first cat? ")
Name of the first cat? Luna
>>> second_cat = input("Name of the second cat? ")
Name of the second cat? Artemis
```

## Variables

As you've already seen, variables are how we store data in Python programs.  They are the basic building blocks for almost all programs in almost all programming languages.


## Variable Practice

Identify all of the variables in the following code:

```python
market = "Pike Place"
attraction = "Space Needle"
weather = "cloudy"
chance_of_rain = "90%"

print(chance_of_rain)
```

### !challenge

* type: checkbox
* id: beee62b65b8f41998498bc7bf0f6146f
* title: Variables in the example
* points: 1
* topics: variables

##### !question

Which of the following are variables in the example above?

##### !end-question

##### !options

* market
* attraction
* weather
* chance_of_rain
* "cloudy"
* print

##### !end-options

##### !answer

* market
* attraction
* weather
* chance_of_rain

##### !end-answer

### !end-challenge


## Manipulating Variable Data

In the textbook above, we learned about the `type` function that can be used on variables to return the data type (more specifically, the data type class) of its value. 

```python
>>> mystery = "32"
>>> type(mystery)
<class 'str'>
```

## Constants

Sometimes we want to have a readable name for a value like a variable, but we want to make sure it never changes.  In Python, a _constant_ is a type of variable whose value **cannot** be changed.  Constants are named containers for values that cannot be reassigned.

We create constants by creating variables with all uppercase letters.  We can break up words with underscores.

**Examples**

```python
# Gravity accellerates at 9.8 m/s^2
GRAVITY = 9.8

print(f"Gravity is {GRAVITY} m/s^2 at sea level on earth")

# Another constant example
MAX_LENGTH = 79
```

So why use constants?

1. Using constants makes code more **readable**.  Named values helps communicate their meaning.
1. It helps avoid typos because it would be easy to accidentally type 9.7 at some point in your program and never catch the bug.
1. If the constant value needs to be changed later it's nice to have 1 line which assigns the value in the entire program.

As we build our Snowman program, we will use the following constants:

1.  **SNOWMAN_MIN_WORD_LENGTH** - The shortest length of word we will allow.
1.  **SNOWMAN_MAX_WORD_LENGTH** - The longest length of word we will allow.

## Input/Output (IO)

Input and output (collectively called "I/O" or "IO" for short) are how we get data _in_ to and _out_ of our programs.  You've already used one IO function in your coding challenge: `print`.  The `print` function _outputs_ what we give it to the terminal, so the user can see it.

While there are other types of output (eg. writing to files and sending things over the internet) print will do just fine for our purposes right now.

As for getting data _in_, we're going to introduce a new function that will get input from the user on the terminal.  It was given the helpfully obvious name `input`.  When we call the `input`, it prints a prompt to the user to ask for their input.

### The `input` Function

The `input` function takes a string that prints to the terminal, and then waits for the user to type on the rest of the _line_. Once the user hits the return key, the function receives that value.

```python
>>> input("What is your favorite programming language? ")
What is your favorite programming language? Python!
'Python!'
```

Notice the space after the question mark.  If you forget it, there will be no space before the user starts typing:

```python
>>> input("What is your favorite programming language?")
What is your favorite programming language?Python!
'Python!'
```

This still works; it just looks a little awkward.

This isn't so useful on its own, but we can now store the result of calling `input` in a variable for later use:

```python
>>> language = input("What is your favorite \
>>> programming language? ")
What is your favorite programming language? Python!
>>>
>>> print(f"{language} is my favorite too!")
Python is my favorite too!
```

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## The backslash above

Notice we put "\" at the end of `input("What is your favorite programming language? ")`, because the line is too long.  Otherwise the line is too long to fit in learn.  Inside a string, if you put a \ at the end of a line the string will continue on the next line.  It's a way to make things fit.

### !end-callout


## Followup Exercise

Remember the `hello.py` file we created? Let's modify it so that it will input your name and age in variables, and then print out:  "Hello, `<NAME>`, you are `<AGE>` years old!".

For example, if we entered `"Han"` for the name and `"14"` for the age, it would print out:
`"Hello, Han, you are 14 years old!"`

<details>
<summary>Check out our solution!</summary>

```python
name = input("What is your name? ")
age = input("What is your age? ")

print(f"Hello, {name}, you are {age} years old!")
```
</details>


## Check for Understanding

### !challenge

* type: multiple-choice
* id: 97bac648-e693-4099-b77c-53087b4ed2bd
* title: Select Best Option

##### !question

`print("Hello world!")` represents a(n):

##### !end-question

##### !options

* Input
* Output
* Variable
* Constant

##### !end-options

##### !answer

Output

##### !end-answer

##### !explanation

The `print` function _outputs_ the string `"Hello world!"` to the terminal.

##### !end-explanation

### !end-challenge



### !challenge

* type: short-answer
* id: f045ec9d-1ae4-4aae-85f9-cdee3d2cdaee
* title: Explain the Following Code

##### !question

Why is this not good code?

```python
MAX_QUANTITY = 20

new_quantity = input("How many cookies do you want? ")
MAX_QUANTITY = new_quantity
```

##### !end-question

##### !answer

/.+/

##### !end-answer

##### !placeholder

Add your explanation here...

##### !end-placeholder

<!--optional-->
##### !explanation

A variable name in all uppercase characters is a _constant_, which is *not* supposed to be reassignable.

##### !end-explanation

### !end-challenge


## Summary

Variables and IO are useful for a wide variety of things and are the basic building blocks of almost all programs.  We've shown you a few different ways to use them that will help you going forward.  We use variables to store things and input and output to interact with the world outside of our programs.

