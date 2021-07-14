# Helper Functions

## Learning Goals

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=a39ba8bc-1711-4c3a-a804-ad65007c2576&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

At the end of this lesson we will be able to:

- Identify places where helper functions would be useful
- Create helper functions
- Refactor larger functions into smaller pieces


## Introduction

A helper function is a function that does part of the work for another function. They make our code easier to read by breaking up long expressions or functions into smaller pieces. We recommend giving helper functions descriptive names, to help with readability.

### !callout-info

## Functions Best Practice

Ideally, every function should be designed to handle *one* task in accordance to the [single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle).  

### !end-callout

## Breaking Up Long Functions

Imagine we are building an ecommerce webapp that will display an order summary. In order to create this summary, two calculations must be performed: subtotal of all items purchased and sales tax. It would be reasonable to place these calculations into two separate helper functions: `calculate_subtotal` and `calculate_sales_tax`. 

```Python
def calculate_subtotal(item_prices):
    total = 0
    for price in item_prices:
        total += price
    return float(total)

def calculate_sales_tax(total):
    sales_tax_rate = .08
    sales_tax_total = total * sales_tax_rate
    return float(sales_tax_total)
```

Then, we could create another function `display_order_summary` that takes in a list of item prices and calls `calculate_subtotal` and `calculate_sales_tax`. 

```Python
def display_order_summary(item_prices):
    sub_total = calculate_subtotal(item_prices)
    sales_tax_total = calculate_sales_tax(sub_total) 
    grand_total = sub_total + sales_tax_total

    sub_total = "$ {:.2f}".format(sub_total)
    grand_total = "$ {:.2f}".format(grand_total)
    sales_tax_total = "$  {:.2f}".format(sales_tax_total)

    return (f"""
        **** Order Summary ****\n  
        Item(s) Subtotal:  {sub_total}
        Sales Tax:         {sales_tax_total}
        --------------
        Grand Total:       {grand_total}""") 
```

### !callout-info

## Assigning Variables to Function Calls

Let's recall our learnings from the `Return keyword` section of the previous Functions. If a function has a return value, we can assign a variable to its function call and expect a value. Let's breakdown the `sub_total` variable assignment in `display_order_summary`:

    - `sub_total` is assigned to the function call, `calculate_subtotal`.
    - `calculate_subtotal` runs and returns a value of 40 when finished.
    -  40 is now assigned to `subtotal`. 

    ```Python
    # before executing
    sub_total = calculate_subtotal(item_prices)
    # after executing 
    sub_total = 40 
    ```
### !end-callout


## Breaking Up Long Expressions 

