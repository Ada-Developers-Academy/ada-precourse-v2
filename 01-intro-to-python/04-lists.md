# Lists

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=5a85cd50-b866-4aa4-a5e3-acb8005d04be&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand lists
    * Create new lists
    * Add elements to lists
    * Access elements of lists
    * Search lists for elements
* Combine lists and loops

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1TK9Enhh0mITZ1649l-r4_gzeg2B3eRRu?usp=sharing)

In this section we will be building on the code you wrote in the previous lesson [Loops](03-loops.md).  If you would like to look at our example code for that lesson, you can find it [here](resources/src/03-loops/game-loop.md).

### Introducing Lists, Our First Data Structure!

Variables are awesome!  We can store data, retrieve it, update it and use it in any way we like.  So far, though, are variables have been limited because they have only been able to hold one piece of data.  Imagine we want to write a program to ask for and then display the user's top five favorite flavors of ice cream.  We can store each flavor in it's own variable and then use those variables in our display.  

What happens when we want to modify our program to store our user's top 10 favorite flavors?  We would have to add more variables and update the program to use those new variables.  _Lists_ change all of this!  Lists are a _data structure_ that can hold multiple pieces of data and we can access the data numerically starting with 0.  Lets go back to our ice cream example.  If we use a list to store our ice cream flavors, we can use one variable and then as our user inputs their favorite flavors, we can add the new flavor to the list!  

By using a list, we can store as many ice cream flavors as we want.  Also, python provides us with ways to easily loop through all of the elements in a list so we can use a loop to display all of the flavors, which will simplify our code even further!  

```python

def favorite_flavors():
    icecream_flavors = []
    flavor = ""
    while not flavor == "done": # this loop will run until the 
                                # user types in the word "done"
        flavor = input("What is an icecream flavor that you like? ")
        icecream_flavors.append(flavor) # when we append something to a list,
                                        # we add it to the end of the list
    
    for flavor in icecream_flavors: # this loop will iterate over each element 
                                    # in the list, and store them one at a time 
                                    # in the variable flavor
        print(f"{flavor} is a great ice cream flavor!")

    return icecream_flavors

```


## Vocabulary and Syntax

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| data structure| A collection of data that follows a set of rules for modifying and accessing the data.  Python provides four built in data structures, _lists_, _dictionaries_, _tuples_ and _sets_.  This curriculum will cover lists and dictionaries.     | Collection      | "We organize our collection of students into a list data structure" |
| list      | a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key | Array | "We loop through the list and print out each value"    |
| index      |The position of an element in a _sequence type_, that is, a type that stores data in order.  In Python, strings and lists are examples of sequence types.  In Python indexes start at 0. | Key | "We get the 1st element at index 0."    |
| package      | A collection of modules distributed together  | Egg | "The wonderwords package can give us random words."    |
|  module      | A file containing python code.  | Library | "This module has functions for calculating taxes."    |

```python

# list syntax
# creating a new list:
new_list = []
new_list_2 = ["lemon", "vanilla", "chocolate"]

# adding an element to a list:
new_list_2.append("caramel")
# new_list_2 = ["lemon", "vanilla", "chocolate", "caramel"]

# accessing an element of a list
new_list_2[0]
# "lemon"
new_list_2[3]
# "caramel"

# looping through a list
for i in new_list_2:
    print(i)

# output:
# lemon
# vanilla
# chocolate
# caramel

```

## Practice Problems
<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 610f0431-b999-420f-8088-a40f5ddf9167
* title: Find Index of Item in List
* points: 1
* topics: python, lists

##### !question

Write a function `find_index_of_item` that takes two variables, an item and a list called list_of_items.  The function has the following behavior:
* If the list contains the item, the function returns the index of the item in the list.  
* If the list contains the item multiple times, the function returns the index of the first time the item appears in the list.  
* If the list does not contain the item, the function returns -1.

Example inputs and outputs:

input: ```find_index_of_item(3, [1, 4, 5, 6, 2, 3, 9])```  
output: ```5```

input: ```find_index_of_item("cat", ["dog", "cow", "goat", "pig"])```  
output: ```-1```

input: ```find_index_of_item("chocolate", [])```  
output: ```-1```

