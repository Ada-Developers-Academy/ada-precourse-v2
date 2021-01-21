# Dictionaries

## Learning Goals

At the end of this lesson students will be able to:

* Use and understand dictionaries
    * Create new dictionaries
    * Access key-value pairs in dictionaries
    * update values of key-value pairs in dictionaries
* Combine dictionaries and lists

## Introduction

### [Textbook for this section](https://colab.research.google.com/drive/1AmKeKvSJnNacUUIU9OLSInVohWJrPLkF?usp=sharing)

In this section we will be building on the code you wrote in the previous lesson [Lists](04-lists.md).  If you would like to look at our example code for that lesson, you can find it [here](/resources/src/04-lists/game-list.md).

### Dictionaries, A New Kind of Data Structure

In the lists lesson we used our first complex data structure.  Lists are powerful and useful tools, but they do have some limitations.  Say we want to use our list to store all of the pieces of an address.  We could of course use several variables to store the city, state, zip code, street address, but as we saw in the list lesson, being able to store all of the information in one variable can make it simpler to access the data and pass the data to functions.  If we use a list, we can store each of these pieces of information, but to access them we need to remember the index where we stored them.  

We could set up constants like:

```python
STATE_INDEX = 0
CITY_INDEX = 1

address=["Washington", "Seattle"]

print( f"We live in {address[CITY_INDEX]}, {address[STATE_INDEX]}.")
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
planet_dict = {"mercury":"36 million miles", "venus":"67 million miles"}

# Adding a new key-value pair to an existing dictionary
planet_dict["mars"] = "142 million miles"

# Accessing a key-value pair
distance = planet_dict["venus"]
# distance = "67 million miles"

```

## Snowman

The last piece of our snowman game is displaying to the user the letters they have guessed correctly.  We have:

 *  The word 
 *  The list of correctly guessed letters  
 
Our end goal is to display each letter of the word with an '_' character if the letter has not yet been guessed and the correct letter if it has been guessed.  

Every time a new correct letter is guessed, we want to update this display with the new information that we have.  One strategy is to use loops and lists to solve this problem by looping over each letter in the word and checking to see if it's in the list of guessed letters.  We could then use a conditional test to displaying either the letter or the underscore character.

Each time we search through our list it takes time, and using the above strategy we're repeating the same search every time we want to display our word.  A way to limit the number of times we do these searches is to save the result of the search.  We are going to use dictionaries to do that!  

We are going to build a dictionary for each letter that contains the letter and a "guessed" value that we can set to `True` or `False` to let us know if the user has guessed the letter.  We will store all of the dictionaries in a list and use the resulting list to construct our word display for our user.

### Creating the List of Dictionaries

1. The first step is to construct our list of dictionaries data structure.  We are going to write a helper function to do that called `build_word_list` which will take the secret word as a parameter return a list of dictionaries.  We will call this helper function at the top of snowman:

    ```python

    def snowman():
        r = RandomWord()
        snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
                              word_max_length=SNOWMAN_MAX_WORD_LENGTH)
        #print(f"debug info: {snowman_word}")
        snowman_list = build_word_list(snowman_word)
        # ...

    def build_word_list(word):
        word_list = []

        return word_list

    ```

1. Our word_list value is currently an empty list.  Our goal is to populate it with dictionaries that correspond to each letter.  To do this we will first need to loop over each letter in the word.  Luckily for us, python provides a useful `for/in` operator for strings that will loop over all of the characters in the string and store the characters in a variable that we can use inside the loop (syntax `for letter in word`):

    ```python

    def build_word_list(word):
        word_list = []
        for letter in word:
            pass # pass is a python keyword that means do nothing.  We are using it here as a placeholder.
        return word_list

    ```

1. Next we need to construct the dictionary that contains our letter and the guessed value

    ```python

    def build_word_list(word):
        word_list = []
        for letter in word:
            letter_dict = {"letter": letter, "guessed": False}
        return word_list

    ```

1. Last, we need to add the dictionary to `word_list`

    ```python

    def build_word_list(word):
        word_list = []
        for letter in word:
            letter_dict = {"letter": letter, "guessed": False}
            word_list.append(letter_dict)
        return word_list

    ```

### Displaying the List of Dictionaries

Now that we have this list, we need a way to display it to our user.  To do this we will write a helper function called `print_word_list`.  This function will take the word list as an argument and will print each letter as either an underscore ('_') or the letter.  We also want it to put spaces between each character.  This function will need to:

* Create an empty string
* Loop over each element of the list
* Check the value of the "guessed" key-value pair
    * If the value of "guessed" is true add the letter to the string
    * If the value of "guessed" is false add '_' to the string
* Add 1 space between each letter/underscore

<details>
<summary>Write the function and when you are finished, compare your code with ours</summary>

```python

def print_word_list(word_list):
    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)

```

</details>

The next step is to update the `snowman` function to print the word as part of the game play.  If we were playing in real life we would write out the number of underscores to show our players how many letters are part of the word, so we will want to that as part of our game.  We also want to print after we display the current state of the snowman after each guess.

