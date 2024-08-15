# Dictionaries

<!-- PRECOURSE UPDATE -->
<!-- <iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=6b996ebc-da68-4315-a03b-ad6400489151&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe> -->

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand dictionaries
    * Create new dictionaries
    * Access key-value pairs in dictionaries
    * Update values of key-value pairs in dictionaries
* Combine dictionaries and lists

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1AmKeKvSJnNacUUIU9OLSInVohWJrPLkF?usp=sharing)

In this section we will be building on the code you wrote in the previous lesson [Lists](lists.md).  If you would like to look at our example code for that lesson, you can find it [here](resources/src/lists/games_list.md).

### Dictionaries, A New Kind of Data Structure

In the lists lesson we used our first data structure.  Lists are powerful and useful tools, but they do have some limitations.  Say we want to use our list to store all of the pieces of an address.  We could use several variables to store the city, state, zip code, street address, but as we saw in the list lesson, being able to store all of the information in one variable can make it simpler to access the data and pass the data to functions.  We can use a list to store each of these pieces of information, but we would need to remember the location where we stored them so we could access the elements by their index.  

We could set up constants like:

```python
STATE_INDEX = 0
CITY_INDEX = 1

address=["Washington", "Seattle"]

print(f"We live in {address[CITY_INDEX]}, {address[STATE_INDEX]}.")
```

Using constants to remember the indices would make the code easier to read, but it's still not ideal. Enter dictionaries!

Dictionaries __associate__ each piece of data with a unique key, and then we can use the key to access the data's value in the dictionary. In the case of our address data structure, we can use descriptive strings like "city" and "state", and then in our code whenever we want to access these pieces of the address, we can use the appropriate key to grab the data we want from the dictionary.

## Vocabulary and Syntax

| Vocab          | Definition                                                    | Synonyms  | How to Use in a Sentence                                                      |
| -------------- | ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| dictionary | A collection that associates unique keys with values | hash table, associative array | "This dictionary uses a planet name as the key and the value is its distance from the sun." |
| key | A key is used to retrieve a value stored in a dictionary. Keys in a dictionary must be unique. | name, label, or tag | "The keys for the dictionary are all the planets, 'mercury', 'venus', 'mars', and so on." |
| value | A piece of data of any possible type. Values in a dictionary, unlike keys, are not necessarily unique. | content | "The value for the key 'mercury' is '36 million miles'."|

Let's look at some Python syntax related to dictionaries. The snippet below shows how we can:
* Create an empty dictionary
* Create a dictionary with key-value pairs in it
* Add a key-value pair to a dictionary
* How to access a value from a dictionary with a key.

```python

# Syntax for creating an empty dictionary
empty_dict = {}

# Syntax for creating a dictionary with content
planet_dict = {
  "mercury": "36 million miles", 
  "venus": "67 million miles"
}

# Adding a new key-value pair to an existing dictionary
planet_dict["mars"] = "142 million miles"

# Accessing a value using a key
distance = planet_dict["venus"]
# distance = "67 million miles"

```  

### !callout-info

## Adding New Values to a Dictionary

Notice that we do not use a method to add a value to a dictionary in the example above. When adding a new element to a list, we used an `append` method, which adds the element at the end of the list.

<br />

We usually don't think about dictionaries having their keys in a particular order, so they do not provide a method for adding a key-value pair "at the end". Instead, by using regular square bracket syntax with the key, and assigning the value with the assignment operator, Python will add the key to the dictionary if needed, or update the value associated with the key if the key is already present. 

### !end-callout


## Heterogeneous vs. Homogeneous Dictionaries

Dictionaries store data using key-value pairs. Let's look at a few examples where the datatype of the values is different within a single dictionary (heterogeneous) and where the datatype of the values is the same within a single dictionary (homogeneous).

### Address
Let's look at how we might store an address using a dictionary in more detail.

```Python
adas_address = {
    "name":  "Ada Developers Academy"
    "street": ["315 5th Ave S", "Suite 200"]
    "city": "Seattle"
    "state": "WA"
    "zip_code": 98104
}
```

Notice that `adas_address` is a *heterogeneous* dictionary. The values associated with `"name"`, `"city"`, and `"state"` are *strings*. In contrast, the key `"street"` is associated with a value that is a *list* that holds the first and second lines of the address, and the key `"zip_code"` is associated with an *integer*.

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
* title: Dictionaries
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

