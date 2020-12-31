# Loops

## Textbook for this section: [link to ada build Loops]

In this section we will be building on the code that you wrote in the previous lesson [Functions].  If you would like to look at our example code version for that lesson, you can find it [here]

## Why Loops?

Loops are one of the primary control structures in programming and they show up in almost every programming language.  In the world of Computer Science Theory, loops, along with sequences (executing one section of code and then another) and selection (aka conditionals, choosing between blocks of code based on a boolean test) are all that are needed to compute any computable function [https://en.wikipedia.org/wiki/Structured_program_theorem].  Understanding loops and using them effectively in your code is a vital first step in your journey as a programmer.  In this lesson we will explore while loops and for loops and use them make Guess the Number a fully functional game and add core functionality to Snowman.  In this lesson we will use both for and while loops to 

## Vocabulary

* `while` loop:  a while loop repeats as long as a boolean conditional statement is true.  The statement is tested before executing the code block inside loop.
```python

test = 0
while test < 10:
    test = test + 2
    print(f"The value of test is {test}")

# When run, this code chunk will output:
# The value of test is 2
# The value of test is 4
# The value of test is 6
# The value of test is 8

```

* `for` loop: a for loop that _iterates_ or repeats over a sequence.  In python it is often used to iterate over a `list` data structure.  It is also commonly paired with the `range` function[link to range function], which returns a list of numbers.  The `for` loop repeats n times, where n is the length of the sequence being looped over.

```python

for num in range(3):
    print(f"The value of num is {num}")

# When run, this code chunk will output:
# The value of num is 0
# The value of num is 1
# the value of num is 2

for num in range(2, 5):
    print(f"The value of num is {num}")

# When run, this code chunk will output:
# The value of num is 2
# The value of num is 3
# the value of num is 4

```

* flag: a variable that is used as a signal that a condition has been met.  Usually a flag is a boolean variable and the value is changed to indicate that the goal or target (whatever the condition is) has been achieved.

## Guess The Number

### Validating User input

In the previous lesson, we pulled the user input into it's own function, while acknowledging that we weren't actually doing the work of validating the input.  We let the user know that the input is not good, but then we just return it:

```python

def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input

```

What we really want to do in this function is to compel the user to give us valid input, and only return our input when it is valid.  We can't really force the user to give us valid input, but what we can do is repeat the process of asking for input until we get something that is valid (or just keep asking forever).  In cases like this, where you need to repeat a process but there is uncertainty about how many times you will do so, a while loop is the ideal tool to use.  To solve this problem we are going to use a flag controlled while loop.  A "flag" is a term for a boolean variable that is set before we enter the loop, and then at some point will be flipped inside the loop to signal that the loop should end (and that the whatever action the loop was trying to accomplish has been completed).  

<details>
<summary>Add a while loop with a flag to the get_number_from_user function to continue to loop until the user gives valid input.  Once you have finished, click here to compare your solution to ours</summary>

```python

def get_number_from_user():
    valid_input = False
    user_input = None
    while not valid_input:
        user_input_string = input("Guess the number: ")
        
        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            valid_input = True
        else:
            print("You must input a number!")

    return user_input

```

Notice that our solution uses a not in the while test.  You could use a flag that is set it to true, and then when we get valid input set it to false.  Think about the readability of your code in that case.  It would not make sense to have a variable named valid_input set to true, if we are trying to get a valid input at the end (starting true then setting to false makes it seem like we're not getting valid input).  Changing the variable name to something like `attempting_valid_input` would work better to make the code readable.  In that case, the code would look like this:

```python

def get_number_from_user():
    attempting_valid_input = True
    user_input = None
    while attempting_valid_input:
        user_input_string = input("Guess the number: ")
        
        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            attempting_valid_input = False
        else:
            print("You must input a number!")

    return user_input

```

**As an aside, variable names can make or break the readability of your code!**

</details>

### Keep The Guessing Game Going!

Now that you have a way to get valid input from the user, it's time to take a look at the guess_the_number function.  There are two ways to play this type of guessing game, the first is with unlimited guesses and the second is with a max number of guesses.  Let's start with the first version with unlimited guesses.  The current version of the function is:

```python

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)

    user_input = get_number_from_user()
        
    if user_input == random_number:
        print("You guessed the number!  Good job!")
    if user_input > random_number:
        print("Your guess is too high")
    if user_input < random_number:
        print("Your guess is too low")
    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")

```

Add a while loop with a flag that tests to see if the user has guessed the correct number.

<details>
<summary>When you are finished, compare your code to our version here</summary>

```python

def guess_the_number():

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)
    waiting_for_correct_guess = True
    while waiting_for_correct_guess:
        user_input = get_number_from_user()
            
        if user_input == random_number:
            print("You guessed the number!  Good job!")
            waiting_for_correct_guess = False
        if user_input > random_number:
            print("Your guess is too high")
        if user_input < random_number:
            print("Your guess is too low")
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")

```

</details>

Now let's work on the version with a maximum number of guesses.  At first glance this seems like a good candidate for a for loop because we have a max number of times we're going to run the loop, but let's dig into the actual sequence.  We want to run the loop at most the max guesses number of times, but if the user guesses the number correctly we want to end the loop early.  It is possible to end a loop early using the `break` statement but as a general rule for readability it is better to write meaningful loops that will only execute the number of times you want them to.  In this case, a more complex while loop conditional statement along with a counter variable will result in a loop that does exactly what we want and also is easy to read and understand.  Start by adding a counter variable `num_guesses` and increment inside of the while loop:

```python

def guess_the_number():
    # ...
    num_guesses = 0
    while waiting_for_correct_guess:
        num_guesses += 1 # if you are unfamiliar with the += operator, it is the same as num_guesses = num_guesses + 1
        # ...

```

Next, add a max guesses constant to the other constants at the top of the file and set it to whatever you like.  In our example we will use 20.  Then add a comparision in the while loop to check to see if the current number of guesses is greater than or equal to the max guesses (on our first time through the loop the number of guesses starts at 0, so by the time we get to the max number of guesses we've already guessed that many times):


```python

# ...
MAX_GUESSES = 20
# ...
def guess_the_number():
    # ...
    
    num_guesses = 0
    while waiting_for_correct_guess or num_guesses >= MAX_GUESSES:
        num_guesses += 1 # if you are unfamiliar with the += operator, it is the same as num_guesses = num_guesses + 1
        # ...

```

Last, let's add some feedback to the user to let them know what's going on!

```python

MAX_GUESSES = 20

def guess_the_number():

    random.seed()
    random_number = random.randrange(RANGE_LOW, RANGE_HIGH)
    waiting_for_correct_guess = True
    num_guesses = 0
    while waiting_for_correct_guess or num_guesses >= MAX_GUESSES:
        print(f"You have {MAX_GUESSES - num_guesses} left!")
        num_guesses += 1
        user_input = get_number_from_user()
        if user_input == random_number:
            print("You guessed the number!  Good job!")
            waiting_for_correct_guess = False
        if user_input > random_number:
            print("Your guess is too high")
        if user_input < random_number:
            print("Your guess is too low")
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")
    
    # At this point, there are two options.  1, the user ran out of guesses or 2. they got the correct answer.  
    # We need to let them know if they ran out of guesses, but if we check if num_guesses is >= MAX_GUESSES we could
    # be wrong, because they might have gotten the correct answer on the last try!  If we check waiting_for_currect_guess
    # we will get the answer we want - did they ever guess the correct answer before they were booted out of the loop.  Also, if they
    # got the correct answer, they were given feedback about that inside the loop, so there's no need to do anything here in that case.
    if waiting_for_correct_guess:
        print(f"You ran out of guesses!  The correct answer was {random_number}.")

```

Check the last assumption that we made that we only need to check `waiting_for_correct_guess` to give the user the "You ran out of guesses" feedback.  It seems like we're checking the wrong variable!  In cases like this it can be useful to "be the computer" and run through the code manually.  Write down the state of the variables at each pass through the loop and make sure that the loop is doing what you think it is doing.  Does the waiting_for_correct_guess variable give us the information that we think it does in every situation?  Walk through the code with various possibilities (we call these test cases, a possible list is first, the user guesses correctly, second, the user doesn't guess and runs out of guesses, and last, the user guesses correctly on the last try) and confirm for yourself that the code works.

### Guess the Number is Done..?

You have built a fully functional command line game!  If this is the first time you've done something like this, congratulations!  Go bug everybody you know and make them play it!  We will not be expanding the game further in these lessons, but if you are looking for a project to work on, this game can be a great jumping off point.  Consider adding options for the user to set the range for random number or the number of guesses.  What would be involved in turning it into a two player game where each player has a limited number of guesses?  

## Snowman

### Same Problem, New Context

In programming you will quickly discover that many problems that look different are at the core the same problem, just with different details.  You can use this to your advantage in your work, because programmers love to ask and answer questions.  Sites like stackoverflow.com are a great resource for new programmers, because chances are if you're stuck on a problem, someone else has been stuck on a similar problem and their solution can help you get to your solution.

We're going to switch now to working on Snowman.  First, let's take a look at the current version of our user input function `get_letter_from_user`:

```python

def get_letter_from_user():
    user_input_string = input("Guess a letter: ")
    if not user_input_string.isalpha():
        print("You must input a letter!")
    elif len(user_input_string) > 1:
        print("You can only input one letter at a time!")

    return user_input_string

```

The problem here is the same as `get_number_from_user`, except instead of a number we want to continue to ask the user for a letter until they give us a single letter.  Add a while loop to this function and submit it here:

[python test input]

When you get [FEEDBACK OF SOME KIND THAT INDICATES IT WORKS], move on to the next section.

### Tracking User Input 

Imagine you were playing a game of Snowman with a group of children.  You would probably keep track of the letters that they guessed, and with correct letters you would add to the word and with incorrect you would add to the snowman drawing.  As with all code projects, this project is going to build on itself, so the next step toward that final fully functional version is to keep track of the number of correct and incorrect guesses from the user.  In this version we are not going to compare their guesses to their previous guesses, so if they guess the same incorrect letter multiple times we'll count it as a new wrong guess every time.  Start by adding a loop to the main `snowman()` function similar to the loop inside of `guess_the_word`.  Set up two counters, for example `correct_guesses` and `wrong_guesses`, outside of the while loop, and allow the user to continue to guess until they reach a maximum number of incorrect guesses.  Remember, we're only solving part of the problem here!  Keep track of the number of incorrect and correct guesses in the loop.  Submit your code here:

[python test input]

When you get [FEEDBACK OF SOME KIND THAT INDICATES IT WORKS], move on to the next section.

### Drawing Pictures [TODO]