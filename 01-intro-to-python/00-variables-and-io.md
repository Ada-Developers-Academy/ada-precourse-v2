# Variables and IO

## Learning Goals

At the end of this lesson we will be able to...

- Identify variable definition statements.
- Capture user input in a variable.

## Introduction

**Textbook for this section: [link to ada build variables]**

In this lesson we will have a quick refresher on variables and go into an explanation of IO.

## Vocabulary and Syntax

### Definitions

- **Variable**: Name for a piece of data we have stored.
- **IO**: Input and Output
- **Input**: A way to get information _in_ to a program.
- **Output**: A way to get _out_ of a program.

### Syntax

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

As you've already seen variables are how we store data in Python programs.  They are the basic building blocks for almost all programs in almost all programming languages.


## Variable Practice

Identify all of the variables in the following code:

```python
market = "Pike Place"
attraction = "Space Needle"
weather = "cloudy"
chance_of_rain = "90%"

print(chance_of_rain)
```

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

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

<!-- ======================= END CHALLENGE ======================= -->

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

Input and output (collectively called "I/O" or "IO" for short) are how we get data _in_ to and _out_ of our programs.  You've already used one IO function in your coding challenge: `print`.  The `print` function _outputs_ what we give it to the terminal so the user can see it.

While there are other types of output (eg. writing to files and sending things over the internet) print will do just fine for our purposes right now.

As far as _input_ we're going to introduce a new function to get input from the user on the terminal.  It was given the helpfully obvious name `input`.  When we call the `input` it prints a prompt to the user to ask for their input.

### The `input` Function

The `input` function takes a string that prompts the user with and then takes what they type for the rest of the _line_ and returns that value.

```python
>>> input("What is your favorite programming language? ")
What is your favorite programming language? Python!
'Python!'
```

Notice the space after the question mark.  If forget that there isn't any space before the user starts typing:

```python
>>> input("What is your favorite programming language?")
What is your favorite programming language?Python!
'Python!'
```

This still works, it just looks a little awkward.

This isn't so useful on its own but we can store the result of calling `input` in a variable for later use:

```python
>>> language = input("What is your favorite programming language? ")
What is your favorite programming language? Python!
>>>
>>> print(f"{language} is my favorite too!")
Python is my favorite too!
```

### Exercise: Make a Program in a File

Lets create a file to run our python code in!

Open up terminal and create a folder called `ada` with:

```sh
mkdir ada
```

Then we can move into that folder with:

```sh
cd ada
```

Then lets create a subfolder for the precourse.  This is where we can keep our pre-ada materials.  Then we can move into (or change directory `cd`) into that subfolder.

```sh
mkdir precourse
cd precourse
```

If you ever want to find out what folder you are in you can type:

```sh
pwd
```

`pwd` is short for "Present Working Directory".  It's a handy command to tell you which folder you are in.

Next we can create a blank text file to hold some Python code with the `touch` command.

```sh
touch hello.py
```

We can open that folder (if VS code is properly setup) with the `code` command.

```sh
code .
```

Notice the "." after `code`.  The "." stands for the current folder.  So we told VS Code to open the current folder as a project.  This will be quite handy once we start at Ada.

Next fill in the empty file "hello.py" with the following (copy and paste or type it in).

```python
# hello.py
name = input("What is your name? ")

print(f"Hello, {name}!")
```

You can then run this using from the folder you saved the file in using:

```sh
python3 hello.py
```

## Summary

Variables and IO are useful for a wide variety of things and are the basic building blocks of almost all programs.  We've shown you a few different ways to use them that will help you going forward.  We use variables to store things and input and output to interact with the world outside of our programs.

