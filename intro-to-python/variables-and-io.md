# Variables and IO

<!-- PRECOURSE UPDATE -->
<!-- <iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=411bb142-cb4e-4355-bf00-acb7006740a7&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe> -->

## Learning Goals

At the end of this lesson we will be able to...

- Identify variable definition statements.
- Capture user input in a variable.

## Introduction

**[Textbook for this section](https://colab.research.google.com/drive/1kfE-bujlwiJoDxTWIXa8u1GPGDJAnjvS?usp=sharing)**

In this lesson we will have a quick refresher on variables, and then go into an explanation of IO.

## Vocabulary

### Definitions

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| Variable |  Name for a piece of data we have stored. | Reference | We assigned 21 to the variable |
| IO | Input and Output, describes any operation that transfers data to or from some source | Received and sent data | An example of IO is typing data _into_ our terminal and then that data is _outputted_ to the terminal screen. |
| Input | A way to get information _in_ to a program. | Received data | Our input comes from a spreadsheet | 
| Output | A way to get _out_ of a program. | Sent data | The output will be shown on our monitor. |

## Variables

Variables are how we store data in Python programs.  They are the basic building blocks for almost all programs in almost all programming languages.

Consider this code snippet:

```python

# Create a new variable named "ami" and store the string "Sailor Mercury":
ami = "Sailor Mercury"

# Create a new variable named "cats" and store the number 2:
cats = 2

# "print" using some variables and f-strings.
print(f"{ami} has {cats} cats!") # Sailor Mercury has 2 cats!

```

In the above example, the variable `ami` stores the string value of "Sailor Mercury" and the variable `cats` stores the value of 2. We can use string interpolation to substitute values of variables into placeholders in a string. 

To do string interpolation we use "formatted string literals" (f-strings for short). To use f-strings, begin a string with `f` or `F` before the opening quotation mark. Then inside this string, we can write a Python expression between opening and closing curly braces `{ }`, like a variable, to reference some value.

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

In the Ada Build textbook linked above, we learned about the `type` function that can be used on variables to return the data type (more specifically, the data type class) of its value. 

```python
mystery = "32"
print(type(mystery)) 
# <class 'str'>
```

## Constants

Sometimes we use variables to provide a readable name for a value, but we want to make sure the value never changes.  In Python, a _constant_ is a type of variable whose value **should not** be changed.  Constants are named containers for values that should not be reassigned.

We create constants by creating variables with all uppercase letters.  We can break up words with underscores.

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Capitalization Does Not Prevent Reassignment:

Naming variables in all capital letters is a convention to communicate that such variables have constant values that will not change, however, it does not actually prevent reassignment.

### !end-callout

**Examples**

```python
# Gravity accelerates at 9.8 m/s^2
GRAVITY = 9.8

print(f"Gravity is {GRAVITY} m/s^2 at sea level on Earth")

# Another constant example
DOZEN = 12

# Yet another constant example
NUM_LETTERS_IN_ALPHABET = 26
```

So why use constants?

1. Using constants makes code more **readable**.  Named values help communicate their meaning.
1. Using constants helps avoid typos because it would be easy to accidentally type 1.2 instead of 12 at some point in your program and never catch the bug.
1. Using constants makes code easier to maintain. If the constant value needs to be changed in the future it will only need to be changed in one place in the entire program.
  
In each of the lessons in Practice with Python we will be building a part of a project called Snowman. We will use the following constants:

1.  **SNOWMAN_MIN_WORD_LENGTH** - The shortest length of word we will allow.
2.  **SNOWMAN_MAX_WORD_LENGTH** - The longest length of word we will allow.

## Input/Output (IO)

Input and output (collectively called "I/O" or "IO" for short) are how we get data _in_ to and _out_ of our programs.  You've likely seen and used one IO function in your coding journey: `print`.  The `print` function _outputs_ what we give it to the terminal, so the user can see it.

While there are other types of output (eg. writing to files and sending things over the internet) `print` will do just fine for our purposes right now.

As for getting data _in_, we will use another function to get input from the user and the terminal.  This function has the helpfully clear name `input`.  When we call `input`, it prints a prompt in the terminal to the user to ask for their input.

### The `input` Function

The `input` function takes a string as an argument that gets printed to the terminal, and then waits for the user to type a response to the prompt on the rest of the _line_ in the terminal. Once the user hits the return key, the function receives that value.

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

Gathering user input may not be exciting on it's own, but we can now store the result of calling `input` in a variable for later use. Once we have the input in a variable we can print the value, perform operations on the data, or even create games such as a fill-in-the-blank story with words that a user must fill in to complete the tale.

## Practice Exercises

Create a new file `variables_practice.py` in the `precourse` directory we created in the previous lesson called "Introduction and Getting Started". As a reminder, we use the `touch` command to create a new file. 

Add the following code to `variables_practice.py`:

```python
# The user's input will be stored in the variable called language
language = input("What is your favorite programming language? ")

print(f"{language} is my favorite too!")
```

| <div style="width:175px"> Code </div>| Description | 
| -- | -- | 
| `language = ...` | We are declaring a variable named `language` that will store the value returned by a function call. |
| `... input("What is your favorite programming language? ")` | We call the `input` function with a string that will be displayed to a user. The user's response will be returned as a string when we call `input`. |
| `print(f"{language} is my favorite too!")` | Call the `print` function with an f-string which uses string interpolation to display the value referenced by `language` |

When we're finished writing our program, we should save it and then execute it by running this command:
```sh
python3 variables_practice.py
```

In the following lessons we will use the `input` function to build a guessing game.

### Complete the Story

We've already practiced using the input function in the previous lesson when we asked a user to input their name and age. Now we'll write a short program that asks users for words to fill in some blanks to complete a story.

Create a new file called `story.py` in the Precourse directory. Your program will print out a completed story with user input. Ask the user for a holiday, a noun, and a place. 

The completed story will have user input in place of the variables: `"I can't believe it's already <holiday>! I can't wait to put on my <noun> and visit every <place> in my neighborhood."`

For example, if we entered `"Thanksgiving"` for the holiday, `"cat"` for the noun, and `"fire station"` for the place it would print out: `"I can't believe it's already Thanksgiving! I can't wait to put on my cat and visit every fire station in my neighborhood."`

<br/>

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

Why does this code not follow Python coding convention?

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

A variable name in all uppercase characters is a _constant_ variable. By convention, a constant variable should *not* be reassigned a different value.

##### !end-explanation

### !end-challenge


## Summary

Variables and IO are useful for a wide variety of things and are the basic building blocks of almost all programs.  We've seen a few different ways to use variables that will help us write readable and maintainable code going forward.  We use variables to store values and use input and output to interact with the world outside of our programs.