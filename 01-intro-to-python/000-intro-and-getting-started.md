# Introduction and Getting Started

## Introduction

Welcome to the *Intro to Python* part of the Precourse at Ada Developers Academy!  If you have not yet gone through the *Preparing for Ada* content, we highly recommend you complete those lessons before beginning this portion of the Precourse.  

This Intro to Python course uses the Ada Build curriculum as a "textbook" reference.  If you haven't seen the Ada Build content, that's ok!  Each lesson will contain a "Textbook for this section" link to the relevant Ada Build section near the top of the lesson.

### Learning Goals

There are three main learning goals in this section of the Precourse:

* Review and practice core Python programming concepts from the Ada Build curriculum:
    * Variables and IO
    * Conditionals
    * Functions
    * Loops
    * Lists
    * Dictionaries
* Introduce one new topic not found in the Ada Build curriculum:
    * Helper Functions
* Guide students through building two Python projects:
    * Guess the Number
    * Snowman


Each lesson will follow roughly the same sequence:
* Topic introduction
* Vocabulary
* Examples
* Practice Problems
* Project Work

## Setup

### Make a Program in a File

We can run use a Python repl to run and test our code, but if we want to write longer blocks of code, it's easier to use files to write and run our code.  Lets create our first file to run our python code in!

Open up terminal and check out the screen. It is a text-based visual of our folder and file structure. Let's find out where we are:

```sh
pwd
`pwd` is short for "Present Working Directory".  It's a handy command to tell you which folder you are in.

From this current location in our folder structure we will create a folder called `ada` with:
```sh
mkdir ada
```

Then we can move into that folder with:

```sh
cd ada
```

Now, let's create a subfolder for the Precourse.  This is where we can keep our pre-ada materials.  Then we can move into (or change directory `cd`) into that subfolder.

```sh
mkdir precourse
cd precourse
```

### !callout-info

## What's My Current Location?

If you ever forget or want to find out what folder you are in, remember that you can type `pwd` again to check your current position in your folder structure.

### !end-callout

Next we can create a blank text file to hold some Python code with the `touch` command.

```sh
touch hello.py
```

We can open that folder (if VS code is properly setup) with the `code` command.

```sh
code .
```

Notice the "." after `code`.  The "." stands for the current folder.  So we told VS Code to open the current folder as a project.  This will be quite handy once we start at Ada.

Next, fill in the empty file `hello.py` with the following (copy and paste or type it in) and save the file.

```python
# hello.py
name = input("What is your name? ")

print(f"Hello, {name}!")
```

To run the code in the file, first return to the terminal.  Check to see if you are in the same folder as your file.  To see all of the files in your current folder use the command `ls`.

```sh
ls
```

If you are not in the correct folder, move "down" to the correct folder using the `cd` command (or, if you need to move "up," use `cd ..`).  Once you are in the correct folder, run the code you saved in your `hello.py` file using:

```sh
python3 hello.py
```

You should see the prompt `What is your name? ` and when you enter your name and press return, you should see `Hello, (name)` on the next line!

```sh
python3 hello.py
What is your name? Jasmine
Hello, Jasmine!
```

Congratulations, you just wrote your first Python file!

## Followup Exercise

Modify the "hello.py" program above to read in both your name and age and print out:  "Hello <NAME> you are <AGE> years old!".

For example, if we entered "Han" for the name and "14" for the age, it would print out:

"Hello, Han you are 14 years old!"
