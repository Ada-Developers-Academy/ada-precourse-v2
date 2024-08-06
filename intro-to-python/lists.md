# Lists

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=c65a7cda-04ef-4f27-acd7-aede010488c7&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

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

In this section we will be building on the code you wrote in the [Loops](loops.md) lesson.  If you would like to look at our example code for that lesson, you can find it [here](resources/src/loops/game-loop.md).

### Introducing Lists, Our First Data Structure!

Variables are awesome!  We can store data, retrieve it, update it and use it in any way we like.  So far, though, variables have been limited because they have only been able to hold one piece of data.  Imagine we want to write a program to ask for and then display the user's top five favorite flavors of ice cream.  We can store each flavor in it's own variable and then use those variables in our display.  

What happens when we want to modify our program to store our user's top 10 favorite flavors?  We would have to add more variables and update the program to use those new variables.  _Lists_ change all of this!  Lists are a _data structure_ that can hold multiple pieces of data and we can access the data numerically starting with 0.  Lets go back to our ice cream example.  If we use a list to store our ice cream flavors, we can use one variable and then as our user inputs their favorite flavors, we can add the new flavor to the list!  

By using a list, we can store as many ice cream flavors as we want. Also, Python provides us with ways to easily loop through all of the elements in a list so we can use a loop to display all of the flavors, which will simplify our code even further! Take a look at the following block of code. It repeatedly asks a user to input a flavor of ice cream they like and adds that flavor to a list of ice cream flavors. The code will stop asking a user to input an ice cream flavor when a user inputs the string "done" and then the code loops over the ice cream flavors one at a time and prints them out. 

```python

def favorite_flavors():
    ice_cream_flavors = []
    flavor = ""

    # this loop will run until the user types in the word "done"
    while not flavor == "done":  
        flavor = input("What is an ice cream flavor that you like? ") 
        # add all flavors except for done
        if not flavor == "done":
            # add the user's flavor to the end of the list
            ice_cream_flavors.append(flavor)

    # this loop will iterate over each element in the list
    for flavor in ice_cream_flavors:
        # the looping variable called flavor references each flavor in the list one at a time 
        print(f"{flavor} is a great ice cream flavor!")

    return ice_cream_flavors

favorite_flavors()
```

## Vocabulary and Syntax

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| data structure| A collection of data that follows a set of rules for modifying and accessing the data.  Python provides four built in data structures, _lists_, _dictionaries_, _tuples_ and _sets_.  This curriculum will cover lists and dictionaries.     | Collection      | "We organize our collection of students into a list data structure" |
| list      | A data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key | Array | "We loop through the list and print out each value"    |
| index      |The position of an element in a _sequence type_, that is, a type that stores data in order.  In Python, strings and lists are examples of sequence types.  In Python indices start at 0. | Key | "We get the 1st element at index 0."    |
| module      | A file containing Python code.  | Library | "This module has functions for calculating taxes."    |
| package      | A collection of modules distributed together  | N/A | "We can add the wonderwords package to our project and use it to get random words."    |

Before we get into some practice problems, let's look at some Python syntax related to lists. The snippet below shows how we can create an empty list, create a list with values in it, add a value to a list with the `append` method, access elements by their indices using square brackets, and loop through the elements. 

```python
# creating a new empty list:
new_empty_list = []

# creating a new list with values in it
flavors = ["lemon", "vanilla", "chocolate"]

# adding an element to a list:
flavors.append("caramel")
# new_list_populated_with_strings = ["lemon", "vanilla", "chocolate", "caramel"]

# accessing an element of a list
flavors[0]
# "lemon"

flavors[3]
# "caramel"

# looping through a list
for flavor in flavors:
    print(flavor)

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

Write a function `find_index_of_item` that takes two arguments, an item and a list called list_of_items.  The function has the following behavior:
* If the list contains the item, the function returns the index of the item in the list.  
* If the list contains the item multiple times, the function returns the index of the first time the item appears in the list.  
* If the list does not contain the item, the function returns -1.

Example inputs and outputs:

|input|output|
|--|--|
| `item = 3`<br/> `list_of_items = [1, 4, 5, 6, 2, 3, 9]`|`5`|
| `item = "cow"`<br/> `list_of_items = ["dog", "cow", "goat", "pig"]`|`1`|
| `item = "chocolate"`<br/> `list_of_items = []`|`-1`|
| `item = -93`<br/> `list_of_items = [1, 30, -93, 99, -3, -93, 25, 16]`|`2`|

##### !end-question

##### !placeholder

```python

