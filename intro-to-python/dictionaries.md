# Dictionaries

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=6b996ebc-da68-4315-a03b-ad6400489151&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand dictionaries
    * Create new dictionaries
    * Access key-value pairs in dictionaries
    * update values of key-value pairs in dictionaries
* Combine dictionaries and lists

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1AmKeKvSJnNacUUIU9OLSInVohWJrPLkF?usp=sharing)

In this section we will be building on the code you wrote in the previous lesson [Lists](lists.md).  If you would like to look at our example code for that lesson, you can find it [here](resources/src/lists/games_list.md).

### Dictionaries, A New Kind of Data Structure

In the lists lesson we used our first complex data structure.  Lists are powerful and useful tools, but they do have some limitations.  Say we want to use our list to store all of the pieces of an address.  We could of course use several variables to store the city, state, zip code, street address, but as we saw in the list lesson, being able to store all of the information in one variable can make it simpler to access the data and pass the data to functions.  If we use a list, we can store each of these pieces of information, but to access them we need to remember the index where we stored them.  

We could set up constants like:

```python
STATE_INDEX = 0
CITY_INDEX = 1

address=["Washington", "Seattle"]

print( f"We live in {address[CITY_INDEX]}, \
    {address[STATE_INDEX]}.")
```

Using constants to remember the indices would make the code easier to read, but it's still not ideal. Enter dictionaries!

Dictionaries associate each piece of data with a unique key, and then we can use the key to access the data in the dictionary. In the case of our address data structure, we can just make the keys meaningful words like "city" and "state", and then in our code whenever we want to access these pieces of the address, we can use the appropriate key to grab the data we want from the dictionary.

## Vocabulary and Syntax

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| dictionary | A collection that associates unique keys with values | hash table | "This dictionary uses planet names as the key and the value is the distance from the sun." |
| key | A string.  All of the keys in a dictionary must be unique. | address | "The keys for the dictionary are all the planets, 'mercury', 'venus', 'mars', and so on." |
| value | A piece of data of any possible type. | content | "The value for the key 'mercury' is '36 million miles'."|

```python

# Syntax for creating an empty dictionary
first_dict = {}

# Syntax for creating a dictionary with content
planet_dict = {"mercury":"36 million miles", 
"venus":"67 million miles"}

# Adding a new key-value pair to an existing dictionary
planet_dict["mars"] = "142 million miles"

# Accessing a key-value pair
distance = planet_dict["venus"]
# distance = "67 million miles"

```  

## Heterogeneous vs. Homogeneous Dictionaries

Dictionaries store data using key-value pairs. Let's look at a few examples where the datatype of the values is different within a single dictionary (heterogeneous) and where the datatype of the values is the same within a single dictionary (homogeneous).

### Address
Let's look at an address dictionary in more detail.

```Python
adas_address = {
    "name":  "Ada Developers Academy"
    "street": ["315 5th Ave S", "Suite 200"]
    "city": "Seattle"
    "state": "WA"
    "zip_code": 98104
}
```

Notice that `adas_address` is a *heterogeneous* dictionary. The values paired with `"name"`, `"city"`, and `"state"` are *strings*. In contrast, the `"street"` value is a *list* holding the first and second lines of the address, and the `"zip_code"` is an *integer*.

*Heterogeneous* dictionaries are often used to group data with different data types together. Later in the core curriculum, we will learn about classes and objects and how they are similarly used to group and store data with different data types.

### Planet Distance

Let's revisit the `planet_dict`: 

```Python
planet_dict = {
    "mercury": "36 million miles", 
    "venus": "67 million miles",
    "mars": "142 million miles", 
}
```

Notice that `planet_dict` is a *uniform* or *homogeneous* dictionary. All the values have the same data type, they are all *strings*. Given this, we may chose to drop the `"million miles"` from the values and instead use *integers* for the values. 

```Python
planet_dict = {
    "mercury": 36, 
    "venus": 67,
    "mars": 142, 
}
```