1. Check to see if the dictionary does **not** contain the key
1. If the dictionary does not contain the key, return None
2. If the dictionary does contain the key, return the value associated with that key

<br/>

To check whether a key is in a dictionary, we can use the `in` operator.

```py
# True or False depending on whether some_key exists as a key in the dictionary some_dict
is_some_key_in_some_dict = some_key in some_dict
```

We can use the `not` operator with the `in` operator too. 
```py
# True or False depending on whether some_key does not exist as a key in the dictionary some_dict
is_some_key_in_some_dict = some_key not in some_dict
```

In general, the `in` operator checks whether some data is included in a data structure or string. For dictionaries, `in` checks whether a key is in a dictionary. If the key is present then the expression evaluates to `True` and if the key is absent then the expression evaluates to `False`.

##### !end-hint

<!--optional-->
##### !explanation

Some example solutions:

```python

def get_value_from_dictionary(dict, key):
    if key not in dict:
        return None
	        
    return dict[key]
    
def get_value_from_dictionary(dict, key):
    if key in dict:
        return dict[key]

    return None
```

Both solutions work and are very similar! Pay close attention to the `if` statement and what is returned from each approach. We prefer the first solution because using the key to access a value from the dictionary and returning it is the main logic. This logic is **not** nested inside a conditional block and is less indented. 

<br/>

While the second example works, it nests the logic of getting a value inside a conditional block and `return None` is emphasized as the main logic. Writing the code this way does not quite capture our intent to return some value from a dictionary.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

##### !challenge

* type: code-snippet
* language: python3.6
* id: e165737f-196a-4872-b674-4f70ccbb57e8
* title: Dictionaries
* points: 1
* topics: python, dictionaries

##### !question

Write a function `dict_counter` that takes two arguments, a dictionary and a key that may or may  not be in the dictionary.  The function has the following behavior:
1. If the key is in the dictionary, increment the integer value associated with that key by 1.  
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

1. Check to see whether the dictionary contains the key
1. If the dictionary contains the key, increment the value associated with that key
1. If the dictionary does not contain the key, add the key with the value 1 to the dictionary

<br/>

Another solution for this problem can look like this:

1. Check to see whether the dictionary does **not** contain the key
2. If the dictionary does **not** contain the key, add the key with the value 1 to the dictionary
3. If the dictionary contains the key, increment the value associated with that key

##### !end-hint

<!--optional-->
##### !explanation

An example solution:

```python

# Example 1
def dict_counter(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

    return dict

# Example 2
def dict_counter(dict, key):
    if key not in dict:
        dict[key] = 1
    else:
        dict[key] += 1

    return dict

```

These two solutions are very similar. The first example checks whether a key is in a dictionary. If the key, representing a letter, is present then that means there is already a value for the letter and the code should increment this value by 1 to indicate that another occurrence of the letter has been found in the word. If the key is absent from the dictionary, this condition is captured in the else block, then the value of the key is set to 1 because this is the first occurrence of the letter in the word.

<br/>

The second example is equivalent to the first one, but it flips the check for the if statement. Instead, this approach checks whether a key is **not** in the dictionary. If the key is not in the dictionary, then the code will set the value for the key to 1. This means that when the logic in the else block is executed that the key is already in the dictionary and that the value should be incremented by 1 to accurately count the number of times a letter is in the word.

<br/>

In the first example, the code that adds 1 to an existing integer value is written before the code that initializes the value to 1, but due to the `if` logic, that doesn't mean it will run first. When thinking about our code, we have to keep in mind the logical order (not just the textual order) the code will run in.

<br/>
	
Sometimes, we'll write our conditions so that the textual order of the instructions match the order we expect them to run. Other times, we might choose to use a condition that's easier to understand, but which results in the steps appearing to be "out of order." To more completely understand any code we read, we need to practice running the logic in our heads, not just reading the code in the order it appears.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: code-snippet
* language: python3.6
* id: 96892e63-ae9e-46d1-8638-37090db5a2d3
* title: Dictionaries
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

An example solution:

```python

def build_a_dictionary(keys, values):
    if len(keys) != len(values):
        return None
      
    result = {}
    for index in range(len(keys)):
        result[keys[index]] = values[index]
    return result
```

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Snowman Project