def find_index_of_item(item, list_of_items):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import find_index_of_item

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
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            return i
    return default

def find_index_of_item(item, list_of_items):
    default = -1
    item_index = 0
    for current_item in list_of_items:
        if current_item == item:
            return item_index
        item_index += 1
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


Write a function `count_item_in_list` that takes two arguments, an item and a list called list_of_items.  The function has the following behavior:
* The function returns the number of times the item appears in the list 
* If the list does not contain the item, the function returns 0 .

Example inputs and outputs:

|input|output|
|--|--|
| `item = 3`<br/> `list_of_items = [1, 3, 3, 6, 2, 3, 9]`|`3`|
| `item = "cat"`<br/> `list_of_items = ["dog", "cow", "goat", "pig"]`|`0`|
| `item = 38`<br/> `list_of_items = []`|`0`|
| `item = "dog"`<br/> `list_of_items = ["dog", "cat", "cow", "goat", "pig"]`|`1`|
<!--This can be regular **Markdown**-->

##### !end-question

##### !placeholder


```python

def count_item_in_list(item, list_of_items):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import count_item_in_list

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

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

### Nested Loops

We can also nest loops so that we can iterate over two lists at the same time. Nested loops means a loop is inside of another loop. For example, we could have a while loop inside a for loop or a for loop inside of a for loop. That means while we are iterating over an element in a list, we can also be iterating over another list too which will give us access to two elements at the same time. 

The syntax for nesting loops looks like this:
```python
# outer_loop Expression:
    # inner_loop Expression:
        # statement inside inner_loop

list_of_letters = ["a", "b", "c"]
list_of_nums = [1, 2, 3]

for letter in list_of_letters:
    for num in list_of_nums:
        print(f"{letter} and {num}")

# a and 1
# b and 2
# c and 3
```

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 555531b1-7ebc-4129-8f2b-8f7732180b14
* title: Ice Cream Sundae
* points: 1
* topics: python, lists

##### !question

Write a function `icecream_sundae` that takes two arguments, one list of ice cream flavors and one list of toppings, and returns a new list that contains all of the possible ice cream sundae combinations that can be made by combining each flavor with each toppings.  If the flavors are "vanilla" and "chocolate" and the toppings are "chocolate sauce" and "berry sauce", the output list should contain "vanilla with chocolate sauce", "vanilla with berry sauce", "chocolate with chocolate sauce", "chocolate with berry sauce".  

Note the addition of the word "with" in the combined version.  You can assume that both of the input lists only contain strings.

Example inputs and outputs:

|<div style="width:250px;">input<div>|output|
|--|--|
| `flavors = ["vanilla", "chocolate", "strawberry"]`<br /> <br />`toppings = ["whipped cream", "nuts", "a cherry"]`|`["vanilla with whipped cream", "vanilla with nuts", "vanilla with a cherry", "chocolate with whipped cream", "chocolate with nuts", "chocolate with a cherry", "strawberry with whipped cream", "strawberry with nuts", "strawberry with a cherry"]`|
| `flavors = ["a", "b"]`<br /> <br />`toppings = ["c", "d", "e"]`|`["a with c", "a with d", "a with e", "b with c", "b with d", "b with e"]`|
| `flavors = ["vanilla", "strawberry"]`<br /> <br />`toppings = []`|`[]`|
| `flavors = []`<br /> <br />`toppings = ["chocolate sauce", "caramel sauce"]`|`[]`|

##### !end-question

##### !placeholder

```python

def icecream_sundae(flavors, toppings):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import icecream_sundae

class TestIcecreamSundae(unittest.TestCase):
    def test_with_content(self):
        self.assertEqual(icecream_sundae(["vanilla", "chocolate", "strawberry"], ["whipped cream", "nuts", "a cherry"]), ["vanilla with whipped cream", "vanilla with nuts", "vanilla with a cherry", "chocolate with whipped cream", "chocolate with nuts", "chocolate with a cherry", "strawberry with whipped cream", "strawberry with nuts", "strawberry with a cherry"])

    def test_with_letters(self):
        self.assertEqual(icecream_sundae(["a", "b"], ["c", "d", "e"]), ["a with c", "a with d", "a with e", "b with c", "b with d", "b with e"])

    def test_with_empty_toppings(self):
        self.assertEqual(icecream_sundae(["vanilla", "strawberry"], []), [])

    def test_with_empty_flavors(self):
        self.assertEqual(icecream_sundae([], ["chocolate sauce", "caramel sauce"]), [])

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