input: ```find_index_of_item(-93, [1, 30, -93, 99, -3, -93, 25, 16])```  
output: ```2```

##### !end-question

##### !placeholder

```python

def find_index_of_item(item, list_of_items):
    return None

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import *

class TestFindIndexOfItemChallenge(unittest.TestCase):
    def test_find_success(self):
        self.assertEqual(find_index_of_item(3, [1, 4, 5, 6, 2, 3, 9]), 5)
    
    def test_find_first(self):
        self.assertEqual(find_index_of_item(-93, [1, 30, -93, 99, -3, -93, 25, 16]), 2)
    
    def test_find_failure(self):
        self.assertEqual(find_index_of_item("cat", ["dog", "cow", "goat", "pig"]), -1)
    
    def test_find_failure_empty_list(self):
        self.assertEqual(find_index_of_item("chocolate", []),-1)

```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Loop over list_of_items
1. Compare each element in list_of_items to item
1. If an element in list_of_items matches item, return the index of that element
1. If no matching element is found, return -1

##### !end-hint

<!--optional-->
##### !explanation
Three examples of working implementations:

```python
def find_index_of_item(item, list_of_items):
    default = -1
    for count, current_item in enumerate(list_of_items):
        if current_item == item:
            return count
    return default

def find_index_of_item(item, list_of_items):
    default = -1
    count = 0
    for current_item in list_of_items:
        if current_item == item:
            return count
        count += 1
    return default

def find_index_of_item(item, list_of_items):
    default = -1
    count = 0
    while count < len(list_of_items):
        if list_of_items[count] == item:
            return count
        count += 1
    return default
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 57d4bc1e-eb50-40bd-b6cb-680e4529f146
* title: Count Occurrences of Item in List
* points: 1
* topics: python, lists

##### !question


Write a function `count_item_in_list` that takes two variables, an item and a list called list_of_items.  The function has the following behavior:
* The function returns the number of times the item appears in the list 
* If the list does not contain the item, the function returns 0 .

Example inputs and outputs:

input: ```count_item_in_list(3, [1, 3, 3, 6, 2, 3, 9])```  
output: ```3```


input: ```count_item_in_list("cat", ["dog", "cow", "goat", "pig"])```  
output: ```0```


input: ```count_item_in_list(38, [])```  
output: ```0```


input: ```count_item_in_list("dog", ["dog", "cat", "cow", "goat", "pig"])```  
output: ```1```

<!--This can be regular **Markdown**-->

##### !end-question

##### !placeholder


```python

def count_item_in_list(item, list_of_items):
    return None

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import *

class TestCountItemInListChallenge(unittest.TestCase):
    def test_find_multiple(self):
        self.assertEqual(count_item_in_list(3, [1, 3, 3, 6, 2, 3, 9]), 3)
    
    def test_find_none(self):
        self.assertEqual(count_item_in_list("cat", ["dog", "cow", "goat", "pig"]), 0)
    
    def test_find_empty_list(self):
        self.assertEqual(count_item_in_list(38, []), -0)
    
    def test_find_one(self):
        self.assertEqual(count_item_in_list("dog", ["dog", "cat", "cow", "goat", "pig"]), 1)

```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Loop over list_of_items
1. Compare each element in list_of_items to item
1. If an element in list_of_items matches item, increment a counter
1. Return the counter
1. If no matching elements are found, return 0

##### !end-hint

<!--optional-->
##### !explanation

Three examples of working implementations:

```python

def count_item_in_list(item, list_of_items):
    count = 0
    for current_item in list_of_items:
        if current_item == item:
            count += 1
    return count

def count_item_in_list(item, list_of_items):
    count = 0
    for index in range(len(list_of_items)):
        if list_of_items[index] == item:
            count += 1
    return count

def find_index_of_item(item, list_of_items):
    count = -1
    index = 0
    while index < len(list_of_items):
        if list_of_items[count] == item:
            count += count
        index += 1
    return count

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 555531b1-7ebc-4129-8f2b-8f7732180b14
* title: Ice Cream Sunday
* points: 1
* topics: python, lists

##### !question

