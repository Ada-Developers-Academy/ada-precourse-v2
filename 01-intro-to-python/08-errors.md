# Errors

## Learning Goals

At the end of this lesson students will be able to:

* Read Python error output
    * Understand stack traces
    * Find the line number where an error occurs
* Use a search engine to better understand error messages

## Introduction

Errors are a part of writing code. No matter how experienced or how skilled a programmer is, they will still sometimes make mistakes! Error output helps us find those mistakes and gives hints on how to fix them. Python error output can be a bit tricky to decipher at first, but it becomes easier and easier with practice!

## An example error

Let's look at a Python program that has a bug, and see what type of error it produces.

The program below has a function `print_greeting` that takes in a name, and prints a hello message to that person. We call this function with the name `"Xinting"`.

```python
def print_greeting(person):
    print(f"Hello {preson}!")

print_greeting("Xinting")
```

We expect that when we run the program we will get the following output:

```
Hello Xinting!
```

However, we instead get an error output. This is what the output looks like:

```
Traceback (most recent call last):
  File "/Users/ada/scratch/greeter.py", line 4, in <module>
    print_greeting("Xinting")
  File "/Users/ada/scratch/greeter.py", line 2, in print_greeting
    print(f"Hello {preson}!")
NameError: name 'preson' is not defined
```

It looks like we've got a bug in our program! This error output is quite a mouthful, so let's split it into parts to see what it's telling us.

## Dissecting an error

Errors in Python often have two parts - a stack trace and an error message. The stack trace will tell us where the error happened, and the error message will tell us what went wrong. We will discuss each part.

### Stack Trace

| Vocab       | Definition                                                                                                                                            | Synonyms  | How to Use in a Sentence                                                                                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stack Trace | A report of the functions that were called at a certain point in time during the execution of a program. | Traceback | "When debugging that error, we should check the stack trace to see what line of code caused it," "The stack trace is very long, but we can see what test called this function here." |

Stack traces tell us where the error happened. They are useful for showing us what chain of events led up to the error, and what lines of code are responsible. This is what the stack trace is for the error from above:

```
Traceback (most recent call last):
  File "/Users/ada/scratch/greeter.py", line 4, in <module>
    print_greeting("Xinting")
  File "/Users/ada/scratch/greeter.py", line 2, in print_greeting
    print(f"Hello {preson}!")
```

What does this stack trace show? It shows what chain of functions was called when the error occurred. It's telling us where the error happened, and under what conditions.

The stack trace in this example has two parts. The first one shows where our function was called:

```
  File "/Users/ada/scratch/greeter.py", line 4, in <module>
    print_greeting("Xinting")
```

This tells us the file the function was called in, and the line the function call happened on. It also displays the line of code where the function was called. In this case, we can see that `print_greeting("Xinting")` was executed in line 4 of `greeter.py`.

The second part shows what happened inside that `print_greeting` function:

```
  File "/Users/ada/scratch/greeter.py", line 2, in print_greeting
    print(f"Hello {preson}!")
```

It's telling us the error occurred when trying to execute `print(f"Hello {preson}!")` in the `print_greeting` function on line 2 of the `greeting.py` file.

Together, these parts of the traceback tell the story of how we got to the line where the error happened. We know that line 2 is suspicious and should be investigated! But what exactly happened?

### Error message

After the traceback, the error output includes an error message that describes the actual problem. Here's what the error message looks like in our example:

```
NameError: name 'preson' is not defined
```

This error message has two parts: the type of the error, and a description of the error.

The first part before the colon tells us the type of error, in this case a `NameError`. This type of error occurs when Python is unable to find a variable or function with the name specified in the code.

The second part, after the colon, tells us what happened in this specific `NameError`. In our example, it tells us:

```
name 'preson' is not defined
```

It's telling us that we attempted to use a variable named `preson`, but Python couldn't find any variable with that name.

## Using an error to debug

Let's put what we've learned together to see if we can find the cause of the error and how to fix it. As a reminder, here's the code we ran, and the error output we got:

```python
def print_greeting(person):
    print(f"Hello {preson}!")

print_greeting("Xinting")
```

```
Traceback (most recent call last):
  File "/Users/ada/scratch/greeter.py", line 4, in <module>
    print_greeting("Xinting")
  File "/Users/ada/scratch/greeter.py", line 2, in print_greeting
    print(f"Hello {preson}!")
NameError: name 'preson' is not defined
```

From the stack trace, we determined that the error occurred on line 2. From the error message, we determined that Python was unable to find a variable named `preson`. Based on this, take a moment to see if you can spot the bug in the program!

<br>

<details>
<summary>Expand to see answer</summary>