<details>
<summary>Update your `snowman` function and when you are finished, compare your code with ours</summary>

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
                          word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    #print(f"debug info: {snowman_word}")
    snowman_list = build_word_list(snowman_word)
    correct_guesses_list = []
    wrong_guesses_list = []
    print_word_list(snowman_list)
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and not all_guessed:
        user_input = get_letter_from_user(correct_guesses_list, wrong_guesses_list)
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input)
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))
        print_word_list(snowman_list)
        print("Wrong guesses: " + " ".join(wrong_guesses_list))

```

</details>

### Updating the List of Dictionaries

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 82650cb3-48e5-4747-8ace-97f7b976b82a
* title: update_and_check_word_list
* points: 1
* topics: python, python-dictionaries

##### !question

Right now our `print_word_list` will always just print out underscores because we're not yet updating the list of dictionaries when our user guesses a correct letter.  The next step is to write a function that takes a letter and the list of dictionaries and updates the guessed boolean for each dictionary that contains that letter.  We are going to make this function do a little extra work.  We are also going to ask this function to return `True` or `False` to tell us if all of the letters have been guessed or not.  We already have to loop through the list to compare our letter to the letter value of each dictionary, so we can use the same loop to also check to see if all of the guessed values are `True`.  We will call the function `update_and_check_word_list`.

This function will:

* Accept a list of dictionaries and a letter as parameters
* Set the 'guessed' value to `True` for each dictionary who's 'letter' value matches the letter parameter
* Return `True` if all of the letters have been guessed and `False` if they have not.
  
##### !end-question

##### !placeholder

```python
def update_and_check_word_list(list_of_letters, guessed_letter):
    # Your code goes here

```
##### !end-placeholder

##### !tests

```py
import unittest
import main as p

class TestPython1(unittest.TestCase):

    def test_returns_false_if_not_all_letters_guessed(self):
        # Arrange
        input_letter = "n"
        input_list = [
            {
                "letter": "p",
                "guessed": True,
            },
            {
                "letter": "y",
                "guessed": True,
            },
            {
                "letter": "t",
                "guessed": False,
            },
            {
                "letter": "h",
                "guessed": False,
            },
            {
                "letter": "o",
                "guessed": False,
            },      
            {
                "letter": "n",
                "guessed": False,
            },            
        ]

        # Act
        answer = p.update_and_check_word_list(input_list, input_letter)

        # Assert
        assert not answer

    def test_true_if_all_letters_guessed(self):
        # Arrange
        input_letter = "y"
        input_list = [
            {
                "letter": "p",
                "guessed": True,
            },
            {
                "letter": "y",
                "guessed": False,
            },
            {
                "letter": "t",
                "guessed": True,
            },
            {
                "letter": "h",
                "guessed": True,
            },
            {
                "letter": "o",
                "guessed": True,
            },      
            {
                "letter": "n",
                "guessed": True,
            },                   
        ]

        # Act
        answer = p.update_and_check_word_list(input_list, input_letter)

        # Assert
        assert answer


    def test_changes_guessed_to_true_if_the_letter_matches(self):
        # Arrange
        input_letter = "t"
        input_list = [
            {
                "letter": "p",
                "guessed": True,
            },
            {
                "letter": "y",
                "guessed": False,
            },
            {
                "letter": "t",
                "guessed": False,
            },
            {
                "letter": "h",
                "guessed": True,
            },
            {
                "letter": "o",
                "guessed": True,
            },      
            {
                "letter": "n",
                "guessed": True,
            },                   
        ]

        # Act
        p.update_and_check_word_list(input_list, input_letter)

        # Assert
        assert input_list[2]["guessed"]

    def test_changes_guessed_to_true_if_the_letter_matches_for_first_letter(self):
        # Arrange
        input_letter = "p"
        input_list = [
            {
                "letter": "p",
                "guessed": False,
            },
            {
                "letter": "y",
                "guessed": False,
            },
            {
                "letter": "t",
                "guessed": True,
            },
            {
                "letter": "h",
                "guessed": True,
            },
            {
                "letter": "o",
                "guessed": True,
            },      
            {
                "letter": "n",
                "guessed": True,
            },                   
        ]

        # Act
        p.update_and_check_word_list(input_list, input_letter)

        # Assert
        assert input_list[0]["guessed"]

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->


### Snowman Project

It's time to bring all the pieces together into a fully functional Snowman game!

[Click here to begin the Snowman Project checkpoint and write the final version!](06-snowman.checkpoint.md)

## Summary

Congratuations, you wrote two fully functional, interactive, playable command line games and you have completed the Ada pre-course curriculum.  We encourage you to continue to explore programming between now and when you start at Ada, in whatever form appeals to you.  If you're looking for some ideas, consider taking these projects and expanding them! Some ideas include building a dashboard for your user where they can choose the game they want to play, or expanding Snowman to a 'Wheel of Fortune' type game!