Write a function `icecream_sundae` that takes two lists, one list of ice cream flavors and one list of toppings, and returns a new list that contains all of the possible ice cream sundae combinations that can be made by combining each flavor with each toppings.  If the flavors are "vanilla" and "chocolate" and the toppings are "chocolate sauce" and "berry sauce", the output list should contain "vanilla with chocolate sauce", "vanilla with berry sauce", "chocolate with chocolate sauce", "chocolate with berry sauce".  

Note the addition of the word "with" in the combined version.  You can assume that both of the input lists only contain strings.

Example inputs and outputs:
inputs: ```icecream_sunday(["vanilla", "chocolate", "strawberry"], ["whipped cream", "nuts", "a cherry"])```   
output: ```["vanilla with whipped cream", "vanilla with nuts", "vanilla with a cherry", "chocolate with whipped cream", "chocolate with nuts", "chocolate with a cherry", "strawberry with whipped cream", "strawberry with nuts", "strawberry with a cherry"]```

inputs: ```icecream_sunday(["a", "b"], ["c", "d", "e"])```  
outputs: ```["a with c", "a with d", "a with e", "b with c", "b with d", "b with e"]```

inputs: ```icecream_sunday(["vanilla", "strawberry"], [])```  
outputs: ```[]```

inputs: ```icecream_sunday([], ["chocolate sauce", "caramel sauce"])```  
outputs: ```[]```

##### !end-question

##### !placeholder

```python

def icecream_sunday(flavors, toppings):
    return None

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import *

class TestIcecreamSunday(unittest.TestCase):
    def test_with_content(self):
        self.assertEqual(icecream_sunday(["vanilla", "chocolate", "strawberry"], ["whipped cream", "nuts", "a cherry"]), ["vanilla with whipped cream", "vanilla with nuts", "vanilla with a cherry", "chocolate with whipped cream", "chocolate with nuts", "chocolate with a cherry", "strawberry with whipped cream", "strawberry with nuts", "strawberry with a cherry"])

    def test_with_letters(self):
        self.assertEqual(icecream_sunday(["a", "b"], ["c", "d", "e"]), ["a with c", "a with d", "a with e", "b with c", "b with d", "b with e"])

    def test_with_empty_toppings(self):
        self.assertEqual(icecream_sunday(["vanilla", "strawberry"], []), [])

    def test_with_empty_flavors(self):
        self.assertEqual(icecream_sunday([], ["chocolate sauce", "caramel sauce"]), [])

```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Loop over flavors
1. For each flavor, loop over toppings
1. Create a pairing between each flavor and each topping
1. Add each pairing to the result list
1. Return the result list

##### !end-hint

<!--optional-->
##### !explanation

Three examples of working implementations:

