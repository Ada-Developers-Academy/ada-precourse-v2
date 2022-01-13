# Errors

## Learning Goals

At the end of this lesson students will be able to:

* Read Python error messages
    * Understand stack traces
    * Find the line number where an error occurs
* Identify common errors

## Introduction

Errors are a part of part of writing code. No matter how experienced or how skilled a programmer is, they will still sometimes make mistakes! Error messages help us find those mistakes and give hints on how to fix them. Python error messages can be a bit tricky to decipher at first, but it becomes easier and easier with practice!

## An example error

Let's look at a Python program that has a bug, and see what type of error it produces.

The program below has a function `print_greeting` that takes in a name, and prints a hello message to that person. We call this function with the name `"Xinting"`.

```python
def print_greeting(person):
    print(f"Hello {preson}!")

print_greeting("Xinting")
```

We expect that when we run the program we get the following output:

```
Hello Xinting!
```

However, we instead get an error message. This is what the message looks like:

```
Traceback (most recent call last):
  File "/Users/auberonlopez/programming/ada/scratch/greeter.py", line 4, in <module>
    print_greeting("Xinting")
  File "/Users/auberonlopez/programming/ada/scratch/greeter.py", line 2, in print_greeting
    print(f"Hello {preson}!")
NameError: name 'preson' is not defined
```

It looks like we've got a bug in our program! This error message is quite a mouthful, so let's split it into parts to see what it's telling us.

## Dissecting an error

