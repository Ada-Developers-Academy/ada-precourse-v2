# Helper Functions

## Learning Goals

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=a39ba8bc-1711-4c3a-a804-ad65007c2576&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

At the end of this lesson we will be able to:

- Identify places where helper functions would be useful
- Create helper functions
- Refactor larger functions into smaller pieces


## Introduction

A helper function is a function that does part of the work for another function. They make our code easier to read by breaking up long expressions or functions into smaller pieces. We recommend giving helper functions descriptive names, to help with readability.

## Single Responsibility Principle

### !callout-info

## Functions Best Practice

Ideally, every function should be designed to handle *one* task in accordance to the [single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle).  

### !end-callout

Let's recall the `convert_celsius_to_fahrenheit` example from the [Function](./functions.md) lesson. 

```Python
# an example function that returns a temperature in
# Celsius converted to Fahrenheit for numeric arguments
# and returns None for non-numeric arguments.
def convert_celsius_to_fahrenheit(temp):
    if not isinstance(temp, int) and not isinstance(temp, float):
        return None

    return 9/5*temp+32
```

This function `convert_celsius_to_fahrenheit` first validates that the `temp` is a numeric value, and then returns the `temp` converted to Fahrenheit.

In order to follow best practices, our functions should have a single responsibility. As such, we can write a helper function `valiate_num` to encapsulate the functionality of validating the argument `temp`.  We will call this helper function in `convert_celsius_to_fahrenheit`.

```Python
def validate_num(num):
    if isinstance(num, int) or isinstance(num, float):
        return True
    else:
        return False


def convert_celsius_to_fahrenheit(temp):
    if not validate_num(temp):
        return None
    
    return 9/5*temp+32
```

In addition to helping us follow the single responsibility principle, we may note that understanding the conditional logic in `validate_num` is a bit more straight forward than in the initial function, where we have a compound conditional that includes `not` before each condition (`if not isinstance(temp, int) and not isinstance(temp, float):`).

## Reuse

Another benefit of helper functions is that we can use them as many times as we like. Imagine that in addition to converting a temperature from Celsius to Fahrenheit, we also want to convert from Celsius to Kelvins. We can write another function `convert_celsius_to_kelvin` that also calls `validate_num`.

```Python
def validate_num(num):
    if isinstance(num, int) or isinstance(num, float):
        return True
    else:
        return False


def convert_celsius_to_fahrenheit(temp):
    if not validate_num(temp):
        return None

    return 9/5*temp+32


def convert_celsius_to_kelvin(temp):
    if not validate_num(temp):
        return None

    return temp+273.15


result = convert_celsius_to_fahrenheit(0)
print(result)  # 32

result = convert_celsius_to_fahrenheit("non numeric value")
print(result)  # None

result = convert_celsius_to_kelvin(0)
print(result)  # 273.15

result = convert_celsius_to_kelvin("non numeric value")
print(result)  # None
```

## Breaking Up Long Functions
Let's look at another example using helper functions to ensure functions have a single responsibility. In addition, this example will demonstrate how breaking up long functions using helper functions can enhance readability. 

Imagine we are building an ecommerce webapp that will display an order summary. In order to create this summary, multiple calculations must be performed: calculating the subtotal of all items purchased, calculating the sales tax, and calculating the grand_total. Then these values need to be displayed.

Let's look at a single function that performs all these tasks.

```Python
def calculate_and_display_bill(item_prices, sales_tax_rate):
    # calculate subtotal
    sub_total = 0
    for price in item_prices:
        sub_total += price

    # add subtotal to calculate sales tax
    sales_tax_total = sub_total * sales_tax_rate

    # calculate grand total
    grand_total = sub_total + sales_tax_total

    # display totals
    sub_total = f"${sub_total}:.2f"
    sales_tax_total = f"${sales_tax_total}:.2f"
    grand_total = f"${grand_total}:.2f"
    

    return (f"""
        **** Order Summary ****\n  
        Item(s) Subtotal:  {sub_total}
        Sales Tax:         {sales_tax_total}
        --------------
        Grand Total:       {grand_total}""")


bill = calculate_and_display_bill([5.00, 8.00, 10.00], 0.08)
print(bill)
# **** Order Summary ****
#
#        Item(s) Subtotal:  $ 23.00
#        Sales Tax:         $  1.84
#        --------------
#        Grand Total:       $ 24.84
```