```python

def icecream_sunday(flavors, toppings):
    result = []
    for flavor in flavors:
        for topping in toppings:
            pair = flavor + " with " + topping
            result.append(pair)
    return result

def icecream_sunday(flavors, toppings):
    result = []
    for flavor_index in range(len(flavors)):
        for topping_index in range(len(toppings)):
            pair = flavors[flavor_index] + " with " + toppings[topping_index]
            result.append(pair)
    return result

def icecream_sunday(flavors, toppings):
    result = []
    flavor_index = 0
    topping_index = 0
    while flavor_index < len(flavors):
        topping_index = 0
        while topping_index < len(toppings):
            pair = flavors[flavor_index] + " with " + toppings[topping_index]
            result.append(pair)
            topping_index += 1
        flavor_index += 1
    return result

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman Project

It's time to jump back into our Snowman Project, open up your snowman.py and lets get started!

### Adding A Random Word

So far our Snowman game has used a constant as the secret word (`SNOWMAN_WORD = 'broccoli'`), but a game that always uses the same word is not a great game.  The code to generate a random English word is outside of the scope of these lessons, although it is an interesting problem and worth spending some time thinking about.  We are going to use a _package_ to come up with a random word.  We are going to use the _wonderwords_ package.  

1. Before we can use it in our code, we will need to install the package using the command line.  To install, copypasta this into your terminal:

    ```console
    $ pip3 install wonderwords
    ```
1. Once that's done, add the line `from wonderwords import RandomWord` to the top of our file.
    * This will import the class `RandomWord` for us to use in our code.
    ```python
    import random
    from wonderwords import RandomWord
    #https://pypi.org/project/wonderwords/

    # ... rest of file

    ```
1. Next, add the constants `SNOWMAN_MAX_WORD_LENGTH = 8` and `SNOWMAN_MIN_WORD_LENGTH = 5` with the other constants at the top of the file.    
1. Last, add the following lines of code to the top of the `snowman` function:
    ```python

        r = RandomWord()
        snowman_word = r.word(
          word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
          word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    ```
    <details>
    <summary>Curious about these lines of code?  Click here for more!</summary>
    The first line `r = RandomWord()` gives us a `RandomWord` object to work with.  We will not cover classes and objects in the pre-course material, but they will be a topic we will cover at Ada.  
    
    The next line, `snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)` will call the function `word` on the the RandomWord object `r` and give us a random word.  
    
 We are passing two arguments (word_min_length and word_max_length) using keyword arguments.  Again, we will not be covering these topics further in the pre-course, but they will come up later in the Ada curriculum.  The arguments that we are passing to the function `word` will instruct `word` to give us an English word where the length is between the SNOWMAN_MIN_WORD_LENGTH and SNOWMAN_MAX_WORD_LENGTH.  Feel free to experiment with setting different values for the constants.
    </details>

1. The last piece of adding our new random word is replacing the constant `SNOWMAN_WORD` in the conditional test inside of the `snowman` function with the new `snowman_word` variable.

    ```python

    def snowman():
        r = RandomWord()
        snowman_word = r.word(
          word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
          word_max_length=SNOWMAN_MAX_WORD_LENGTH)
        correct_guesses = 0
        wrong_guesses = 0
        while wrong_guesses < SNOWMAN_WRONG_GUESSES:
            user_input = get_letter_from_user()
            # Using the new variable instead of the constant SNOWMAN_WORD here:
            if user_input in snowman_word:
                print("You guessed a letter that's in the word!")
                correct_guesses += 1
            else:
                print(f"The letter {user_input} is not in the word")
                wrong_guesses += 1
            print_snowman(wrong_guesses)

    ```

### !callout-info

## Debugging

How do you know what your code is doing when it's generating a random word?  Use print() to print out the word during development.  Adding a print statement here will print the word to the terminal and make it easier to debug your code:
```python
snowman_word = r.word(
    word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
    word_max_length=SNOWMAN_MAX_WORD_LENGTH)