The last piece of our snowman game is displaying the word with the letters that the users have guessed correctly so far.  Open up your `snowman.py` and let's finish this game!

### Displaying User Progress

So far we have:

 *  The secret word 
 *  The list of correctly guessed letters  
 
Our end goal is to display each letter of the word with an underscore `_` if the letter has not yet been guessed and display the correct letter if it has been guessed.

### Building a Word Dictionary

Let's start by taking a look at the data structure that we're using to hold the correctly guessed letters.  Right now, it's a list.  If we wanted to find out if our user had guessed a particular letter from the word, we would need to loop through the list to see if we find the letter.  If we find the letter, we know our user has guessed it, and if we don't find the letter, we know they haven't.  That's a lot of work to find out if the user has guessed a particular letter!  Here's the code to solve this problem:

```python

# `correct_guesses_list` represents the letters in the secret word
correct_guesses_list = ["c", "a", "t"]

# Assume we have a variable `guessed_letter` that contains the letter that we're curious about
guessed_letter = "a"

# We haven't found `guessed_letter` in the list yet so we should set `result` to False.
result = False

# We want to check each letter in `correct_guesses_list` to see if it is the same as `guessed_letter`
for letter in correct_guesses_list:
    # if the letter in `correct_guesses_list` is the same as `guessed_letter` we can updated `result` to be `True`
    if letter == guessed_letter:
        # when `result` is set to `True` that means `guessed_letter` was a letter in the word.
        result = True

# If the condition in the if statement does not evaluate to `True`, then the value of `result` will still be `False` 
print(result)

```

You might be saying to yourself, what about the `in` operator?  We can just use the line of code `if guessed_letter in correct_guesses_list` to do this same thing, but under the hood, that `in` operator is doing the same search that's written above here.  Either way, finding things in a list always includes searching through the list one element at a time.  Also, we've got to do some logic work to say if it's in the list, then our user has guessed it, and if it isn't in the list then our user hasn't guessed it.

Luckily for us, we have dictionaries!  Dictionaries allow us to store a value with a key. Let's consider the following:
* We can put every letter from the secret word into the dictionary and set the initial values to `False`.
* When a user guesses a letter that's in the secret word, we can change the value to `True`.
* Then, if we want to know if a user has guessed a particular letter, we can just check the value for that letter in the dictionary and get a `True` or `False` answer that will tell us if our user has guessed that letter or not.

The first thing we need to do is store the letters from the secret word `snowman_word` in a dictionary, marking them all as "not guessed". Let's write a helper function `build_word_dict` that takes a string and returns a dictionary, where each unique letter from the word is a key and all of the values are `False`.  

<br>

<details>
<summary>Write <code>build_word_dict</code> and when you are finished, compare your code with ours.</summary>

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
        if letter not in word_dict:
            word_dict[letter] = False
    return word_dict
```

The end result here will be the same, in the first example any time we encounter a letter that is already in `word_dict` we'll overwrite it, but the values are always the same, so the end result of both of functions above will be the same.
</details>

### Using the Word Dictionary

Now that we have the `build_word_dict` function, we need to call it in our `snowman()` function and replace the `correct_guesses_list` with the new dictionary that's generated by `build_word_dict`. 

We will need to:
1. Remove the `correct_guesses_list` since we won't be using it anymore
2. Invoke `build_word_dict` and pass in `snowman_word` as an argument. We should use a variable called `snowman_dict` to capture the return value from calling the function.
3. Refactor the call to `get_letter_from_user` so that the first argument is `snowman_dict` instead of `correct_guesses_list`, but we'll still need `wrong_guesses_list` so we can leave the second argument as is.
4. Now that we have `snowman_dict`, we should use it to see if a user has correctly guessed a letter that is in the secret `snowman_word`  
5. If the user's guess is correct, then we need to update `snowman_dict` dictionary. Before a correct guess, a key (represented by a letter) has a value set to `False`. After a correct guess, we need to update the key's value to `True`
   - Since we're using `snowman_dict` instead of `correct_guesses_list`, we can now remove the line of code `correct_guesses_list.append(user_input)` 

<br>

<details>
<summary> When you are finished editing <code>snowman()</code>, compare your edits to ours.</summary>

In this solution, we have commented out obsolete lines of code to show where changes were made. Feel free to delete the lines of obsolete code in your own version to keep your solution uncluttered. Also note that we have changed the function call to `get_letter_from_user`, but we haven't changed the implementation of the function body yet so we should expect this function to be in a broken state. 

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(
      word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
      word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    print(f"debug info: {snowman_word}")

    # correct_guesses_list = []
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []

    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        # user_input = get_letter_from_user(correct_guesses_list, wrong_guesses_list)
        # This function call won't work yet, the next step is to update this function
        # to use the word dictionary instead of the list we were using before.
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)
        #if user_input in snowman_word:
        if user_input in snowman_dict: # instead of looking our letter up in the word
                                       # we can use the `in` operator with snowman_dict.  
                                       # Checking this way is faster than looking it up in
                                       # the word!
            print("You guessed a letter that's in the word!")
            # correct_guesses_list.append(user_input)
            snowman_dict[user_input] = True
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)

        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")

```

