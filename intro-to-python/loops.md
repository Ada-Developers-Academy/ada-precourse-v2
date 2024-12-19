# Loops

<!-- PRECOURSE UPDATE -->
<!-- <iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=6dbde348-1f6b-46fe-9ea8-acb80025d2b6&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe> -->

## Learning Goals

At the end of this lesson students will be able to:

- Understand and use `while` loops
- Understand and use `for` loops

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1m9h053kS6bjAeiHnEHIP39fqbyOO7glc?usp=sharing)

In this section we will be building on the code that you wrote in the lesson [Helper Functions](helper-functions.md). If you would like to look at our example code for that lesson, you can find it [here](resources/src/functions/games_function.md).

## Vocabulary and Syntax

| Vocab | Definition | Synonyms | How to Use in a Sentence |
| -- | -- | -- | -- |
| while loop | A loop that repeats a code block inside it as long as its conditional statement evaluates to `True`. The statement is tested before executing the code block inside the loop. | sentinel controlled loop, pre-test loop | "The code in the while loop will run as long as the test is true." |
| for loop | A loop that _iterates_ a certain number of times or repeats over a sequence. In Python it is often used to iterate over a `list` data structure. It is also commonly paired with the `range` [function](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#ranges), which returns a list of numbers. The `for` loop repeats n times, where n is the length of the sequence being looped over. | counter controlled loop | "To repeat the code five times we will use a for loop." |
| flag | A variable that is used to indicate that a condition has been met. Usually a flag is a boolean variable and the value is changed to indicate that the goal or target (whatever the condition is) has been achieved. | signal | "The while loop will stop when the value of the flag is changed from `True` to `False`." |

### Loop Examples

Hypothesize the outputs for each of the different loops below.

```python
# Example 1: while loop
counter = 0
while counter < 10:
    counter = counter + 2
    print(f"The value of counter is {counter}")
```

```python
# Example 2: while loop with flag
keep_running = True
counter = 0
while keep_running:
    counter = counter + 3
    if counter > 10 :
        keep_running = False
    print(f"The value of counter is {counter}")
```

```python
# Example 3: another while loop with flag
ask_for_input = True 
while ask_for_input: 
    user_input = input("Do you want to keep running? Enter 'y' or 'n': ") 
    ask_for_input = (user_input == 'y')
```

```python
# Example 4: for loop using range with implicit start
for number in range(3):
    print(f"The value of num is {number}")
```

```python
# Example 5: for loop using range with explicit start and stop
for number in range(2, 5):
    print(f"The value of num is {number}")
```

```python
# Example 6: for-in loop over a collection
a_string = "Hello, World!"
for letter in a_string:
    print(f"The current letter is {letter}")
```

## `while` Loops

While loops are handy when we don’t know how many times we need to perform an action. They check if a condition is true and continue to loop until that condition evaluates to false. This condition statement could be a complex logic expression, or it could be a single boolean variable that we treat as a flag and set to `False` when we’re ready to stop.

We declare a while loop with the `while` keyword, followed by the condition we want to evaluate, then a colon:

```python
while <condition>:
    # Take actions inside the loop if the condition is true
```

With that in mind, let’s take another look at the third while loop we saw above.

```python
ask_for_input = True 
while ask_for_input: 
    user_input = input("Do you want to keep running? Enter 'y' or 'n': ") 
    ask_for_input = (user_input == 'y')
```

In this example, we set up a flag called `ask_for_input` with the value set to `True` indicating that we should as a user for input. While this variable's value is `True`, the loop's body will execute and ask a user for input. After a user enters some input, either "y" or "n", we compare the value of `user_input` to the string "y". When we use `==` to compare if two values are equal to each other, the result of that comparison will be a boolean value. 

If `user_input` references "n" and we compare that variable to the string "y", then the return value of this comparison is `False`. If `user_input` references "y" and we compare that variable to the string "y", then the return value of this comparison is `True`.

Therefore, in the loop's body the flag called `ask_for_input` gets re-assigned the boolean value from comparing `user_input` with "y". If the flag's value remains `True` then the loop will continue to run. If the user entered 'n', which means that `user_input` does not equal 'y', then `ask_for_input` will be re-assigned the value `False` and the loop will stop running. 

## `for` Loops

For loops let us loop over a fixed sequence, commonly a sequence of numbers, letters in a string, or items in a data structure. This makes them our preferred choice when we know how many times we want to take an action.

For loops need a little bit more information than a while loop. While this makes the syntax of the loop itself a little more involved, on the other hand it means that all the information needed for the loop is collected in one place, making it a little more difficult to make mistakes!

We declare a for loop using the `for` keyword, followed by a variable name (which we use inside the loop body to refer to each iterated value), then the keyword `in`, followed by the iterable expression we are iterating over, and capped off with a colon:

```python
for <variable_name> in <iterable_expression>:
    # Do something with <variable_name>
```

Say we want to print "Hello!" 3 times. When we know the exact number of times to take an action, we can use the `range` function to give us a list of numbers to iterate over. `range` has some helpful options, if we pass it a single integer parameter, `range` will generate a sequence from 0 to the number we passed _exclusive_. This means if we call `range(3)` it will create the sequence `[0, 1, 2]`, it _excludes_ 3. If we use this with a for loop, it would look something like this:

```python
for number in range(3):
    print("Hello!")
    print(f"The value of number is {number}")

# When run, this code will output:
# Hello!
# The value of number is 0
# Hello!
# The value of number is 1
# Hello!
# the value of number is 2
```

If we need to perform work a specific number of times, but we don't want our count to start at 0, `range` still has us covered. We can define the start of our number sequence by passing `range` two parameters, the number we want to start at (inclusive) and where we want to end (exclusive). For example, if we call `range(2,5)` it will give us the number sequence `[2, 3, 4]`, 2 is included but 5 is excluded. Using this version of `range` in a for loop, we can do the following:

```python
for number in range(2, 5):
    print(f"The value of number is {number}")

# When run, this code will output:
# The value of number is 2
# The value of number is 3
# the value of number is 4
```

In the while loop section above, the first example is a while loop that runs exactly 5 times. Since we know how many times the loop's logic should execute, we can refactor this while loop into a ranged for loop. Because a for loop iterates over values, we can also remove the `counter` variable.

We've seen through examples that the default behavior for `range` is to create a list by increasing our starting value by one until the upper limit is reached. However, we can pass a third argument to `range` which tells it how many steps to increment by each time. We can generate the list of values we need to refactor our while loop example by calling `range(2, 11, 2)`. This will give us a number sequence that starts at 2, increases by 2 for each time, and stops when our limit 11 (which is always excluded) is reached: `[2, 4, 6, 8, 10]`. Putting it all together, that loop looks like:

```python
for number in range(2, 11, 2):
    print(f"The value of number is {number}")

# When run, this code will output:
# The value of number is 2
# The value of number is 4
# The value of number is 6
# The value of number is 8
# The value of number is 10
```

We won't go further into iterating over lists here since we'll learn more about them in the next lesson, but it's helpful to know that we can use for loops to inspect each item in a list of values and perform some action with it:

```python
word_list = ["Hello", "world"]
for word in word_list:
    print(f"The current word is {word}")

# When run, this code will output:
# The current word is Hello
# The current word is world
```

## Practice Problems

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 9a27d597-95f0-4a9b-8736-807140aadfbc
* title: Constant Loop
* points: 1
* topics: python, loops

##### !question

Write a function `print_ten` that takes one argument, a string.  The function has the following behavior:
* The function returns a string that repeats a counter number (starting at 1) and then the string ten times
* The function can use either a while loop or a for loop, but it must use a loop

Example inputs and outputs:

|input|output|
|--|--|
| `word = "snow"`|`"1 snow 2 snow 3 snow 4 snow 5 snow 6 snow 7 snow 8 snow 9 snow 10 snow "`|
| `word = ""`|<code>"1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5&nbsp;&nbsp;6&nbsp;&nbsp;7&nbsp;&nbsp;8&nbsp;&nbsp;9&nbsp;&nbsp;10&nbsp;&nbsp;"</code>|
| `word = "123"`|`"1 123 2 123 3 123 4 123 5 123 6 123 7 123 8 123 9 123 10 123 "`|

##### !end-question

##### !placeholder

```python
def print_ten(word):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
from main import print_ten

class TestPrintTen(unittest.TestCase):
    def test_word(self):
        self.assertEqual(print_ten("snow"),"1 snow 2 snow 3 snow 4 snow 5 snow 6 snow 7 snow 8 snow 9 snow 10 snow ")

    def test_empty(self):
        self.assertEqual(print_ten(""), "1  2  3  4  5  6  7  8  9  10  ")

    def test_string(self):
        self.assertEqual(print_ten("123"), "1 123 2 123 3 123 4 123 5 123 6 123 7 123 8 123 9 123 10 123 ")
```

##### !end-tests

<!--optional-->

##### !explanation

Two examples of working implementations:

```python
def print_ten(word):
    count = 1
    result = ""
    while count < 11:
        result += str(count)
        result += " "
        result += word
        result += " "
        count += 1

    return result

def print_ten(word):
    result = ""
    for i in range(1, 11):
        result += str(i) + " "
        result += word + " "
    return result
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 648f56bd-9879-46f2-af82-94d962d51d13
* title: Variable Loop
* points: 1
* topics: python, loops

##### !question

Write a function `print_multiple` that takes two argument, a string `word` and a number `amount`.  The function has the following behavior:
* The function returns a string that repeats a counter number (starting at 1) and then the string `amount` number of times
* The function can use either a while loop or a for loop, but it must use a loop

Example inputs and outputs:

|input|output|
|--|--|
| `word = "snow"`<br/> `amount = 4`|`"1 snow 2 snow 3 snow 4 snow"`|
| `word = ""` <br/> `amount = 7`|<code>"1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5&nbsp;&nbsp;6&nbsp;&nbsp;7 "</code>|
| `word = "123"` <br/> `amount = 11`|`"1 123 2 123 3 123 4 123 5 123 6 123 7 123 8 123 9 123 10 123 11 123"`|

##### !end-question

##### !placeholder

```python
def print_multiple(word, amount):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
from main import print_multiple

class TestPrintMultiple(unittest.TestCase):
    def test_word(self):
        self.assertEqual(print_multiple("snow", 4),"1 snow 2 snow 3 snow 4 snow")

    def test_empty(self):
        self.assertEqual(print_multiple("", 7), "1  2  3  4  5  6  7 ")

    def test_string(self):
        self.assertEqual(print_multiple("123", 11), "1 123 2 123 3 123 4 123 5 123 6 123 7 123 8 123 9 123 10 123 11 123")
```

##### !end-tests

<!--optional-->

##### !explanation

Two examples of working implementations:

```python
def print_multiple(word, amount):
    count = 1
    result = ""
    while count < amount + 1:
        if count > 1:
            result += " "
        result += str(count)
        result += " "
        result += word
        count += 1

    return result

def print_multiple(word, amount):
    result = ""
    for i in range(1, amount + 1):
        if i > 1:
            result += " "
        result += str(i) + " "
        result += word
    return result
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Guess the Number Project

In our previous work on this project, we built some solid functionality, but it isn't very game-like yet. Now we're going to use loops to add complexity and build more interactivity. Open up your `game.py` and let's get started!

### Validating User Input

In the previous lesson, we pulled the user input into its own function, while acknowledging that we weren't actually doing the work of validating the input. We let the user know that the input is not good, but then we just return it:

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

What we really want to do in this function is to compel the user to give us valid input, and only return our input when it is valid. We can't really force the user to give us valid input, but what we can do is repeat the process of asking for input until we get something that is valid (or just keep asking forever). In cases like this, where we need to repeat a process but there is uncertainty about how many times we will do so, a while loop is the ideal tool to use.

To solve this problem we are going to use a flag controlled while loop. A "flag" is a term for a boolean variable that is set before we enter the loop, and then at some point will be flipped inside the loop to signal that the loop should end (and that whatever action the loop was trying to accomplish has been completed).

Add a while loop with a flag to the `get_number_from_user` function to continue to loop until the user gives valid input.  

<br>

<details>
<summary>Once you have finished, click here to compare your solution to ours.</summary>

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

Notice that our solution uses a `not` in the while test. This operator negates, or inverts, a boolean value. We could use a flag that is set it to `True`, and then when we get valid input set it to `False`. Think about the readability of our code in that case. It would not make sense to have a variable named `valid_input` set to `True`, if we are trying to get a valid input at the end (starting with flag that is `True` then setting it to `False` makes it seem like we're not getting valid input). Changing the variable name to something like `attempting_valid_input` would work better to make the code readable. In that case, the code would look like this:

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

**As an aside, variable names can make or break the readability of code!**

</details>

### Keep the Guessing Game Going!

Now that we have a way to get valid input from the user, it's time to take a look at the `guess_the_number` function. There are two ways to play this type of guessing game, the first is with unlimited guesses and the second is with a maximum number of guesses. Let's start with the first version with unlimited guesses. The current version of the function is:

```python
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    user_input = get_number_from_user()

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print("Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number! Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")
```

Add a while loop with a flag that tests to see if the user has guessed the correct number.

<br>

<details>
<summary>When you are finished, compare your code to our version here.</summary>

```python
def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    waiting_for_correct_guess = True

    while waiting_for_correct_guess:
        user_input = get_number_from_user()

        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number! Good job!")
            waiting_for_correct_guess = False
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")
```

</details>

Now let's work on the version with a maximum number of guesses. At first glance this seems like a good candidate for a for loop because we have a maximum number of times we're going to run the loop, but let's dig into the actual sequence.

We want to run the loop at most the same number of times as the number of maximum guesses, but if the user guesses the number correctly before reaching the maximum number of guesses we want to end the loop early. In this case, we do not actually know how many times the loop should run so a more complex while loop conditional statement along with a counter variable will result in a loop that does exactly what we want and also is easy to read and understand.

1.  First, add a counter variable `num_guesses` and increment it inside of the while loop:

    ```python
    def guess_the_number():
        # ...
        num_guesses = 0

        while waiting_for_correct_guess:
            # the += operator is the same as num_guesses = num_guesses + 1
            num_guesses += 1
            # ...
    ```

2.  Next, add a constant variable to represent the maximum guesses underneath the other variable at the top of the file and set it to any integer value (in our example we will use 20.) Then add a comparison in the while loop to check to see if the current number of guesses is greater than or equal to the maximum number of guesses (on our first time through the loop the number of guesses starts at 0, so by the time we get to the maximum number of guesses we've already guessed that many times):

    ```python
    # ...
    MAX_GUESSES = 20
    # ...
    def guess_the_number():
        # ...

        num_guesses = 0
        while (waiting_for_correct_guess and num_guesses <= MAX_GUESSES):
            num_guesses += 1
            # ...
    ```

3.  Lastly, let's add some feedback to the user to let them know what's going on!

    ```python
    MAX_GUESSES = 20

    def guess_the_number():
        random_number = random.randint(RANGE_LOW, RANGE_HIGH)

        waiting_for_correct_guess = True
        num_guesses = 0

        while (waiting_for_correct_guess and num_guesses <= MAX_GUESSES):

            num_guesses += 1
            user_input = get_number_from_user()

            if user_input == random_number:
                print("You guessed the number! Good job!")
                waiting_for_correct_guess = False
            elif user_input < RANGE_LOW or user_input > RANGE_HIGH:
                print("Your guess is out of bounds.")
                print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
            elif user_input > random_number:
                print("Your guess is too high")
            elif user_input < random_number:
                print("Your guess is too low")

        # At this point, there are two options.
        #    1. the user ran out of guesses or
        #    2. they got the correct answer.
        # We need to let them know if they ran out of guesses,
        # but if we check if num_guesses is >= MAX_GUESSES we could
        # be wrong, because they might have gotten the correct answer
        # on the last try!  If we check waiting_for_correct_guess
        # we will get the answer we want - did they ever guess the
        # correct answer before they were booted out of the loop.  Also, if they
        # got the correct answer, they were given feedback about that
        # inside the loop, so there's no need to do anything here in that case.
        
        if waiting_for_correct_guess:
            print(f"You ran out of guesses! The correct answer was {random_number}.")

    # Call the function to test it
    guess_the_number()
    ```

    Execute the code in `game.py`. Check the last assumption that we made – that we only need to check `waiting_for_correct_guess` to give the user the "You ran out of guesses" feedback. It seems like we're checking the wrong variable! In cases like this it can be useful to "be the computer" and run through the code manually. Write down the state of the variables at each pass through the loop and make sure that the loop is doing what we think it is doing. Does the `waiting_for_correct_guess` variable give us the information that we think it does in every situation? Walk through the code with the following various possibilities, also known as "test cases": 
    * The user guesses correctly
    * The user doesn't guess correctly and runs out of guesses
    * The user guesses correctly on the last try
   
    Confirm that the code works according to the requirements for the test cases outlined above.

### Guess the Number is Done..?

You have built a fully functional command line game! If this is the first time you've done something like this, congratulations! Go bug everybody you know and make them play it! We will not be expanding the game further in these lessons, but if you are looking for a project to work on, this game can be a great jumping off point. Consider adding options for the user to set the range for random number or the number of guesses. What would be involved in turning it into a two player game where each player has a limited number of guesses?

## Snowman Project

### Same Problem, New Context

In programming, many problems that look different are at the core the same problem just with different details. We can use this to our advantage in our work! If we identify that a problem is similar to one we have already solved, we can take the solution we've already written and modify it for the new problem.

We're going to switch now to working on Snowman.  Start by opening up `snowman.py` in VSCode.  First, let's take a look at the current version of our user input helper function `get_letter_from_user`:

```python
def get_letter_from_user():
    user_input_string = input("Guess a letter: ")

    if len(user_input_string) > 1 or not user_input_string.isalpha():
        print("Invalid letter please enter a single character.")
    
    return user_input_string
```

The problem here is the same as `get_number_from_user`, except instead of a number we want to continue to ask the user for a letter until they give us a single letter. Add a while loop to `get_letter_from_user` so that the function will continue to run until a user provides a single letter when prompted for input. If we run into bugs or our code is not running as we expect it to, we can add debugging print statements in our function to see the values of variables in order to reason about what is going on. Be sure to execute the code with the `python3` command from the terminal and check if the refactored code works as expected. 

<br>

<details>
<summary>When you are finished compare your version with ours.</summary>

```python
def get_letter_from_user():
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        else:
            valid_input = True

    return user_input_string

# Call the method to test out the new functionality 
get_letter_from_user()
```

</details>

### Tracking User Input

Imagine we are playing a game of Snowman with several players.  We would probably keep track of the letters that they guessed, and given a correct letter we would add to the word and with an incorrect letter we would add to the snowman drawing.

 In this version we are going to keep track of the number of correct and incorrect guesses from the user. If the user guesses the same incorrect letter multiple times we'll count it as a new wrong guess every time. For the moment, we will be doing the same thing with correct guesses - we will end the loop if the user makes as many correct guesses as the length of the word even if they guess the same letter repeatedly. We will update this functionality this in a future lesson. 
 
 In `snowman.py` make changes to the `snowman` function according to the requirements below:
1.  Add a loop to the main `snowman` function similar to the loop in `guess_the_number`.  
2.  Add two counters `correct_guesses` and `wrong_guesses`.
3.  Adjust the loop to allow the user to continue to guess until they reach 7 `SNOWMAN_MAX_WRONG_GUESSES`. If the number of `correct_guesses` is equal to the length of `SNOWMAN_WORD` then that means the word has been guessed and the user should no longer be able to submit guesses. 
4.  Use the helper function `get_letter_from_user` to get user input in the loop.
5.  Track the number of correct and incorrect guesses, adding one to the proper counter when the user makes a guess.
6.  We no longer need to return `True` or `False` in the `snowman` function so we can remove that code from the function

When finished print out, "You made X correct and Y incorrect guesses" where X and Y are the number of correct and incorrect guesses.

Use the debugging techniques we have discussed and execute `snowman.py` to test that your solution works according to the requirements.

<br>

<details>
<summary>When you are finished compare your version of <code>snowman.py</code> with ours.</summary>

```python
SNOWMAN_WORD = "broccoli"
SNOWMAN_MAX_WRONG_GUESSES = 7

def get_letter_from_user():
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        else:
            valid_input = True

    return user_input_string

def snowman():
    correct_guesses = 0
    wrong_guesses = 0

    while wrong_guesses < SNOWMAN_MAX_WRONG_GUESSES and correct_guesses < len(SNOWMAN_WORD):
        user_input = get_letter_from_user()
        if user_input in SNOWMAN_WORD:
            print("You guessed a letter that's in the word!")
            correct_guesses += 1
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses += 1
    
    print(f"You made {correct_guesses} correct and {wrong_guesses} incorrect guesses")

snowman()
```

</details>

### Drawing Pictures

Add these string ASCII snowman drawings as constant variables to the top of `snowman.py`. Notice that the number of constant variables that make up the drawing is the same as SNOWMAN_MAX_WRONG_GUESSES. For each wrong guess, we will want to add a new element to the drawing:

```python
SNOWMAN_0 = '*   *   *  '
SNOWMAN_1 = ' *   _ *   '
SNOWMAN_2 = '   _[_]_ * '
SNOWMAN_3 = '  * (")    '
SNOWMAN_4 = '  \\( : )/ *'
SNOWMAN_5 = '* (_ : _)  '
SNOWMAN_6 = '-----------'
```

The value of `SNOWMAN_4` may look like it's one character off from the other values. From the textbook section for [Variables and IO](variables-and-io.md), remember that the backslash `\` character acts as an "escape" character within strings. Normally, this tells Python that the character following the backslash should be treated specially. But in this case, we don't want the parenthesis `(` to be treated specially—it has no special meaning when escaped. Rather, we want to print the backslash (the arm) and the parenthesis (the body). To do this, we need to escape the backslash itself. So, to print a backslash in a string, we need to use two backslashes `\\`. This is why the value of `SNOWMAN_4` is <code>'&nbsp;&nbsp;\\\\(&nbsp;:&nbsp;)/&nbsp;*'</code>.

### !callout-info

## Zero-Based Counting

Notice that the variable names for the element of the snowman drawing starts at 0 with the variable `SNOWMAN_0` and ends at 6 with the variable `SNOWMAN_6`. Often times in programming we use zero-based counting.  We'll dive more into this concept when we go over lists. For now, we'll proceed with our implementation of drawing a snowman based on counting from 0 upwards. So in our game, if a user has 7 guesses then we'd count the guesses like 0, 1, 2, 3, 4, 5, 6.  

### !end-callout

Our end goal is to have a helper function called `print_snowman` that we can pass the current `wrong_guesses` value to and it will draw the appropriate amount of the snowman.  Let's start by writing `print_snowman` which will have a parameter called `wrong_guesses_count` which will draw a specific element of the snowman based on a passed value.  For example, if we pass the function 0, we want the function to draw SNOWMAN_0.  This will seem slightly contrived, but it is just a starting place.

<br> 

<details>
<summary>Once you've written <code>print_snowman</code>, run your code to see how it works and then compare what you have to our version.</summary>

```python
def print_snowman(wrong_guesses_count):
    if wrong_guesses_count == 0:
        print(SNOWMAN_0)
    elif wrong_guesses_count == 1:
        print(SNOWMAN_1)
    elif wrong_guesses_count == 2:
        print(SNOWMAN_2)
    elif wrong_guesses_count == 3:
        print(SNOWMAN_3)
    elif wrong_guesses_count == 4:
        print(SNOWMAN_4)
    elif wrong_guesses_count == 5:
        print(SNOWMAN_5)
    elif wrong_guesses_count == 6:
        print(SNOWMAN_6)
```

</details>

Now we're going to add a loop inside the `print_snowman` function to make it draw not just one element of the snowman, but all the elements we want. We want to draw our snowman from the ground up, so if we have only 1 incorrect guess, we want to print the last element, if we have 2 incorrect guesses we want to print the last two elements, and so on. Our function should take in the number of incorrect guesses and use that value with the `range` function to draw the elements of the snowman in the order that we want.

Unlike our other loops so far, we're not going to use a `while` loop, this time we're going to use a `for` loop. A `for` loop is a great tool when we know exactly how many times we're going to be executing our loop.

Start by adding a `for` loop 

* Use the `range()` function with the `for` loop.
* With the `range()` function, we want to provide start and end values so that we only loop over a specific range according to the number of incorrect guesses a user has made
* We will calculate the start and end values using `wrong_guesses_count`

### !callout-info

## The Range Function is Exclusive
The range function is _exclusive_, which means it goes up to but does not include the last element of the given range. This means that `range(1, 8) = [1, 2, 3, 4, 5, 6, 7]`

### !end-callout

  <details>
  <summary> When you have updated <code>print_snowman</code>, compare what you have to our version.</summary>

  ```python
  def print_snowman(wrong_guesses_count):
      for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
          if i == 0:
              print(SNOWMAN_0)
          elif i == 1:
              print(SNOWMAN_1)
          elif i == 2:
              print(SNOWMAN_2)
          elif i == 3:
              print(SNOWMAN_3)
          elif i == 4:
              print(SNOWMAN_4)
          elif i == 5:
              print(SNOWMAN_5)
          elif i == 6:
              print(SNOWMAN_6)
  ```

   </details>

Finally, inside of the `snowman` function, let's remove the print statement at the end of the function. For user feedback, inside the while loop we'll add the `print_snowman` function call to print out the current state of the snowman to the user after each guess.

  ```python
  def snowman():
      correct_guesses = 0
      wrong_guesses = 0

      while wrong_guesses < SNOWMAN_MAX_WRONG_GUESSES and correct_guesses < len(SNOWMAN_WORD):
          user_input = get_letter_from_user()
          if user_input in SNOWMAN_WORD:
              print("You guessed a letter that's in the word!")
              correct_guesses += 1
          else:
              print(f"The letter {user_input} is not in the word")
              wrong_guesses += 1
                                                  
          print_snowman(wrong_guesses)
  ```

Execute `snowman.py` and test out the game!

## Summary

Loops are incredibly powerful.  By adding a few loops we have transformed our Guess the Number code into a fully functional game!  We have also added core functionality to Snowman.  In the next lesson we will use the `list` data structure to add functionality to our Snowman game. 