print(snowman_word)
```

Printing the value of variables in your code is an easy way to see what's going on inside your code.  Nobody writes perfect code!  There are always bugs, and learning how to debug is a core part of learning to be a programmer.  One strategy for debugging is to start by figuring out what your code is doing, and then work on making it do what you want.  Think of yourself as a detective, and instead of focusing on what you think your code should be doing, focus on figuring out exactly what it is doing.  Using all kinds of print statements is a simple way to start to look inside your code as it's running and see what's happening.

### !end-callout


### Tracking User Input

So far all we have done with our user input is check to see if it is in our word, but if we go back to the hypothetical game of snowman with a group, we would want to keep track of the letters that had been guessed.  We would also not accept guesses of the same letter that had been guessed before.  

Let's start with tracking incorrect guesses.  We know we are going to have a max of SNOWMAN_WRONG_GUESSES, so we could make that many variables and store our incorrect guesses in those variables.  This solution could be made to work, but every time we change the value of the constant we would have to rewrite our code.  Using a `list` gives us a way to store as many or as little wrong guesses as we want and will allow us to make the code flexible and easy to modify.

1. Start by addding an incorrect guesses list variable to the top of the `snowman` function:

    ```python

    def snowman():
        r = RandomWord()
        snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH,
                            word_max_length=SNOWMAN_MAX_WORD_LENGTH)
        wrong_guesses_list = []
        
        # ...

    ```

1. Next we need to add each incorrect guess to the list.  We are going to do this with the list function `append` which adds elements to the end of the list:

    ```python

        # ...
            if user_input in snowman_word:
                print("You guessed a letter that's in the word!")
            else:
                print(f"The letter {user_input} is not in the word")
                wrong_guesses_list.append(user_input)
        # ...

    ```

1. In the previous version, we were incrementing a variable `wrong_guesses` each time the user guessed a letter that was not in the word, and then using that variable in the test for our while loop.  We can continue to use this variable, but we can use our list instead and simplify our code.  The number of elements in `wrong_guesses_list` is the number of incorrect guesses, so we can use the length of the list instead of the counter variable.  We get the length of the list by using the len() function.  We can also use the length of the list when we call the print_snowman function.  Here's the updated version of the function:

    ```python

    def snowman():
        r = RandomWord()
        snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
                              word_max_length=SNOWMAN_MAX_WORD_LENGTH)
        wrong_guesses_list = []
        while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
            user_input = get_letter_from_user()
            if user_input in snowman_word:
                print("You guessed a letter that's in the word!")
            else:
                print(f"The letter {user_input} is not in the word")
                wrong_guesses_list.append(user_input)
            print_snowman(len(wrong_guesses_list))

    ```

###  Using `wrong_guesses_list` in `get_letter_from_user`

Now that we have a list incorrect guesses, we can use them in `get_letter_from_user` to prevent our user from inputting the same incorrect letter multiple times.  

1. The first step is to pass the variable `wrong_guesses_list` to `get_letter_from_user` as an argument.  
1. Next, We will need to update our function definition of `get_letter_from_user` with a new parameter.  
1. Last, we need to use the new information inside of `get_letter_from_user`.  
    * Python lists provide us with a handy `in` operator (syntax `item in list`) that returns `True` if the item is in the list and `False` if it is not.

    ```python

    # ...
    def snowman():
        # ...
        wrong_guesses_list = []
        while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
            user_input = get_letter_from_user(wrong_guesses_list)
        # ...

    def get_letter_from_user(wrong_list):
        valid_input = False
        user_input_string = None
        while not valid_input:
            user_input_string = input("Guess a letter: ")
            if not user_input_string.isalpha():
                print("You must input a letter!")
            elif len(user_input_string) > 1:
                print("You can only input one letter at a time!")
            # NEW SECTION
            elif user_input_string in wrong_list:
                print("You have already guessed that letter!")
            # END NEW SECTION
            else:
                valid_input = True

        return user_input_string

    ```

### Tracking Correct letters

At this point we are keeping track of the incorrect letters guessed and using those to provide feedback to our user when they guess a new letter.  Now it is time to do the same thing but with correct letters!

1. Add a `correct_guesses_list` to the `snowman` function
1. Add correct guesses to the list

<details>
<summary>When you are finished, compare your code with ours</summary>

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    print(f"debug info: {snowman_word}")
    correct_guesses_list = []
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

```

</details>

### Using `correct_guesses_list` in `get_letter_from_user`

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: ca1d65d6-960e-4f58-af35-8b8663f8bcf7
* title: get_letter_from_user detecting duplicate entries
* points: 1
* topics: python python-lists

##### !question

Update the function `get_letter_from_user` so that it takes an additional argument (correct_guesses) and uses that along with `wrong_guesses` to print the "You have already guessed that letter" as feedback to the user if the user has already guessed the letter.

##### !end-question

##### !placeholder

```py
def get_letter_from_user(wrong_list, correct_guesses):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # UPDATE THIS AREA
        elif user_input_string in wrong_list:
            print("You have already guessed that letter!")
        # END UPDATE AREA
        else:
            valid_input = True

    return user_input_string


```

##### !end-placeholder

##### !tests