</details>

The next step is to update our helper function `get_letter_from_user` to use the word dictionary instead of the list of correct letters.  Right now, we're only telling a user whether they've guessed a letter before, but while we're updating this function, let's modify it to tell the user whether they've guessed a letter before, __and__ whether that letter is in the word or not.  

There is one important change of which to be aware. Right now we're just checking whether the letter the user guessed is in the list of correct letters.  If we do that with the dictionary, we'll end up with a logical error!  Consider these code snippets:

```python

# Snippet from the previous version of get_letter_from_user:

#...
elif user_input_string in wrong_guesses_list or user_input_string in correct_guesses_list:
    print("You have already guessed that letter")
#...

# assume we replace the parameter `correct_guesses_list` in the function call with the parameter `word_dict`
# if we just swap it in we'll end up with a logical error:

#...
elif user_input_string in wrong_guesses_list or user_input_string in word_dict:
    print("You have already guessed that letter")
#...

```
The logical error comes in because all of the letters from the word are already in `word_dict`, just with a `False` value! If we only check to see whether the letter is in `word_dict`, we'll tell the user that they've already guessed a letter even if it's the first time they've guessed it! We need to add a check that looks at the value to see whether it's `True` or `False`:

```python

#...
elif user_input_string in wrong_guesses_list or (user_input_string in word_dict and word_dict[user_input_string]):
    print("You have already guessed that letter")
#...

```

Update `get_letter_from_user` helper function and make the following changes:
1. Change the first parameter to be the word dictionary instead of a list
2. Add additional feedback to the user, when they attempt to guess a letter that they have already guessed, to inform them whether or not the letter is in the word.

<br>

<details>
<summary>
When you are finished updating <code>get_letter_from_user</code>, compare your code with ours:
</summary>

```python

def get_letter_from_user(word_dict, wrong_guesses_list):
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
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

```

</details>

### Displaying User Progress

Now we're going to get back to our original goal, displaying each letter of the word with an underscore `_` if the letter has not yet been guessed and the correct letter if it has been guessed.  For example, if the word is `pepper` and our user has guessed the letters `p`, and `r`, we want to print out `p _ p p _ r`.  Each time they guess a correct letter, we want to print out an updated version of this string.  We're going to start by writing a helper function that generates and returns this string.  This function will need to:

* Create an empty string
* Loop over each letter in the word
* Check whether the letter has been guessed or not
    * If the value of "guessed" is `True` add the letter to the string
    * If the value of "guessed" is `False` add `_` to the string
* Add 1 space between each letter/underscore

In `snowman.py` write a helper function `generate_word_progress_string` that takes two parameters, a word and a dictionary where each letter in the word is a key and the values are `True` or `False`.  The function returns a string that represents the word, with spaces between each letter.  For each letter, if the value in the dictionary is `True`, the letter is displayed.  If the value in the dictionary is `False`, the letter is replaced with a `_` character.

Example inputs and outputs:

|input|output|
|--|--|
|`word="pepper"` <br/> `word_dict={"p":True, "e": False, "r": False}`|`"p _ p p _ _"`|
|`word="tiger"` <br/> `word_dict={"e":False, "g": False, "i": False, "r": False, "t": False}`|`"_ _ _ _ _"`|
|`word="swamp"` <br/> `word_dict={"a":True, "m": True, "p": True, "s": True, "w": True}`|`"s w a m p"`|

### !callout-info