The bug is a typo. We accidentally wrote `preson` on line 2 instead of `person`. Oops! Because of this typo, Python wasn't able to find the right variable. That's why it gave us a `NameError`. This is a super common error and one you'll certainly run into at some point!

The fixed code would look like this:

```python
def print_greeting(person):
    print(f"Hello {person}!") # Fixed the typo on this line

print_greeting("Xinting")
```
</details>

## Debugging tips

### The good stuff is usually at the bottom

Stack traces can get VERY long if there are lots of function calls. Usually, we don't need to look at the whole thing. We can start by looking just at the error message, and the last part of the stack trace. This will tell us the error that happened, and the line where the error actually occurred.

### Search engines are our friend!

What if we looked at the error message and it wasn't clear to us what it was saying? We can search for the error message online to help us find out what's going on!

Our error message will often include some of our own variable names that might obscure the search. Try removing these before pasting the error message into the search engine. For example, instead of searching for:

```
NameError: name 'preson' is not defined
```

Try searching for:

```
NameError: name is not defined
```

Note that we removed `'preson'` because that variable name is specific to our code.

After searching for this error, we might receive a result like [this excellent page](https://careerkarma.com/blog/python-nameerror-name-is-not-defined/) that describes a `NameError` and possible causes and fixes.

### VS Code is our friend!

VS Code will often help us find bugs by underlining parts of your code with possible issues. This is what our example code looks like in VS Code:

![The sample code used in this lesson as displayed in VS Code. There is a squiggly line underneath the misspelled preson variable.](/01-intro-to-python/images/vscode-underlining.png)

Note that there's a squiggly underline beneath our variable name with the typo! Super useful!

To get even more information, we can hover the mouse over the underlined portion:

![The sample code used in this lesson as displayed in VS Code. A message box displays details about the underlined error: "preson" is not defined.](/01-intro-to-python/images/vscode-hover.png)

We can see that it warns us that the variable is not defined. Sometimes the warning that VS Code gives when hovering is different than what we get when running the program. It's often useful to look at both to see if one is easier to understand than the other!

## Summary

Reading error output is an essential skill for software engineers. In this lesson we learned how we can use the stack trace to see where an error happened, and the error message to tell what went wrong. We now know that the useful part of the error output is often at the bottom. We also found that VS Code and search engines can be helpful in deciphering confusing error messages.

## Questions

### !challenge

* type: multiple-choice
* id: 78653bc7-4ff9-417c-8f37-24a1bf77659b
* title: Searching for Errors

##### !question

Suppose that we have the code:

```python
number_str = "7.0"
parsed_number = int(number_str)
```

When we run this, we get the following output:

```
Traceback (most recent call last):
  File "/Users/ada/scratch/number.py", line 2, in <module>
    parsed_number = int(number_str)
ValueError: invalid literal for int() with base 10: '7.0'
```

What's the best query to put into a search engine to help us determine the cause of the error?

##### !end-question

##### !options

* `ValueError: invalid literal for int() with base 10: '7.0'`
* `ValueError: invalid literal for int() with base 10`
* `ValueError`
* `File "/Users/ada/scratch/number.py", line 2, in <module>`

##### !end-options

##### !answer

* `ValueError: invalid literal for int() with base 10`

##### !end-answer

#### !explanation
`ValueError: invalid literal for int() with base 10` gives all the necessary information about the cause of the error. We make sure to avoid including the specific value from our code, `7.0`, because that's a bit too specific and may muddy the search. In this particular case it doesn't make a huge difference, but it can sometimes be very important!
#### !end-explanation

### !end-challenge


### !challenge

* type: multiple-choice
* id: 938efb00-5764-4f6d-8a3c-38101e348416
* title: Reading Tracebacks

##### !question

Suppose we get an error output that looks like this:

```
Traceback (most recent call last):
  File "/Users/ada/scratch/number.py", line 16, in <module>
    a()
  File "/Users/ada/scratch/number.py", line 5, in a
    b()
  File "/Users/ada/scratch/number.py", line 11, in b
    something()
  File "/Users/ada/scratch/number.py", line 14, in something
    ada()
  File "/Users/ada/scratch/number.py", line 2, in ada
    lovelace()
  File "/Users/ada/scratch/number.py", line 8, in lovelace
    1 / 0
ZeroDivisionError: division by zero
```

What line does the `ZeroDivisionError` occur at in our code?
##### !end-question

##### !options

* 16
* 5
* 11
* 14
* 2
* 8

##### !end-options

##### !answer

* 8

##### !end-answer

#### !explanation
Remember, the good stuff is often at the bottom! The last part of the stack trace tells us that the error happened on line 8. All the other parts of the stack trace are telling us which functions were called on our way to line 8.
#### !end-explanation

### !end-challenge