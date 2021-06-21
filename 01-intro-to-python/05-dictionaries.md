# Dictionaries

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=2cbe7e0c-5cf2-4f93-a242-acb80075f6af&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand dictionaries
    * Create new dictionaries
    * Access key-value pairs in dictionaries
    * update values of key-value pairs in dictionaries
* Combine dictionaries and lists

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1AmKeKvSJnNacUUIU9OLSInVohWJrPLkF?usp=sharing)

In this section we will be building on the code you wrote in the previous lesson [Lists](04-lists.md).  If you would like to look at our example code for that lesson, you can find it [here](resources/src/04-lists/games_list.md).

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
| dictionary | A collection that associates unique keys with values | hashtable | "This dictionary uses planet names as the key and the value is the distance from the sun." |
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
* If the dictionary contains the key, the function returns the value that matches the key.
* If the dictionary does not contain the key, the function returns None.

Example inputs and outputs:

input: ```get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "tree")
output: ```"bush"```

input: ```get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "chocolate")
output: ```None```

input: ```get_value_from_dictionary({"dog":"cat", "tree":"bush", "star":"planet"}, "cat")
output: ```None```

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
from main import *

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
* language: python2.7
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

input: ```dict_counter({"dog":1, "tree":1, "star":4}, "tree")
output: ```{"dog":1, "tree":2, "star":4}```

input: ```dict_counter({"dog":1, "tree":1, "star":4}, "chocolate")
output: ```{"dog":1, "tree":1, "star":4, "chocolate":1}```

input: ```dict_counter({}, "chocolate")
output: ```{"chocolate":1}```

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
from main import *

class TestDictCounter(unittest.TestCase):
    def test_increment_existing(self):
        self.assertEqual(dict_counter({"dog":1, "tree":1, "star":4}, "tree"), {"dog":1, "tree":2, "star":4})
    
    def test_add_new(self):
        self.assertEqual(dict_counter({"dog":1, "tree":1, "star":4}, "chocolate"), {"dog":1, "tree":1, "star":4, "chocolate":1})
    
    def test_add_new_empty_dict(self):
        self.assertEqual(dict_counter({}, "chocolate"), {"chocolate":1})
    
    def test_sequence(self)
        dict = {"dog":1, "tree":1, "star":4}
        dict = dict_counter(dict, "cat")
        self.assert_equal(dict, {"dog":1, "tree":1, "star":4, "cat":1})
        
        dict = dict_counter(dict, "cat")
        self.assert_equal(dict, {"dog":1, "tree":1, "star":4, "cat":2})


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

input: ```build_a_dictionary(["dog", "cat", "bird", "mouse"], [1, 2, 3, 4])```
output: ```{"dog":1, "cat":2, "bird":3, "mouse":4}```

input: ```build_a_dictionary([1, 2, 3, 4], ["dog", "cat", "bird", "mouse"])```
output: ```{1: "dog", 2: "cat", 3: "bird", 4: "mouse"}```

input: ```build_a_dictionary([1, 2,], ["dog", "cat", "bird", "mouse"])```
output: ```None```

input: ```build_a_dictionary(["dog", "cat", "bird", "mouse"], [])```
output: ```None```

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
from main import *

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

Luckily for us, we have dictionaries!  Dictionaries allow us to store a value with a key.  If we put every letter in the secret word into the dictionary, and set the initial values to `False`, we can change the value to `True` when a user guesses a letter that's in the list.  Then, if we want to know if a user has guessed a particular letter, we can just check the value for that letter in the dictionary and get a `True`/`False` answer that will tell us if our user has guessed that letter or not.

The first thing we need to do is convert the secret word `snowman_word` into a dictionary.  Write a function `build_word_dict` that takes a string and returns a dictionary, where each unique letter from the word is a key and all of the values are `False`.  

<details>
<summary>Write the function and when you are finished, compare your code with ours.</summary>

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

The next step is to update our function `get_letter_from_user` to use the word dictionary instead of the list of correct letters.  Right now, we're only telling a user if they've guessed a letter before, but while we're updating this function let's modify it to tell the user if they've guessed a letter before, and if that letter is in the word or not.  There is one important change to be aware of, right now we're just checking if the letter the user guessed is in the list of correct letters.  If we do that with the dictionary, we'll end up with a logical error!  Consider these code snippets:

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
Update your `get_letter_from_user` function and make the following changes:
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

Now we're going to get back to our original goal, displaying each letter of the word with an '_' character if the letter has not yet been guessed and the correct letter if it has been guessed.  For example, if the word is `pepper` and our user has guessed the letters `p`, and `r`, we want to print out `p _ p p _ r`.  Each time they guess a correct letter, we want to print out an updated version of this string.  We're going to start by writing a function that generates and returns this string.  This function will need to:

* Create an empty string
* Loop over each letter in the word
* Check if the letter has been guessed or not
    * If the value of "guessed" is true add the letter to the string
    * If the value of "guessed" is false add '_' to the string
* Add 1 space between each letter/underscore

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 8b55c0e8-f7db-45e3-8fdc-ae6a70e0fb32
* title: Get Word Progress
* points: 1
* topics: python, dictionaries

##### !question

Write a function `get_word_progress` that takes two variables, a word and a dictionary where each letter in the word is a key and the values are `True` or `False`.  The function returns a string that represents the word, with spaces between each letter.  For each letter, if the value in the dictionary is `True`, the letter is displayed.  If the value in the dictionary is `False`, the letter is replaced with a `_` character.

Example inputs and outputs:

input: ```get_word_progress("pepper", {"p":True, "e": False, "r": False})```
output: ```"p _ p p _ _"```

input: ```get_word_progress("tiger", {"e":False, "g": False, "i": False, "r": False, "t": False})```
output: ```"_ _ _ _ _"```

input: ```get_word_progress("swamp", {"a":True, "m": True, "p": True, "s": True, "w": True})```
output: ```"s w a m p"```

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

import main
import unittest
from main import *


class TestGetWordProgress(unittest.TestCase):
    def test_mixed(self):
        self.assertEqual(get_word_progress("pepper", {"p":True, "e": False, "r": False}), "p _ p p _ _")

    def test_all_false(self):
        self.assertEqual(get_word_progress("tiger", {"e":False, "g": False, "i": False, "r": False, "t": False}), "_ _ _ _ _")
    
    def test_all_true(self):
        self.assertEqual(get_word_progress("swamp", {"a":True, "m": True, "p": True, "s": True, "w": True}), "s w a m p")


```
##### !end-tests

<!--optional-->
##### !explanation

Here is our implementation:

```python

def get_word_progress(word, word_dict):
    output_string = ""
    for elem in word:
        if word_dict[elem]:
            output_string += elem
        else:
            output_string += "_"
        output_string += " "
    return output_string

```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

Now that we have the function `get_word_progress` working, let's revisit our original goal.  Right now we're returning the display string, but we really want to display it.  Also, the name of the function `get_word_progress` implies that we're going to get some information about our user's progress toward guessing all of the letters.  Let's revisit this function and make some minor changes.

First, let's switch to printing out the result instead of returning it:

```python

def get_word_progress(word, word_dict):
    output_string = ""
    for elem in word:
       # ...
    #return output_string
    print(output_string)

```

Next, we want to return either `True` or `False`.  We are already looping through the word to build the output string, so now we need to add some logic to determine if every letter in the word has been guessed or not.  If all of them have been guessed, the function returns `True`.  If any of them haven't been guessed, the function returns `False`.

<details>
<summary> Edit your `get_word_progress` function and when you are finished, compare your edits to ours.</summary>
</summary>

```python

def get_word_progress(word, word_dict):
    output_string = ""
    result = True
    for elem in word:
        if word_dict[elem]:
            output_string += elem
        else:
            result = False
            output_string += "_"
        output_string += " "
    print(output_string)
    return result

```

</details>

### Snowman Project

We have all of the pieces we need to build the final version, and now it's time to bring all the pieces together into a fully functional Snowman game!  The last piece of the puzzle is to incorporate the `get_word_progress` function and end the game with a success message if the user guesses all of the letters in the word.  Use the following description of the final version as a guide and follow the link below to write and test your final version of Snowman!

Game Description:
1. User starts the game from the command line
1. A secret word is selected
1. User is prompted to guess a letter
1. The game checks the letter to see if it is in the word
1. The game prints out a section of the snowman drawing, showing one level for each incorrectly guessed letters
1. The game prints out a hidden version of the word, where each correct letter is displayed and unguessed letters are hidden
1. The game prints out all of the incorrect letters that have been guessed
1. The game loops back to asking the user to guess a letter and continues that pattern until either the user has guessed all of the letters in the word, or the snowman drawing is complete.

[Click here to begin the Snowman Project checkpoint and write the final version!](06-snowman.checkpoint.md)

## Summary

Congratuations, you wrote two fully functional, interactive, playable command line games and you have completed the Ada pre-course curriculum.  We encourage you to continue to explore programming between now and when you start at Ada, in whatever form appeals to you.  If you're looking for some ideas, consider taking these projects and expanding them! Some ideas include building a dashboard for your user where they can choose the game they want to play, or expanding Snowman to a 'Wheel of Fortune' type game!