## Write Some Code, Check the Code, Repeat

As you're writing your implementation, be sure to call the helper function often so that you can see the output and confirm whether or not it's working. It's good practice to write a line or logical unit of code and then run it to check that you are getting the expected output before moving on to the next line of code. It is easier to identify where a bug is in one or two lines of code versus ten lines of code.

<br/>

If you run into a bug, add debugging print statements or walk through the code line by line and make predictions about what should happen versus what actually happens to help you resolve the bug. 

<br/>

Finally, recall that the helper function should __return__ a string. When you invoke the function, if you're not seeing any output printed to the terminal you will need to print the value returned from `generate_word_progress_string`.

<br/>

As always, feel free to reach out over Slack if you need help!

### !end-callout

<br>

<details>
<summary>Here is our implementation.</summary>

```python

def generate_word_progress_string(word, word_dict):
    output_string = ""
    letter_num = 0

    for letter in word:
        if letter_num > 0:
            output_string += " "

        if word_dict[letter]:
            output_string += letter
        else:
            output_string += "_"

        letter_num += 1

    return output_string
    
```

</details>

Now that we have the helper function `generate_word_progress_string` working, let's revisit our original goal.  Right now we're returning the progress string, but what we really want to do is display it. Let's switch to printing out the result instead of returning it. We'll rename our function to `print_word_progress_string`:

```python

def print_word_progress_string(word, word_dict):
    output_string = ""
    letter_num = 0
    
    for letter in word:
       # ...
       
    # return output_string
    print(output_string)

```

### Get Game Progress

The helper function `print_word_progress_string` provides a visual display of the player's progress towards guessing the word. We also need to write a function that indicates whether or not all the letters of the word have been guessed. We will name this function `get_word_progress`. The function `get_word_progress` should return `True` if all the letters have been guessed, and `False` otherwise.


This function will need to:

* Loop over each letter (key) in the `word_dict`
    * If `word_dict[letter]` is `False`, return `False`
* If the loop terminates without encountering a `False` value, return `True`

Write a helper function `get_word_progress(word, word_dict)` that takes two parameters, a word and a dictionary where each letter in the word is a key and the values are `True` or `False`.  The function returns `True` if every value in the dictionary is `True`. The function returns `False` if any of the values in the dictionary are `False`.

Example inputs and outputs:

|input|output|
|--|--|
|`word="pepper"` <br/> `word_dict={"p":True, "e": False, "r": False}`|`False`|
|`word="tiger"` <br/> `word_dict={"e":False, "g": False, "i": False, "r": False, "t": False}`|`False`|
|`word="swamp"` <br/> `word_dict={"a":True, "m": True, "p": True, "s": True, "w": True}`|`True`|

<br>
<details>

<summary>Here is our implementation.</summary>

```python

def get_word_progress(word, word_dict):
    for letter in word:
        if not word_dict[letter]:
            return False
    return True
    
```

</details>

### Snowman Project

We have all of the pieces we need to build the final version, and now it's time to bring all the pieces together into a fully functional Snowman game!  The last piece of the puzzle is to incorporate the `print_word_progress_string` and `get_word_progress` helper functions and end the game with a success message if the user guesses all of the letters in the word.  Use the following description of the final version as a guide and follow the link below to write and test your final version of Snowman!

Game Description:
1. User starts the game from the command line
1. A secret word is selected
1. User is prompted to guess a letter
1. The game checks the letter to see if it is in the word
1. The game prints out a section of the snowman drawing, showing one level for each incorrectly guessed letter
1. The game prints out a hidden version of the word, where each correct letter is displayed and un-guessed letters are hidden
1. The game prints out all of the incorrect letters that have been guessed
1. The game loops back to asking the user to guess a letter and continues that pattern until either the user has guessed all of the letters in the word, or the snowman drawing is complete.

[Click here to begin the Snowman Project checkpoint and write the final version!](snowman.checkpoint.md)

## Summary

Congratulations, you wrote two fully functional, interactive, playable command line games and you have completed the Ada Precourse curriculum!  We encourage you to continue to explore programming between now and when you start at Ada, in whatever form appeals to you.  If you're looking for some ideas, consider taking these projects and expanding them! Some ideas include building a dashboard for your user where they can choose the game they want to play, or expanding Snowman to a 'Wheel of Fortune' type game!