Now that all the values are *integers*, it is easy to iterate over the `planet_dict` and perform calculations as we no longer have to parse the numbers out of the string values and cast them to integers. For instance, we may want to calculate the average distance or the max distance. Iterating over the data and processing the data in a uniform fashion is one benefit of *homogeneous* dictionaries.

## Practice Problems

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 9af1ebe0-a2ec-42fb-b65f-479bd6e603e1
* title: Basic Dictionary Interactions
* points: 1
* topics: python, dictionaries

##### !question

Write a function `get_value_from_dictionary` that takes two arguments, a dictionary and a key that may or may not be in the dictionary.  The function has the following behavior:
* If the dictionary contains the key, the function returns the **value** for that the key.
* If the dictionary does not contain the key, the function returns `None`.

Example inputs and outputs:

|input|output|
|--|--|
| `dict = {"dog":"cat", "tree":"bush", "star":"planet"}` <br/> `key = "tree"`|`"bush"`|
| `dict = {"dog":"cat", "tree":"bush", "star":"planet"}` <br/> `key = "chocolate"`|`None`|
| `dict = {"dog":"cat", "tree":"bush", "star":"planet"}` <br/> `key = "cat"`|`None`|

##### !end-question

##### !placeholder

```python

def get_value_from_dictionary(dict, key):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import get_value_from_dictionary

class TestGetFromDict(unittest.TestCase):
    def test_success(self):
        self.assertEqual(get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "tree"), "bush")
    
    def test_failure(self):
        self.assertEqual(get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "chocolate"), None)
    
    def test_failure_key_is_value(self):
        self.assertEqual(get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "cat"), None)
    
    def test_success_2(self):
        self.assertEqual(get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet", "sign":"poster"}, "sign"), "poster")

```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Check to see if the dictionary contains the key
1. If the dictionary contains the key, return the value associated with that key
1. If the dictionary does not contain the key, return None

##### !end-hint

<!--optional-->
##### !explanation

Two working implementations:

```python

def get_value_from_dictionary(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None


def get_value_from_dictionary(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

##### !challenge

* type: code-snippet
* language: python3.6
* id: e165737f-196a-4872-b674-4f70ccbb57e8
* title: Dictionary Counter
* points: 1
* topics: python, dictionaries

##### !question

Write a function `dict_counter` that takes two arguments, a dictionary and a key that may or may  not be in the dictionary.  The function has the following behavior:
1. If the key is in the dictionary, increment the value associated with that key by 1.  
1. If the key is not in the dictionary, set the value for that key to 1.
1. Return the updated dictionary.

Example inputs and outputs:

|input|output|
|--|--|
| `dict = {"dog":1, "tree":1, "star":4}` <br/> `key = "tree"`|`{"dog":1, "tree":2, "star":4}`|
| `dict = {"dog":1, "tree":1, "star":4}` <br/> `key = "chocolate"`|`{"dog":1, "tree":1, "star":4, "chocolate":1}`|
| `dict = {}` <br/> `key = "chocolate"`|`{"chocolate":1}`|

##### !end-question

##### !placeholder

```python
def dict_counter(dict, key):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import dict_counter

class TestDictCounter(unittest.TestCase):
    def test_increment_existing(self):
        self.assertEqual(dict_counter({"dog":1, "tree":1, "star":4}, "tree"), {"dog":1, "tree":2, "star":4})
    
    def test_add_new(self):
        self.assertEqual(dict_counter({"dog":1, "tree":1, "star":4}, "chocolate"), {"dog":1, "tree":1, "star":4, "chocolate":1})
    
    def test_add_new_empty_dict(self):
        self.assertEqual(dict_counter({}, "chocolate"), {"chocolate":1})
    
    def test_sequence(self):
        dict = {"dog":1, "tree":1, "star":4}
        dict = dict_counter(dict, "cat")
        self.assertEqual(dict, {"dog":1, "tree":1, "star":4, "cat":1})
        
        dict = dict_counter(dict, "cat")
        self.assertEqual(dict, {"dog":1, "tree":1, "star":4, "cat":2})

