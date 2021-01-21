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

```python
# hello.py
name = input("What is your name? ")

print(f"Hello, {name}!")
```

You can then run this using from the folder you saved the file in using:

```sh
python3 hello.py
```

You can do this by opening up a terminal and using the `cd` command to get to the directory you have the file saved in.

If you don't know what directory your file is saved in you can right-click or <kbd>control</kbd> + click on the tab in VS Code and choose "Copy Path".

If you saved this file inside of your `Developer` folder you would see something like `/Users/your-name/Developer/hello.py`.

Once you remove the `hello.py` from the end you can use the `cd` command to get to the correct folder:

```sh
cd /Users/your-name/Developer/
```

Once you do this you should be able to run the command:

```sh
python3 /Users/your-name/Developer/hello.py
```

And see the following:

```
What is your name? Ada Pre Course
Hello, Ada Pre Course!
```

## Summary

Variables and IO are useful for a wide variety of things and are the basic building blocks of almost all programs.  We've shown you a few different ways to use them that will help you going forward.  We use variables to store things and input and output to interact with the world outside of our programs.