def icecream_sundae(flavors, toppings):
    result = []
    for flavor in flavors:
        for topping in toppings:
            pair = flavor + " with " + topping
            result.append(pair)
    return result

def icecream_sundae(flavors, toppings):
    result = []
    for flavor_index in range(len(flavors)):
        for topping_index in range(len(toppings)):
            pair = flavors[flavor_index] + " with " + toppings[topping_index]
            result.append(pair)
    return result

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman Project

It's time to jump back into our Snowman Project. Open up your `snowman.py` and let's get started!

### Adding A Random Word

So far our Snowman game has used a constant as the secret word (`SNOWMAN_WORD = 'broccoli'`), but a game that always uses the same word is not a great game.  The code to generate a random English word is outside of the scope of these lessons, although it is an interesting problem and worth spending some time thinking about.  We are going to use a _package_ to come up with a random word.  We are going to use the _wonderwords_ package.  

1. Before we can use it in our code, we will need to install the package using the command line. We will need to navigate to the `snowman_project` directory if we're not already there. We can run `pwd` to check where we are and we should see something like `/ada/precourse/snowman_project`. Once we're in the correct directory, run the following commands one by one:

    ```console
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

<!-- prettier-ignore-start -->
| Terminal Command | Notes |
| ------------- | ----- |
| `python3 -m venv venv` | Creates a virtual environment named `venv` for this project |
| `source venv/bin/activate` | Activates this virtual environment |
<!-- prettier-ignore-end -->

After running `source venv/bin/activate` to activate our virtual environment, we should now see that each line of our terminal now begins with `(venv)`. This tells us that our virtual environment named `venv` has been activated. Our terminal should now look something like this:

```console

(venv) snowman_project 

