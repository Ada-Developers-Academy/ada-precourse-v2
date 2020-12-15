RANGE_LOW = 0
RANGE_HIGH = 100

random.seed()
random_number = random.randrange(RANGE_LOW, RANGE_HIGH)

user_input_string = input("Guess the number: ")
user_input = None

if(user_input_string.isnumeric()):
    user_input = int(user_input_string)
    if(user_input == random_number):
        print("You guessed the number!  Good job!")
    if(user_input > random_number):
        print("Your guess is too high")
    if(user_input < random_number):
        print("Your guess is too low")
    if(user_input < RANGE_LOW or user_input > RANGE_HIGH):
        print(f"Your guess is out of bounds.  The maximum is {RANGE_LOW} and the minimum is {RANGE_HIGH}")
elif:
    print("You must input a number!")

