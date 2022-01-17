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

## Capturing the Return Value of Function Calls in Variables

Let's recall our learnings from the `Return keyword` section of the previous Functions reading.

<br>

If a function has a return value, we often want to capture that value, and use it in our code later. To do this, we set up a variable assignment to receive the result of the function call.

<br>

The syntax for this is `variable_name = function_call()`.

<br>

We set a variable, which we want to receive the return value of the function, equal to the result of calling the function. When this code is executed, Python sees that we are trying to assign a value, so it evaluates everything on the right-hand side of the assignment (in this case, running our function call), and then stores the result in the variable.

<br>

<details>

<summary>Expand for a breakdown of the <code>sub_total</code> variable assignment in <code>display_order_summary</code>.</summary>


  1. `sub_total` is set up to receive a variable assignment, so Python looks at the code to the right of the assignment, where it sees `calculate_subtotal(item_prices)`.
  1. `calculate_subtotal` runs and returns a value of 40 when finished.
  1. The expression result, 40, is assigned to `subtotal`. 

```python
# before right-hand side evaluation
sub_total = calculate_subtotal(item_prices)

# after right-hand side evaluation
sub_total = 40 
```

</details>

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

Ada Bubble Tea needs help creating `drink_summary` for their online order display. Each drink has three options: tea flavor, milk, and boba.  The tea flavor options are oolong ($4.50), jasmine ($4.50) and silver needle ($5.00).  The milk options are none ($0.00), dairy ($0.50), oat ($0.75) and soy ($0.50).  The boba options are yes ($0.50) and no ($0.00). Create the helper function `calculate_total` that takes in a data structure that represents the order and calculates the total to be used in `drink_summary`.

|example input `flavor`, `milk`, `boba`| example output (return value) |
|--|--|
|`'oolong', 'none', 'yes'`| `5.00`|
|`'silver needle', 'oat', 'yes'}`| `6.25`|

##### !end-question

##### !placeholder

```py

def calculate_total(flavor, milk, boba):
    pass 

def drink_summary(flavor, milk, boba):
    total = calculate_total(flavor, milk, boba)

    print('*** Drink Summary ***')
    drink_display = flavor.capitalize()
    if milk != 'none' or boba != 'no':
        drink_display = drink_display + ' with '
    if milk != 'none':
        drink_display = drink_display + milk + ' milk'
    if milk != 'none' and boba != 'no':
        drink_display = drink_display + ' and '
    if boba != 'no':
        drink_display = drink_display + 'boba'
    
    print(drink_display)
    print(f'Drink total: {total}')
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import calculate_total

class TestPython1(unittest.TestCase):
    def test_total_of_least_expensive_drink(self):
        # Arrange
        flavor='oolong'
        milk='none'
        boba='no'

        # Act/Assert
        self.assertEqual(calculate_total(flavor, milk, boba), 4.5)

    def test_total_of_most_expensive_drink(self):
        # Arrange
        flavor='silver needle'
        milk='oat'
        boba='yes'
        
        # Act/Arrange
        self.assertEqual(calculate_total(flavor, milk, boba), 6.25)

```

##### !end-tests
### !end-challenge

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: b0746ef4-8fc2-4187-8c44-eb7a5c5adf58
* title: Number Converter

##### !question
The Ada Web Design company often has clients send them color changes for websites.  Sometimes the clients send these colors in RGB format, but websites use hexadecimal color codes to represent colors.  The RGB format describes a color by setting red, green and blue values in the range of 0-255.  Hex color codes also include red, green and blue values, but the values are converted to base-16, aka hexadecimal.

Write a function that converts an RGB color to to a hex color string.  This function should use the helper function `number_to_hex_string`, which takes a number and returns the hexadecimal representation of that number in a two digit string format.

* The RGB color will be passed into the function as red, green and blue values, each in the range of 0-255.  
* Hex color codes are in the format _#RRGGBB_, where RR is the red value in hexadecimal, GG is the green value in hexadecimal and BB is the blue value in hexadecimal.  

|example input `red`, `green`, `blue`| example output (return value) |
|--|--|
|`255, 255, 255`| `'#FFFFFF'`|
|`100, 50, 5`| `'#643205'`|
|`0, 0, 0`| `'#000000'`|

##### !end-question

##### !placeholder

```python

def color_converter(red, green, blue):
    pass

def number_to_hex_string(num):
    prefix = '0x'
    hex_string = hex(num)
    if hex_string.startswith(prefix):
        hex_string = hex_string[len(prefix):]
    if len(hex_string) < 2:
        hex_string = '0' + hex_string
    return hex_string.upper()

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import color_converter, number_to_hex_string


class TestPython1(unittest.TestCase):
    def test_red(self):
        #Arrange
        red = 255
        green = 0
        blue = 0
        #Act/Assert
        self.assertEqual(color_converter(red, green, blue), '#FF0000')

    def test_blue(self):
        #Arrange
        red = 0
        green = 0
        blue = 255

        #Act/Assert
        self.assertEqual(color_converter(red, green, blue), '#0000FF')

    def test_purple(self):
        #Arrange
        red = 106
        green = 13
        blue = 173

        #Act/Assert
        self.assertEqual(color_converter(red, green, blue), '#6A0DAD')
    
    def test_grey(self):
         #Arrange
        red = 75
        green = 75
        blue = 75

        #Act/Assert
        self.assertEqual(color_converter(red, green, blue), '#4B4B4B')
       
```
##### !end-tests


### !end-challenge

<!--END CHALLENGE-->