```

At a high level, a virtual environment is an isolated space where you can work on your Python projects. We will create and use virtual environments for almost all Python projects we work on. Feel free to do your own research about virtual environments. For now, we'll focus on the implementation of our Snowman game and delve more into virtual environments later on. 

2. After creating and activating our virtual environment, we can install the `wonderwords` package. Since our project requires the `wonderwords` package in order to work, we will add this project requirement to the `requirements.txt` file. We will also learn more about this file and project requirements later on. 

    Run the following commands in your terminal, one at a time. Note that `(venv)` is **not** part of the commands we need to run. It is displayed in the command line to indicate to us that our virtual environment is currently activated.

    ```console
    $ (venv) pip install wonderwords
    $ (venv) pip freeze > requirements.txt
    ```

<!-- prettier-ignore-start -->
| Terminal Command | Notes |
| ------------- | ----- |
| `pip install wonderwords` | Install the `wonderwords` package to our virtual environment |
| `pip freeze > requirements.txt` | Add any installed packages to requirements.txt |
<!-- prettier-ignore-end -->

3. Once that's done, add the line `from wonderwords import RandomWord` to the top of `snowman.py`.
    * This will import the class `RandomWord` for us to use in our code.
  
    ```python
    import random
    from wonderwords import RandomWord
    # https://pypi.org/project/wonderwords/

    # ... rest of file

    ```
4. Next, add the constants `SNOWMAN_MAX_WORD_LENGTH = 8` and `SNOWMAN_MIN_WORD_LENGTH = 5` with the other constants at the top of the file.  
 
5. Then, add the following lines of code inside the top of the `snowman` function:
    ```python

        r = RandomWord()
        snowman_word = r.word(
          word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
          word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    ```

    <br>

    <details>
    <summary>Curious about these lines of code?  Click here for more!</summary>

    Invoking the `RandomWord()` returns a `RandomWord` object that we save to the variable we call `r`.  We'll learn more about classes and objects soon in Unit 1.  
    
    The `RandomWord` object referenced by our variable `r` has a method called `word` and we invoke that method to get a random word.  
    
    We are passing two arguments (`word_min_length` and `word_max_length`) using keyword arguments.  Again, we will not be covering these topics further in the Precourse, but they will come up later in the Ada curriculum.  The arguments that we are passing to the method `word` from `RandomWord` will instruct `word` to give us an English word where the length is between the `SNOWMAN_MIN_WORD_LENGTH` and `SNOWMAN_MAX_WORD_LENGTH`.  Feel free to experiment with setting different values for the constants.
    </details>

6. We no longer need a hardcoded constant variable since we have a way to get random words. Replace the constant variable `SNOWMAN_WORD` in the conditional test inside of the `snowman` function with the new `snowman_word` variable. 
7. 
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
            # Use the new variable snowman_word instead of the constant variable SNOWMAN_WORD here:
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

How do you know what your code is doing when it's generating a random word?  Use `print()` to print out the word during development.  Adding a print statement here will print the word to the terminal and make it easier to debug your code:

```python

snowman_word = r.word(
    word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
    word_max_length=SNOWMAN_MAX_WORD_LENGTH)
print(snowman_word)

```

Printing the value of variables in your code is an easy way to see what's going on inside your code.  Nobody writes perfect code!  There are always bugs, and learning and practicing how to debug is a core part of learning to be a programmer.  One strategy for debugging is to start by figuring out what your code is doing, and then work on making it do what you want.  Think of yourself as a detective, and instead of focusing on what you think your code _should be_ doing, focus on figuring out exactly what it _is_ doing.  Using all kinds of print statements is a simple way to start looking inside your code as it's running and see what's happening.

### !end-callout


### Tracking User Input

So far, all we have done with our user input is check to see if it is in our word. But if we go back to the hypothetical game of snowman with a group of children, we would want to keep track of the letters that have been guessed.  We would also not accept guesses of the same letter that have already been guessed.  

Let's start with tracking incorrect guesses.  We know we are going to have a max of SNOWMAN_WRONG_GUESSES, so we could make that many variables and store our incorrect guesses in those variables.  This solution could be made to work, but every time we change the value of the constant we would have to rewrite our code.  Using a `list` gives us a way to store as many or as little wrong guesses as we want and will allow us to make the code flexible and easy to modify.

1. Start by adding an incorrect guesses list variable to the `snowman` function:

    ```python

    def snowman():

        r = RandomWord()
        snowman_word = r.word(
          word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
          word_max_length=SNOWMAN_MAX_WORD_LENGTH)

        wrong_guesses_list = []
        
        # ...

    ```

2. Next we need to add each incorrect guess to the list.  We are going to do this with the list function `append` which adds elements to the end of the list:

    ```python

        # ...
            if user_input in snowman_word:
                print("You guessed a letter that's in the word!")
            else:
                print(f"The letter {user_input} is not in the word")
                wrong_guesses_list.append(user_input)
        # ...

    ```

3. In the previous version, we were incrementing a variable `wrong_guesses` each time the user guessed a letter that was not in the word, and then using that variable in the test for our while loop.  We can continue to use this variable, but we can use our list instead and simplify our code.  The number of elements in `wrong_guesses_list` is the number of incorrect guesses, so we can use the length of the list instead of the counter variable.  We get the length of the list by using the `len()` function.  We can also use the length of the list when we call the print_snowman function. Additionally, we can print the incorrect guesses to remind the user of what they have already guessed. Here's the updated version of the function:

    ```python

    def snowman():
        r = RandomWord()
        snowman_word = r.word(
          word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
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
            print(f"Wrong guesses: {wrong_guesses_list}")

    ```

###  Using `wrong_guesses_list` in `get_letter_from_user`

Now that we have a list incorrect guesses, we can use them in the helper function `get_letter_from_user` to prevent our user from inputting the same incorrect letter multiple times.  

1. The first step is to pass the variable `wrong_guesses_list` to `get_letter_from_user` as an argument.  
2. Next, we will need to update our function definition of `get_letter_from_user` with a new parameter.  
3. Last, we need to use the new information inside of `get_letter_from_user`.  
    * Python lists provide us with a handy `in` operator (syntax `item in list`) that returns `True` if the item is in the list and `False` if it is not.

    ```python

    # ...
    def snowman():
        # ...
        wrong_guesses_list = []
        while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
            # First we pass `wrong_guesses_list` when we call `get_letter_from_user()`
            user_input = get_letter_from_user(wrong_guesses_list)
        # ...

    # We refactor `get_letter_from_user` to include a parameter `wrong_guesses_list`
    def get_letter_from_user(wrong_guesses_list):
        valid_input = False
        user_input_string = None

        while not valid_input:
            user_input_string = input("Guess a letter: ")
            if not user_input_string.isalpha():
                print("You must input a letter!")
            elif len(user_input_string) > 1:
                print("You can only input one letter at a time!")
            # NEW SECTION: check to see if the user's current guess has already been guessed.
            elif user_input_string in wrong_guesses_list:
                print("You have already guessed that letter!")
            # END NEW SECTION
            else:
                valid_input = True

        return user_input_string

    ```

### Tracking Correct letters

At this point we are keeping track of the incorrectly guessed letters and using those to provide feedback to our user when they guess a new letter.  Now it is time to do the same thing but with correct letters!

1. Add a `correct_guesses_list` to the `snowman` function
2. Add correct guesses to the list

<br>

<details>
<summary>When you are finished, compare your code with ours</summary>

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(
      word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
      word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    print(f"debug info: {snowman_word}")
    
    # Add a new list to track correctly guessed letters
    correct_guesses_list = []
    wrong_guesses_list = []

    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            # Add a correctly guessed letter to `correct_guesses_list`
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)

        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

# Call the function run the code and test out the new changes
snowman()

```

</details>

We've made a lot of changes to our code, execute `snowman.py` as we're coding to test out our new changes. If the code is not behaving as expected, add some debugging print statements to see what is happening. From there, try identifying which lines of code need to be updated to fix it. It's ok if you're code isn't working as described in the lesson. Reach out to Slack with your questions and to get help!

### Using `correct_guesses_list` in `get_letter_from_user`

Update the helper function `get_letter_from_user` so that it takes an additional argument `correct_guesses_list`. Use this new argument along with `wrong_guesses_list` to print "You have already guessed that letter" as feedback if the user has already guessed a letter in `correct_guesses_list`.

Here's what `get_letter_from_user` looks like so far:

```py
def get_letter_from_user(wrong_guesses_list, correct_guesses_list):
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # UPDATE THIS AREA
        elif user_input_string in wrong_guesses_list:
            print("You have already guessed that letter!")
        # END UPDATE AREA
        else:
            valid_input = True

    return user_input_string

```

<br>

<details>
<summary>When you are finished, compare your code with ours</summary>

```python
def get_letter_from_user(wrong_guesses_list, correct_guesses_list):
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_guesses_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string
```
</details>



## Using Lists to Improve Readability and Simplify Code

In the Loops lesson we wrote the helper function `print_snowman` that drew our snowman up to the height that corresponded to the number of incorrect guesses.  The code for that function was fairly long because our graphic was broken up into seven constants.  We will use a list to simplify and streamline this code.

1. The first step is to store all of the drawing constants in a list referenced by the constant variable `SNOWMAN_GRAPHIC`:

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
        snowman_image_start = SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count
        snowman_image_end = SNOWMAN_WRONG_GUESSES + 1

        for i in range(snowman_image_start, snowman_image_end)
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

2. Now, instead of using individual variables, we can use the indices of a list to access different parts of the snowman graphic. SNOWMAN_1 is now SNOWMAN_GRAPHIC[0], SNOWMAN_2 we use SNOWMAN_GRAPHIC[1], and so on.  Reminder - the first index of a list is 0, not 1.  That means that for element number `x` in the list, the index will be `x - 1`.  Let's update our code to use this new way of accessing each element of the graphic:

    ```python

    def print_snowman(wrong_guesses_count):
        snowman_image_start = SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses_count
        snowman_image_end = SNOWMAN_WRONG_GUESSES + 1

        for i in range(snowman_image_start, snowman_image_end)
            print(SNOWMAN_GRAPHIC[i - 1])

    ```

    Notice in the above code that we have `+ 1` and `- 1`.  This is because in the first version if we wanted to draw the whole snowman we needed the math to produce the sequence 1 to 7 because we were using the numbers 1-7 in our constants and this made the code easier to read.  Now, we're using a list, so to draw the whole snowman we need the sequence to be 0 to 6.  We can now simplify some of our math with that in mind.

    ```python

    def print_snowman(wrong_guesses_count):
        # + 1 and - 1 can be removed from our starting and ending points
        snowman_image_start = SNOWMAN_WRONG_GUESSES - wrong_guesses_count
        snowman_image_end = SNOWMAN_WRONG_GUESSES 

        for i in range(snowman_image_start, snowman_image_end)
            # We no longer need to offset the index by 1
            print(SNOWMAN_GRAPHIC[i])

    ```

    Execute the code in `snowman.py` to try the game out!
  
### Deactivating the Virtual Environment

When we're done working on the Snowman game for the time being, we should deactivate our virtual environment. We can do so by running `deactivate` in the terminal. We should no longer see `(venv)` at the start of each line in our terminal. 

```console
(venv) snowman_project 
(venv) snowman_project deactivate
snowman_project
```

The first line of the terminal output above shows the terminal command line when the virtual environment is activated. The second line shows the `deactivate` command being run. The final line shows the what the terminal command line looks like when the virtual environment is deactivated.

When we start working on `snowman.py` again, we will need to reactivate the virtual environment before we can execute our code. 

## Summary

Lists are powerful tools!  Being able to add data to a list and access all of the elements of the list means that one variable can do the work of many variables.  Pairing lists with tools like loops allows us to do complex operations with just a few concise lines of code.  