```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Check to see if the dictionary contains the key
1. If the dictionary contains the key, increment the value associated with that key
1. If the dictionary does not contain the key, add the key with the value 1 to the dictionary

##### !end-hint

<!--optional-->
##### !explanation

Two working implementations:

```python

def dict_counter(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

    return dict


def dict_counter(dict, key):
    try:
        dict[key] += 1
    except KeyError:
        dict[key] = 1

    return dict

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 96892e63-ae9e-46d1-8638-37090db5a2d3
* title: Build a Dictionary
* points: 1
* topics: python, dictionaries

##### !question

Write a function `build_a_dictionary` that takes two arguments, a list of keys and a list of values.  The function has the following behavior:
1. Verify that the inputs are valid (the inputs are valid if the two lists match in length)
1. Create a new dictionary that contains all of the keys and values
1. The keys and values must be matched in order, ie, the key at index 0 in the key list goes with the value at index 0 in the value list
1. Return the new dictionary or None if the inputs are not valid

Example inputs and outputs:

|input|output|
|--|--|
|`keys=["dog", "cat", "bird", "mouse"]` <br/> `values=[1, 2, 3, 4]`|`{"dog":1, "cat":2, "bird":3, "mouse":4}`|
|`keys=[1, 2, 3, 4]` <br/> `values=["dog", "cat", "bird", "mouse"]`|`{1: "dog", 2: "cat", 3: "bird", 4: "mouse"}`|
|`keys=[1, 2,]` <br/> `values=["dog", "cat", "bird", "mouse"]`|`None`|
|`keys=["dog", "cat", "bird", "mouse"]` <br/> `values=[]`|`None`|

##### !end-question

##### !placeholder

```python

def build_a_dictionary(keys, values):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import build_a_dictionary

class TestBuildADictionary(unittest.TestCase):
    def test_success(self):
        self.assertEqual(build_a_dictionary(["dog", "cat", "bird", "mouse"], [1, 2, 3, 4]),{"dog":1, "cat":2, "bird":3, "mouse":4})

    def test_success_2(self):
        self.assertEqual(build_a_dictionary([1, 2, 3, 4], ["dog", "cat", "bird", "mouse"]), {1: "dog", 2: "cat", 3: "bird", 4: "mouse"})
    
    def test_failure_wrong_length(self):
        self.assertEqual(build_a_dictionary([1, 2,], ["dog", "cat", "bird", "mouse"]), None)
    
    def test_failure_empty_list(self):
        self.assertEqual(build_a_dictionary(["dog", "cat", "bird", "mouse"], []), None)


```
##### !end-tests

<!--optional-->
##### !hint

A solution for this problem can be broken into the following steps:

1. Check to see if the lengths of the list match
1. If the lengths match, loop over the lists and add each key-value pair to the dictionary
1. If the lengths do not match, return None

##### !end-hint

<!--optional-->
##### !explanation

Two working implementations:

```python

def build_a_dictionary(keys, values):
    if not len(keys) == len(values):
        return None
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result

def build_a_dictionary(keys, values):
    if len(keys) == len(values):
        result = {}
        for index in range(len(keys)):
            result[keys[index]] = values[index]
        return result
    else:
        return None
    

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman Project

The last piece of our snowman game is displaying the word with the letters that the users have guessed correctly so far.  Open up your `snowman.py` and let's finish this game!

### Displaying User Progress

So far we have:

 *  The word 
 *  The list of correctly guessed letters  
 
Our end goal is to display each letter of the word with an underscore, or '_' character, if the letter has not yet been guessed and the correct letter if it has been guessed.

### Building a Word Dictionary

Let's start by taking a look at the data structure that we're using to hold the correctly guessed letters.  Right now, it's a list.  If we wanted to find out if our user had guessed a particular letter from the word, we would need to loop through the list to see if we find the letter.  If we find the letter, we know our user has guessed it, and if we don't find the letter, we know they haven't.  That's a lot of work to find out if the user has guessed a particular letter!  Here's the code to solve this problem:

```python

# assume we have a variable 'letter' that contains the letter that we're curious about

for test_letter in correct_guesses_list:
    if test_letter == letter:
        result = True

# if we didn't find the letter in the list, we can set the result to False.
result = False

```

You might be saying to yourself, what about the `in` operator?  We can just use the line of code `if letter in correct_guesses_list` to do this same thing, but under the hood, that `in` operator is doing the same search that's written out above here.  Either way, finding things in a list always includes searching through the list one element at a time.  Also, we've got to do some logic work to say if it's in the list, then our user has guessed it, and if it isn't in the list then our user hasn't guessed it.

Luckily for us, we have dictionaries!  Dictionaries allow us to store a value with a key. Let's consider the following:
* We can put every letter from the secret word into the dictionary and set the initial values to `False`.
* When a user guesses a letter that's in the secret word, we can change the value to `True`.
* Then, if we want to know if a user has guessed a particular letter, we can just check the value for that letter in the dictionary and get a `True` or `False` answer that will tell us if our user has guessed that letter or not.

The first thing we need to do is convert the secret word `snowman_word` into a dictionary.  Write a helper function `build_word_dict` that takes a string and returns a dictionary, where each unique letter from the word is a key and all of the values are `False`.  

<details>
<summary>Write the helper function and when you are finished, compare your code with ours.</summary>

```python

def build_word_dict(word):
    word_dict = {}
    for letter in word:
        word_dict[letter] = False
    return word_dict

```

Notice that our function doesn't check to see if a letter is already in the dictionary.  If we wanted to, we could check and only add the letter if it's not already in the dictionary:

```python

def build_word_dict(word):
    word_dict = {}
    for letter in word:
        if not letter in word_dict:
            word_dict[letter] = False
    return word_dict
```

The end result here will be the same, in the first example any time we find an already existing letter we'll overwrite it, but the values are always the same, so the end result of both of functions above will be the same.
</details>

### Using the Word Dictionary

Now that we have the `build_word_dict` function we need to call it in our `snowman()` function and replace the `correct_guesses_list` with the new dictionary that's generated by `build_word_dict`.

<details>
<summary> Edit your `snowman()` function and when you are finished, compare your edits to ours.</summary>

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
                          word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    print(f"debug info: {snowman_word}")
    #correct_guesses_list = []
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        #user_input = get_letter_from_user(correct_guesses_list, wrong_guesses_list)
        # This function call won't work yet, the next step is to update this function
        # to use the word dictionary instead of the list we were using before.
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)
        #if user_input in snowman_word:
        if user_input in snowman_dict: # instead of looking our letter up in the word
                                       # we can use the `in` operator with snowman_dict.  
                                       # Checking this way is faster than looking it up in
                                       # the word!
            print("You guessed a letter that's in the word!")
            #correct_guesses_list.append(user_input)
            snowman_dict[user_input] = True
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

```

</details>

The next step is to update our helper function `get_letter_from_user` to use the word dictionary instead of the list of correct letters.  Right now, we're only telling a user if they've guessed a letter before, but while we're updating this function let's modify it to tell the user if they've guessed a letter before, and if that letter is in the word or not.  There is one important change to be aware of, right now we're just checking if the letter the user guessed is in the list of correct letters.  If we do that with the dictionary, we'll end up with a logical error!  Consider these code snippets:

```python

#snippet from the version of get_letter_from_user:

#...
elif user_input_string in list1 or user_input_string in list2:
    print("You already guessed that letter")
#...

# assume we replace the parameter list1 in the function call with the parameter `word_dict`
# if we just swap it in we'll end up with a logical error:

#...
elif user_input_string in word_dict or user_input_string in list2:
    print("You already guessed that letter")
#...

```

The logical error comes in because all of the letters from the word are in the word_dict!  If we only check to see if the letter is in the word_dict, we'll tell the user that they've already guessed a letter even if it's the first time they've guessed it if it's in the word!  We need to add a check that looks at the value to see if it's `True` or `False`:

```python

#...
elif (user_input_string in word_dict and word_dict[user_input_string]) or user_input_string in list2:
    print("You already guessed that letter")
#...

```

<details>
<summary>
Update your `get_letter_from_user` helper function and make the following changes:
1. Change the first parameter to be the word dictionary instead of a list
1. Add additional feedback to the user when they attempt to guess a letter that they have already guessed that informs them if the letter is in the word or not.

When you are finished, compare your code with ours:
</summary>

```python

def get_letter_from_user(word_dict, list2):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in word_dict and word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in list2:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

```

</details>

### Displaying User Progress

Now we're going to get back to our original goal, displaying each letter of the word with an '_' character if the letter has not yet been guessed and the correct letter if it has been guessed.  For example, if the word is `pepper` and our user has guessed the letters `p`, and `r`, we want to print out `p _ p p _ r`.  Each time they guess a correct letter, we want to print out an updated version of this string.  We're going to start by writing a helper function that generates and returns this string.  This function will need to:

* Create an empty string
* Loop over each letter in the word
* Check if the letter has been guessed or not
    * If the value of "guessed" is `True` add the letter to the string
    * If the value of "guessed" is `False` add '_' to the string
* Add 1 space between each letter/underscore

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 8b55c0e8-f7db-45e3-8fdc-ae6a70e0fb32
* title: Generate Word Progress String
* points: 1
* topics: python, dictionaries

##### !question

Write a helper function `generate_word_progress_string` that takes two parameters, a word and a dictionary where each letter in the word is a key and the values are `True` or `False`.  The function returns a string that represents the word, with spaces between each letter.  For each letter, if the value in the dictionary is `True`, the letter is displayed.  If the value in the dictionary is `False`, the letter is replaced with a `_` character.

Example inputs and outputs:


|input|output|
|--|--|
|`word="pepper"` <br/> `word_dict={"p":True, "e": False, "r": False}`|`"p _ p p _ _"`|
|`word="tiger"` <br/> `word_dict={"e":False, "g": False, "i": False, "r": False, "t": False}`|`"_ _ _ _ _"`|
|`word="swamp"` <br/> `word_dict={"a":True, "m": True, "p": True, "s": True, "w": True}`|`"s w a m p"`|

<!--This can be regular **Markdown**-->

##### !end-question

##### !placeholder

```python

def generate_word_progress_string(word, word_dict):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import generate_word_progress_string


class TestGetWordProgressString(unittest.TestCase):
    def test_mixed(self):
        self.assertEqual(generate_word_progress_string("pepper", {"p":True, "e": False, "r": False}), "p _ p p _ _")

    def test_all_false(self):
        self.assertEqual(generate_word_progress_string("tiger", {"e":False, "g": False, "i": False, "r": False, "t": False}), "_ _ _ _ _")
    
    def test_all_true(self):
        self.assertEqual(generate_word_progress_string("swamp", {"a":True, "m": True, "p": True, "s": True, "w": True}), "s w a m p")


```
##### !end-tests

<!--optional-->
##### !explanation

Here is our implementation:

```python

def generate_word_progress_string(word, word_dict):
    output_string = ""
    elem_num = 0

    for elem in word:
        if elem_num > 0:
            output_string += " "

        if word_dict[elem]:
            output_string += elem
        else:
            output_string += "_"

        elem_num += 1

    return output_string
    
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

Now that we have the helper function `generate_word_progress_string` working, let's revisit our original goal.  Right now we're returning the progress string, but what we really want to do is display it. Let's switch to printing out the result instead of returning it. We'll rename our function to `print_word_progress_string`:

```python

def print_word_progress_string(word, word_dict):
    output_string = ""
    elem_num = 0
    
    for elem in word:
       # ...
       
    #return output_string
    print(output_string)

```

### Getting Word Guessing Progress

The helper function `print_word_progress_string` provides a visual display of the players progress towards guessing the word. We also need to write a function that indicates whether or not all the letters of the word have been guessed. We will name this function `get_word_progress`. The function `get_word_progress` should return `True` if all the letters have been guesses, and `False` otherwise.


This function will need to:

* Loop over each letter (key) in the `word_dict`
    * If `word_dict[letter]` is `False`, return `False`
* If the loop terminates without encountering a `False` value, return `True`


<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: df6395a3-bf75-4fa0-a8ab-b39e1d5f707b
* title: Get Word Progress
* points: 1
* topics: python, dictionaries

##### !question

Write a helper function `get_word_progress(word, word_dict)` that takes two parameters, a word and a dictionary where each letter in the word is a key and the values are `True` or `False`.  The function returns `True` if every value in the dictionary is `True`. The function returns `False` if any of the values in the dictionary are `False`.

Example inputs and outputs:

|input|output|
|--|--|
|`word="pepper"` <br/> `word_dict={"p":True, "e": False, "r": False}`|`False`|
|`word="tiger"` <br/> `word_dict={"e":False, "g": False, "i": False, "r": False, "t": False}`|`False`|
|`word="swamp"` <br/> `word_dict={"a":True, "m": True, "p": True, "s": True, "w": True}`|`True`|

<!--This can be regular **Markdown**-->

##### !end-question

##### !placeholder

```python

def get_word_progress(word, word_dict):
    pass

```

##### !end-placeholder

##### !tests
```python

import unittest
from main import get_word_progress


class TestGetWordProgress(unittest.TestCase):
    def test_mixed_first_true(self):
        self.assertEqual(get_word_progress("pepper", {"p":True, "e": False, "r": False}), False)

    def test_mixed_last_true(self):
        self.assertEqual(get_word_progress("pepper", {"p":False, "e": False, "r": True}), False)

    def test_all_false(self):
        self.assertEqual(get_word_progress("tiger", {"e":False, "g": False, "i": False, "r": False, "t": False}), False)
    
    def test_all_true(self):
        self.assertEqual(get_word_progress("swamp", {"a":True, "m": True, "p": True, "s": True, "w": True}), True)


```
##### !end-tests

<!--optional-->
##### !explanation

Here is our implementation:

```python

def get_word_progress(word, word_dict):
    for elem in word:
        if not word_dict[elem]:
            return False
    return True
    
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

### Snowman Project

We have all of the pieces we need to build the final version, and now it's time to bring all the pieces together into a fully functional Snowman game!  The last piece of the puzzle is to incorporate the `print_word_progress_string` and `get_word_progress` helper functions and end the game with a success message if the user guesses all of the letters in the word.  Use the following description of the final version as a guide and follow the link below to write and test your final version of Snowman!

Game Description:
1. User starts the game from the command line
1. A secret word is selected
1. User is prompted to guess a letter
1. The game checks the letter to see if it is in the word
1. The game prints out a section of the snowman drawing, showing one level for each incorrectly guessed letters
1. The game prints out a hidden version of the word, where each correct letter is displayed and un-guessed letters are hidden
1. The game prints out all of the incorrect letters that have been guessed
1. The game loops back to asking the user to guess a letter and continues that pattern until either the user has guessed all of the letters in the word, or the snowman drawing is complete.

[Click here to begin the Snowman Project checkpoint and write the final version!](snowman.checkpoint.md)

## Summary

Congratulations, you wrote two fully functional, interactive, playable command line games and you have completed the Ada pre-course curriculum.  We encourage you to continue to explore programming between now and when you start at Ada, in whatever form appeals to you.  If you're looking for some ideas, consider taking these projects and expanding them! Some ideas include building a dashboard for your user where they can choose the game they want to play, or expanding Snowman to a 'Wheel of Fortune' type game!