Now let's look at how we could use helper functions to encapsulate the different parts of the problem including calculating the subtotal, calculating the sales tax, and formatting the numeric output with functions `calculate_subtotal`, `calculate_sales_tax`, and `format_cost`. 

```Python
def calculate_subtotal(item_prices):
    sub_total = 0
    for price in item_prices:
        sub_total += price

    return sub_total


def calculate_sales_tax(sub_total, sales_tax_rate):
    sales_tax_total = sub_total * sales_tax_rate
    return sales_tax_total


def format_cost(cost):
    return f"${cost:.2f}"
```

We will call these helper functions in a function `display_order_summary` that takes in the `item_prices` and `sales_tax_rate` and returns a string that summarizes the order.

```Python
def display_order_summary(item_prices, sales_tax_rate):
    sub_total = calculate_subtotal(item_prices)
    sales_tax_total = calculate_sales_tax(sub_total, sales_tax_rate)
    grand_total = sub_total + sales_tax_total

    return (f"""
        **** Order Summary ****\n  
        Item(s) Subtotal:  {format_cost(sub_total)}
        Sales Tax:         {format_cost(sales_tax_total)}
        --------------
        Grand Total:       {format_cost(grand_total)}""")


bill = display_order_summary([5.00, 8.00, 10.00], 0.08)
print(bill)
# **** Order Summary ****
#
#        Item(s) Subtotal:  $ 23.00
#        Sales Tax:         $  1.84
#        --------------
#        Grand Total:       $ 24.84
```

Note that each function is easier to read and has a single responsibility.

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
  1. `calculate_subtotal` runs and returns a value of 23.00 when finished.
  1. The expression result, 23.00, is assigned to `subtotal`. 

```python
# before right-hand side evaluation
sub_total = calculate_subtotal(item_prices)

# after right-hand side evaluation
sub_total = 23.00 
```

</details>

### !end-callout


## Breaking Up Long Expressions 

Sometimes code will have long expressions that are not easy to read. Imagine we are calculating the total cost of buying a car. We need to consider the sale price, the trade in value (if any), the registration costs, the document fees, and the sales tax. In this situation, sales tax is only applies to the sale price minus the trade in value. The sales tax does not apply to the registration, title, or document fees.

Let's examine this function for calculating the total cost.

```Python
def calculate_car_cost1(sale_price, trade_in_value, reg_fee, title_fee, doc_fee, is_electric, sales_tax_rate):
    return (sale_price - trade_in_value)*(1+sales_tax_rate) + reg_fee + title_fee + doc_fee

print(calculate_car_cost(12000, 5000, 500, 100, 100, 0.10))  # => 8400.0
```

```Python
def calculate_car_cost1(sale_price, trade_in_value, reg_fee, title_fee, doc_fee, sales_tax_rate):
    taxable_cost = sale_price - trade_in_value
    nontaxable_cost = reg_fee + title_fee + doc_fee
    return taxable_cost*(1+sales_tax_rate) + nontaxable_cost

print(calculate_car_cost(12000, 5000, 500, 100, 100, 0.10))  # => 8400.0
```

Our return expression is quite long and a bit unclear. Why is each computation within the mathematical expression necessary? Let's use helper functions to add clarity to this expression. 

We will create helper functions to return the total taxable cost, the total non-taxable cost, and the total sales tax. We will call these functions in an updated `calculate_car_cost` function. For calculating the non-taxable costs, rather then itemizing each of the costs (reg_fee, title_fee, and doc_fee), we will include them in a list similar to the previous example with menu items. 

```Python
def calculate_taxable_cost(sale_price, trade_in_value):
    return sale_price - trade_in_value


def calculate_nontaxable_cost(reg_fee, title_fee, doc_fee):
    return reg_fee + title_fee + doc_fee


def calculate_sales_tax(taxable_cost, sales_tax_rate):
    return sales_tax_rate * taxable_cost


def calculate_car_cost(sale_price, trade_in_value, reg_fee, title_fee, doc_fee, sales_tax_rate):
    return calculate_taxable_cost(sale_price, trade_in_value)*(1+sales_tax_rate) + calculate_nontaxable_cost(non_taxable_costs)


print(calculate_car_cost(12000, 5000, [500, 100, 100], 0.10))  # => 8400.0
```

