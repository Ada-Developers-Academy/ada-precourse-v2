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
| IO | Input and Output | Received and sent data | Our IO was done by entering data into and printing things out on the terminal screen. |
| Input | A way to get information _in_ to a program. | Received data | Our input comes from a spreadsheet | 
| Output | A way to get _out_ of a program. | Sent data | We directed output to Google's website. |

### Syntax

Create a new file `variables_practice.py` in the precourse directory you created in the previous lesson called "Introduction and Getting Started". As a reminder, you use the touch command to create a new file. 

Add the following to your new file:

```python
# Create a new variable named "ami" and store the string "Sailor Mercury":
ami = "Sailor Mercury"

# Create a new variable named "cats" and store the number 2:
cats = 2

# "print" using some variables and f-strings.
print(f"{ami} has {cats} cats!")
# Sailor Mercury has 2 cats!

# Ask the user what the cats are named.
first_cat = input("Name of the first cat? ")
second_cat = input("Name of the second cat? ")
```

When you're finished writing your program, save it and then run it by using:
```sh
python3 variables_practice.py
```

## Variables

As you've already seen, variables are how we store data in Python programs.  They are the basic building blocks for almost all programs in almost all programming languages.

In the above example, the variable `ami` stores the string value of "Sailor Mercury" and the variable `cats` stores the value of 2. We can use string interpolation to substitute values of variables into placeholders in a string. 

To do string interpolation we use "formatted string literals" (f-strings for short). To use f-strings, begin a string with `f` or `F` before the opening quotation mark. Then inside this string, you write a Python expression between { and } that refer to variables.

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
mystery = "32"
print(type(mystery)) 
# <class 'str'>
```

## Constants

Sometimes we want to have a readable name for a value like a variable, but we want to make sure it never changes.  In Python, a _constant_ is a type of variable whose value **should not** be changed.  Constants are named containers for values that should not be reassigned.

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Capitalization does not prevent reassignment:

Naming variables in all capital letters is a convention to communicate that such variables have constant values that will not change, however, it does not actually prevent reassignment.

### !end-callout

We create constants by creating variables with all uppercase letters.  We can break up words with underscores.

**Examples**

```python
# Gravity accelerates at 9.8 m/s^2
GRAVITY = 9.8

print(f"Gravity is {GRAVITY} m/s^2 at sea level on earth")

# Another constant example
DOZEN = 12

# Yet another constant example
MAX_LENGTH = 79
```

So why use constants?

1. Using constants makes code more **readable**.  Named values help communicate their meaning.
1. It helps avoid typos because it would be easy to accidentally type 9.7 at some point in your program and never catch the bug.
1. If the constant value needs to be changed in the future it's nice to have 1 line which assigns the value in the entire program.

In each of the lessons in Practice with Python we will be building a part of a project called Snowman. We will use the following constants:

1.  **SNOWMAN_MIN_WORD_LENGTH** - The shortest length of word we will allow.
1.  **SNOWMAN_MAX_WORD_LENGTH** - The longest length of word we will allow.

## Input/Output (IO)

Input and output (collectively called "I/O" or "IO" for short) are how we get data _in_ to and _out_ of our programs.  You've already used one IO function in your coding challenge: `print`.  The `print` function _outputs_ what we give it to the terminal, so the user can see it.

While there are other types of output (eg. writing to files and sending things over the internet) print will do just fine for our purposes right now.

As for getting data _in_, we're going to introduce a new function that will get input from the user on the terminal.  It was given the helpfully obvious name `input`.  When we call the `input`, it prints a prompt to the user to ask for their input.

### The `input` Function

The `input` function takes a string that prints to the terminal, and then waits for the user to type on the rest of the _line_. Once the user hits the return key, the function receives that value.

```python
input("What is your favorite programming language? ")
```
```python
What is your favorite programming language? Python!
```

Notice the space after the question mark.  If you forget it, there will be no space before the user starts typing:

```python
input("What is your favorite programming language?")
```
```python
What is your favorite programming language?Python!
```
This still works; it just looks a little awkward.

This isn't so useful on its own, but we can now store the result of calling `input` in a variable for later use. Add the code below to `variables_practice.py` and run the code to practice using the `input` function.

```python
# The user's input will be stored in the variable called language
language = input("What is your favorite programming language? ")

print(f"{language} is my favorite too!")
```

## Follow-up Exercise

We've already practiced using the input function in the previous lesson when we asked a user to input their name and age. Now we'll write a short program that asks users for words to fill in some blanks to complete a story.

Create a new file called `story.py` in the precourse directory. Your program will print out a completed story with user input. Ask the user for a holiday, a noun, and a place. 

The completed story will have user input in place of the variables: `"I can't believe it's already <holiday>! I can't wait to put on my <noun> and visit every <place> in my neighborhood."`

For example, if we entered "Thanksgiving" for the holiday, "cat" for the noun, and "fire station" for the place it would print out: "I can't believe it's already Thanksgiving! I can't wait to put on my cat and visit every fire station in my neighborhood."

<details>
<summary>Check out our solution!</summary>

```python
holiday = input("Enter a holiday: ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")

print(f"I can't believe it's already {holiday}! I can't wait to put on my {noun} and visit every {place} in my neighborhood.")
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