Sometimes code will have long expressions that are not easy to read. Imagine we are writing a function to mimic the order of operations rule, [PEMDAS](https://en.wikipedia.org/wiki/Order_of_operations#Mnemonics). We could write the function as a long expression like so:

```Python
def pemdas(n1,n2,n3,n4,n5,n6):
    result = ((((n1**n2)*n3)/n4)+n5)-n6
    return result
```
What happens if the exponent or the division is inaccurate within this expression? It would be much harder to test each calculation within this expression. To improve overall readability, what helper functions should we add? (Note: exclude detecting parenthesis)

<br/>

<details>
    
<summary>Click here to see the helper functions code </summary>
    
```python
def multiply(n1, n2):
    return n1*n2

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1 / n2

def exponent(n1, n2):
    return n1**n2 

def pemdas(n1,n2,n3,n4,n5,n6):
    result = 0 
    result += exponent(n1, n2)
    result = multiply(result, n3)
    result = divide(result, n4)
    result = add(result, n5)
    result = subtract(result, n6)

    return result 
```
</details>


## Guess The Number Project

Open up your `game.py` in VSCode and let's see how we can apply helper functions to our project!

### Exercise:  Breaking Up `guess_the_number`

The function `guess_the_number` can be broken up into two conceptual pieces, getting user input, and then processing the user input.  

```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)

def guess_the_number():

    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number!  Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")

# Run the guess_the_number function to test it
guess_the_number()
```

1.  Start by writing a function called `get_number_from_user`
    * Then pull all of the pieces of code in `guess_the_number` that have to do with getting user input into `get_number_from_user`.  
    * Include any conditional statement that validate user input as a number.  
    * This function should ask the user for a number and then give an error message if the user inputs anything other than a number.  
    * Last, it should return the valid user input, or None if there was no valid input.  
    * In `guess_the_number`, call this function and store the result in user_input.
1.  Then the `guess_the_number` function can use the previous `if...else` statements to tell the user if their guess was too high or too low.
 
<details>
<summary> Our version at this point </summary>

```python

import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)

def guess_the_number():

    user_input = get_number_from_user()

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number!  Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")


def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input

# Run the guess_the_number function to test it
guess_the_number()
```
</details>

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-secondary

## Each Function Does **One** Thing!

Notice in our code that now each function is doing exactly **one** thing.  `get_number_from_user` does just that, it reads in a number from the user.  Similarly `guess_the_number` now just processes the user's guess.  This makes each step *much* easier to read and test.

### !end-callout

### !callout-info

## None and potential Errors

Notice that in our version, if the user does not give a valid input, the return value will be `None`.  This will cause an error in the conditionals in `guess_the_number`, because `None` can not be compared to a number.  That's ok, we're building to a full solution.  Many times when writing code, it is useful to write and test a small portion, and then when we're confident that it works, moving on to build the next portion.

### !end-callout

## Summary

Now that we have broken the various sections into functions, we can easily swap the order of the games, play a game multiple times, or add new games in new functions and insert them in any order we want.  

Functions add flexibility and structure to our code, and make code easier to maintain and read.  In the next lesson we will work on adding more functionality to our functions with loops. 

## Practice Problems 

### !challenge

* type: code-snippet
* language: python3.6
* id: a4494575-f4bd-4e33-8e5a-feae8510a30f
* title: Helper Functions
* points: 1
* topics: python, functions

##### !question

Best Burger needs help creating `order_summary` for their drive-thru display. Best Burger menu include: $5.25 burger, $2.50 fries, and a $4.25 milkshake. Create the helper function `calculate_total` that takes in a list of items and calculates the total to be used in `order_summary`.

|example input `items`| example output (return value) |
|--|--|
|`['fries', 'fries', 'burger']`| `10.25`|
|`['fries', 'milkshake', 'burger']`| `12`|

##### !end-question

##### !placeholder

```py

def calculate_total(order_items):
    pass 

def order_summary(order_items):
    total = calculate_total(order_items)
    
    print("*** Welcome to Best Burger ***")
    print("Order Items: ")
    for item in order_items:
        print(item)
    print(f"Total: {total}")
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import calculate_total

class TestPython1(unittest.TestCase):
    def test_total_of_different_items(self):
        # Arrange
        order = ["burger", "fries", "milkshake"]

        # Act/Assert
        self.assertEqual(calculate_total(order), 12)

    def test_order_of_same_item(self):
        # Arrange
        order = ["fries", "fries", "fries"]
        
        # Act/Arrange
        self.assertEqual(calculate_total(order), 7.5)

    def test_no_items(self):
        # Arrange
        order = []

        # Act/Arrange
        self.assertEqual(calculate_total(order), 0)
```

##### !end-tests
### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 366207b9-4c9e-4843-9a83-60f02b121867
* title: Net Income 
* points: 1
* topics: python, functions

##### !question

FastBooks needs help developing an income statement generator. Given a list of expense costs, create the function `calculate_expenses`. This function will be used in `calculate_net_income`.  

|example input `expense costs`| example output (return value) |
|--|--|
|`[10, 20, 30]`| `60`|


##### !end-question

##### !placeholder

```py

def calculate_expenses(expense_costs):
    pass 

def calculate_net_income(revenue, expense_costs):
    expenses = calculate_expenses(expense_costs)
    net_income = revenue - expenses
    return net_income

```

##### !end-placeholder

##### !tests

```py
import unittest
from main import calculate_expenses

class TestPython1(unittest.TestCase):
    def test_total_of_different_costs(self):
        # Arrange
        expenses = [100, 2000, 200]

        # Act/Assert
        self.assertEqual(calculate_expenses(expenses), 2300)

    def test_no_expenses(self):
        # Arrange
        expenses = []

        # Act/Arrange
        self.assertEqual(calculate_expenses(expenses), 0)
```

##### !end-tests
### !end-challenge



