# Lists

## Learning Goals

## Introduction

### Textbook for this section: [link to ada built lists]

### Why Lists?

[todo: talk about why the need to add data strutures]

## Vocabulary

* list
* package: 

## Snowman

### Adding A Random Word

So far our Snowman game has used a constant as the secret word (`SNOWMAN_WORD = 'broccoli'), but a game that always uses the same word is not a great game.  The code to generate a random English word is outside of the scope of these lessons, although it is an interesting problem and worth spending some time thinking about.  We are going to use a _package_ to come up with a random word.  We are going to use the wonderword package.  Before you can use it in you code, you will need to install the package using the command line `pip3 install wonderwords`.  Once that's done, add the line `from wonderwords import RandomWord` to the top of your file.  Also add the constants `SNOWMAN_MAX_WORD_LENGTH = 8` and `SNOWMAN_MIN_WORD_LENGTH = 5` with the other constants at the top of the file.  This will instruct import the class `RandomWord` for us to use in our code.  Next, add the following lines of code to the top of your `snowman` function:

```python

    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)

```

The first line `r = RandomWord()` gives us a RandomWord object to work with.  We will not cover classes and objects in the pre-course material, but they will be a topic we will cover at Ada.  The next line, `snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)` will call the function `word` on the the RandomWord object `r` and give us a random word.  We are passing two arguments (word_min_length and word_max_length) using keyword arguments.  Again, we will not be covering these topics further in the pre-course, but they will come up later in the Ada curriculum.  The arguments that we are passing to the function `word` will instruct `word` to give us an English word where the length is between the SNOWMAN_MIN_WORD_LENGTH and SNOWMAN_MAX_WORD_LENGTH.  Feel free to experiment with setting different values for the constants.  The last piece of adding our new random word is replacing the constant `SNOWMAN_WORD` in the conditional test inside of the `snowman` function with the new `snowman_word` variable.

### Tracking User Input

So far all we have done with our user input is check to see if it is in our word, but if we go back to the hypothetical game of snowman with a group, we would want to keep track of the letters that had been guessed.  We would also not accept guesses of the same letter that had been guessed before.  Let's start with tracking incorrect guesses.  We know we are going to have a max of SNOWMAN_WRONG_GUESSES, so we could make that many variables and store our incorrect guesses in those variables.  This solution could be made to work, but every time we change the value of the constant we would have to rewrite our code.  Using a `list` gives us a way to store as many or as little wrong guesses as we want and will allow us to make the code flexible and easy to modify.  Start by addding an incorrect guesses list variable to the top of the `snowman` function:

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    wrong_guesses_list = []
    
    # ...

```

Next we need to add each incorrect guess to the list.  We are going to do this with the list function `append` which adds elements to the end of the list:

```python

# ...
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
# ...

```

In the previous version, we were incrementing a variable `wrong_guesses` each time the user guessed a letter that was not in the word, and then using that variable in the test for our while loop.  We can continue to use this variable, but we can use our list instead and simplify our code.  The number of elements in `wrong_guesses_list` is the number of incorrect guesses, so we can use the length of the list instead of the counter variable.  We get the length of the list by using the len() function.  We can also use the length of the list when we call the print_snowman_graphic function.  Here's the updated version of the function:

```python

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user()
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print_snowman_graphic(len(wrong_guesses_list))

```

###  


## Summary