```py
import sys
from unittest import mock
from unittest.mock import patch
import io
import unittest
import re

import main as p

class SimplisticTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_already_used_if_in_correct_guesses_list(self, mock_stdout):
        # Arrange
        input_letters = [
            'a',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(re.match('You have already guessed that letter', mock_stdout.getvalue(), flags=re.IGNORECASE), msg=f"Expected: {'You have already guessed that letter'} but recieved: {mock_stdout.getvalue()}")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_already_used_if_in_wrong_guesses_list(self, mock_stdout):
        # Arrange
        input_letters = [
            'e',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(re.match('You have already guessed that letter', mock_stdout.getvalue(), flags=re.IGNORECASE), msg=f"Expected {'You have already guessed that letter'} but recieved: {mock_stdout.getvalue()}")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_returns_valid_letter_after_invalid_guess(self, mock_stdout):
        # Arrange
        input_letters = [
            'e',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(answer == input_letters[-1], msg=f"Expected after guessing a previously guessed letter to reprompt the user and read in and return a valid letter.  Guessing {input_letters} with correct guesses list {correct_guesses_list} and incorrect guesses list {wrong_list}.  The function returned {answer}")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_only_one_letter_at_a_time_for_input_with_multiple_characters(self, mock_stdout):
        # Arrange
        input_letters = [
            'zzzzz',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(re.match('You can only input one letter at a time!', mock_stdout.getvalue(), flags=re.IGNORECASE), msg=f"Expected to print {'You can only input one letter at a time!'} when 'zzzzz' is entered.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_you_must_input_a_letter_for_non_alpha_input(self, mock_stdout):
        # Arrange
        input_letters = [
            '3',
            'z'
        ]
        correct_guesses_list = ['a', 'b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(re.match('You must input a letter!', mock_stdout.getvalue(), flags=re.IGNORECASE), msg=f"Expected to print {'You must input a letter!'} when a number is input.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_valid_input_the_1st_time_it_just_returns_the_input(self, mock_stdout):
        # Arrange
        input_letters = ['a']
        correct_guesses_list = ['b', 'c']
        wrong_list = ['d', 'e', 'f']
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(answer == input_letters[0], msg=f"When the user guesses a letter that has not been previously guessed, that letter should be returned.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_works_with_empty_lists(self, mock_stdout):
        # Arrange
        input_letters = ['a']
        correct_guesses_list = []
        wrong_list = []
        with unittest.mock.patch('builtins.input', side_effect=input_letters):

            # Act
            answer = p.get_letter_from_user(wrong_list, correct_guesses_list)
        # Assert
        self.assertTrue(answer == input_letters[0], msg="When the no letter has been guessed any valid letter is accepted and returned.")

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
##### !explanation


A sample solution could be:

```python
def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string
```

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

## Using Lists to Improve Readability and Simplify Code

In the last lesson we wrote the function `print_snowman` that drew our snowman up to the height that corresponded to the number of incorrect guesses.  The code for that function was fairly long because our graphic was broken up into seven constants.  We will use a list to simplify and streamline this code.

1. The first step is to store all of the drawing constants in a list:

    ```python

    SNOWMAN_GRAPHIC = [
        '*   *   *  ',
        ' *   _ *   ',
        '   _[_]_ * ',
        '  * (")    ',
        '  \( : )/ *',
        '* (_ : _)  ',
        '-----------'
    ]

    ```

1. The next step is to update our drawing function to use the list.  Here's the previous version:

    ```python

    def print_snowman(wrong_guesses_count):
        for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count,
                    SNOWMAN_WRONG_GUESSES + 1)
            if i == 1:
                print(SNOWMAN_1)
            if(i == 2):
                print(SNOWMAN_2)
            if(i == 3):
                print(SNOWMAN_3)
            if(i == 4):
                print(SNOWMAN_4)
            if(i == 5):
                print(SNOWMAN_5)
            if(i == 6):
                print(SNOWMAN_6)
            if(i == 7):
                print(SNOWMAN_7)

    ```

1. Now, instead of using SNOWMAN_1, we can use SNOWMAN_GRAPHIC[0], for SNOWMAN_2 we use SNOWMAN_GRAPHIC[1], and so on.  Reminder - the first index of a list is 0, not 1.  That means that for element number `x` in the list, the index will be `x - 1`.  Let's update our code to use this new way of accessing each element of the graphic:

    ```python

    def print_snowman(wrong_guesses_count):
        for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count,
                    SNOWMAN_WRONG_GUESSES + 1)
            print(SNOWMAN_GRAPHIC[i - 1])

    ```

    Notice in the above code that we have `+ 1` and `- 1`.  This is because in the first version if we wanted to draw the whole snowman we needed the math to produce the sequence 1 to 7 because we were using the numbers 1-7 in our constants and this made the code easier to read.  Now, we're using a list, so to draw the whole snowman we need the sequence to be 0 to 6.  We can now simplify some of our math with that in mind.

    ```python

    def print_snowman(wrong_guesses_count):
        for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count,
                    SNOWMAN_WRONG_GUESSES)
            print(SNOWMAN_GRAPHIC[i])

    ```

## Summary

Lists are powerful tools!  Being able to add data to a list and access all of the elements of the list means that one variable can do the work of many variables.  Pairing lists with tools like loops allows us to do complex operations with just a few concise lines of code.  
