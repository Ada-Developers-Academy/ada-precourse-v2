# Getting Started & The Pre-Ada Units

Welcome to this the Ada Course.  This course, through the "Learn" Learning Management System is a major tool we will use in your education at Ada.  The first units are Pre-Ada units you will need to complete **prior to starting at Ada**.

The purpose of the Pre-Ada unit is to keep you coding (and talking about code) between admissions and the first day of class. You should understand the topics covered in the precourse and Build curriculum and practice this understanding with the assignments provided. Take this opportunity to meet and study with peers in your cohort.  You will have been invited to the Cohort Slack, and we will set up a channel to discuss the course and coding challenges.  **Take advantage of it.**

All admitted students are expected to be well-versed with the concepts covered Ada Build curriculum on the first day of their cohort. This includes conditional flows, loops, functions, lists, dictionaries and Python basics. As such, you are expected to complete all exercises in the Precourse.  

As you complete each assignment you will recieve feedback, some of which is automated and others are not.  This is only our second time using the Learn platform from [Galvanize](https://www.galvanize.com/), and as such there will be bumps in the process.  **Please be patient with bugs and let us know on Slack, so we can fix them.**

Some exercises here are multiple choice, some ask you to write code into a coding window, while others ask you to submit a link to your solution.  Many of the exercises here have tests to automatically tell you if you solved it or not.  Others require an instructor to review your code.  Be patient and we will try to deliver feedback as promptly as possible.  

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=eb492361-e1ed-47f3-845e-acb5001ae8e6&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## You can resubmit

In this course you can always resubmit work.  If you want a 2nd-round of instructor feedback let us know on Slack as we normally only give feedback once.

### !end-callout

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-danger

## Due Dates

# The Precourse should be completed by 4/30/2021 5pm PST

### !end-callout

## Learning Goals prior to starting at Ada

In this course we want you to learn to do the following:

*  Consistently follow [Python coding practices](https://www.python.org/dev/peps/pep-0008/)
*  Understand and use conditional statements
*  Understand and use functions
*  Understand and use loops
*  Understand and write functions with parameters
*  Understand and use lists along with loops
*  Understand and use dictionaries
*  Understand and use lists and dictionaries together - nested data structures with loops

We also want you to learn a bit of workflow and learn to use [VS Code](https://code.visualstudio.com/) to write your programs.

## Your Pre-Ada Responsibilities

* Complete the installfest and make sure you have everything installed
* Complete Each unit of the pre-ada material

## Coding Exercises

### Tested Code Snippets

As you proceed through this course you will be asked to complete a variety of coding challenges.  Put your code into the text areas provided and when you submit the exercise many will be automatically tested and provide you feedback.  Try the exercise below.

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 9ef56303-7e49-46b3-98fc-838ebf9d08e8
* title: Hello World
* points: 1
* topics: python

##### !question

Use the `print` function to print `Hello World!` here.

Type `print("Hello World!")` inside the function below under `# Put your code here`.

##### !end-question

##### !placeholder

```py
def hello_world():
    # Put your code here

```

##### !end-placeholder

##### !tests

```py
import unittest
import main as p
from io import StringIO
from unittest.mock import patch 

class TestPython1(unittest.TestCase):
    def test_prints_hello_world(self):
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            p.hello_world()
            self.assertEqual("Hello World!", fake_out.getvalue().strip())

        # self.assertEqual(1,p.doSomething())
```

##### !end-tests

##### !explanation

In this exercise you learned how to run a coding snippet.  This allows you to enter code and have it checked for correctness via some automated tests.  This will become standard practice accross the Ada Precourse.  

It is intended to give you additional practice writing Python code and getting used to having it checked in Learn.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

### Links to Code

Other programming exercises called Project Challenges will ask you to submit a link to code in [repl.it](https://repl.it).  Later, after you start at Ada we will have you submit work in Learn from [Github](https://github.com).

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: project
* id: 3680ae6f-8fe0-4169-a6c9-6129b9da492e
* title: Example Project Challenge
* points: 1
* topics: example

##### !question

Create a Hello World application on [Repl.it](https://repl.it), and submit a link to your submission.

##### !end-question

##### !placeholder

Place your link here

##### !end-placeholder

##### !hint 

You can learn [how to create a gist](https://docs.github.com/en/github/writing-on-github/creating-gists), or just create a program on [repl.it](https://repl.it).

##### !end-hint

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

## This Lesson

This lesson is about workflow, Python style, and basic types and operations.  This should feel like review and give you a smooth start.  Try to work through things a little at a time. Also, feel free to walk away for a bit when you are stuck, or shout out for support on Slack.  

We'll let you get started...