Note that in addition to bring clarity the `calculate_car_cost`, the helper functions make the code easier to change and maintain. If the individual elements that go into the non-taxable cost change, we will only need to update the `calculate_non_taxable_cost` function.


Imagine we are writing a function to convert a speed in miles/hour to meters/second. We know that there are mimic the order of operations rule, [PEMDAS](https://en.wikipedia.org/wiki/Order_of_operations#Mnemonics). We could write the function as a long expression like so:


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

## Practice Problems 

### !challenge

* type: code-snippet
* language: python3.6
* id: a4494575-f4bd-4e33-8e5a-feae8510a30f
* title: Helper Functions
* points: 1
* topics: python, functions

##### !question

Ada Bubble Tea needs help creating `drink_summary` for their online order display. Each drink has three options: tea flavor, milk, and boba.  The tea flavor options are _oolong_ ($4.50), _jasmine_ ($4.50), and _silver needle_ ($5.00).  The milk options are _none_ ($0.00), _dairy_ ($0.50), _oat_ ($0.75), and _soy_ ($0.50).  The boba options are _yes_ ($0.50), and _no_ ($0.00).

Create the helper function `calculate_total`. It takes in parameters representing the order, and calculates the total to be used in `drink_summary`.

|example input `flavor`, `milk`, `boba`| example output (return value) |
|--|--|
|`'oolong', 'none', 'yes'`| `5.00`|
|`'silver needle', 'oat', 'yes'`| `6.25`|

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
* title: Speeding

##### !question
You are driving a car from another country in the United States. The speed limit limit is posted in MPH, but your car speedometer shows your speed in kilometers per hour. 

Write a function `am_i_speeding` that takes in a `speed` in units of kilometers per hour and a `speed_limit` in units of miles per hour. The function `am_i_speeding` should return 
- `True` if you are speeding
- `False` if you are are not speeding
- `None` if `speed` or `speed_limit` is not a float or an int.

The function `am_i_speeding` should use the following provided helper functions: 
- `convert_km_to_mi` to convert the `speed` to a mi/hr
- `validate_num` to validate that `speed` and `speed_limit` are a float or an int


|example input (`speed`, `speed_limit`)| example output (return value) |
|--|--|
|`100, 55`| `True`|
|`80, 55`| `False`|
|`"hello"`, `55`| `None`|
|`100`, `"hello"`| `None`|

##### !end-question

##### !placeholder

```python

def am_i_speeding(speed, speed_limit):
    pass

def convert_km_to_mi(num):
    return num*0.62137

def validate_num(num):
    if not isinstance(num, int) and not isinstance(num, float):
        return False
    else:
        return True

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import validate_num, convert_km_to_mi, am_i_speeding


class TestPython1(unittest.TestCase):
    def test_speeding_is_true(self):
        #Arrange
        speed = 100
        speed_limit = 55

        #Act/Assert
        self.assertEqual(am_i_speeding(speed, speed_limit), True)

    def test_speeding_is_false(self):
        #Arrange
        speed = 80
        speed_limit = 55

        #Act/Assert
        self.assertEqual(am_i_speeding(speed, speed_limit), False)

    def test_invalid_speed(self):
        #Arrange
        speed = "hello"
        speed_limit = 55

        #Act/Assert
        self.assertEqual(am_i_speeding(speed, speed_limit), None)
    
    def test_invalid_speed_limit(self):
        #Arrange
        speed = 100
        speed_limit = "hello"

        #Act/Assert
        self.assertEqual(am_i_speeding(speed, speed_limit), None)
       
```
##### !end-tests

##### !explanation

An example of a working implementation:

```Python
def am_i_speeding(speed, speed_limit):
    # validate speed and speed_limit
    if not validate_num(speed) or not validate_num(speed_limit):
        return None
    
    # convert speed to mi/hr and compare to speed_limit
    if convert_km_to_mi(speed) > speed_limit:
        return True
    else:
        return False      
```
##### !end-explanation


### !end-challenge

<!--END CHALLENGE-->

## Summary

Now that we have broken the various sections into functions, we can easily swap the order of the games, play a game multiple times, or add new games in new functions and insert them in any order we want.  

Functions add flexibility and structure to our code, and make code easier to maintain and read.  In the next lesson we will work on adding more functionality to our functions with loops. 

