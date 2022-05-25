import random


# Functions for difficulties stages(easy, medium, hard and very hard)
# The easy stage function
def easy():
    # number between 1 to 10
    number = random.randint(1, 10)
    # ask for the user name
    player_name = input("Hello, Welcome to easy stage! What's your name?")
    # print out the user name 
    print('Okay! ' + player_name + ' You are guessing a number between 1 and 10:')

    number_of_guesses = 0
    score = 10

    while number_of_guesses < 5:
        easy_guess = int(input("Enter an integer number from 1 to 10: "))
        # increase the number of guesses after each attempt
        number_of_guesses += 1
        if easy_guess < number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too low.")

        if easy_guess > number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too high.")

        if easy_guess == number:
            break

    if easy_guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries. So your score is:' + str(score))
    else:
        print('You did not guess the number, The number was ' + str(number) + ". Your score is:" + str(score))


# The medium stage function
def medium():
    # number between 1 to 20
    number = random.randint(1, 20)
    # ask for the user name
    player_name = input("Hello, Welcome to medium stage! What's your name?")
    # print out the user name
    print('Okay! ' + player_name + ' You are guessing a number between 1 and 20:')

    number_of_guesses = 0
    score = 10

    while number_of_guesses < 6:
        easy_guess = int(input("Enter an integer number from 1 to 20: "))
        # increase the number of guesses after each attempt
        number_of_guesses += 1
        if easy_guess < number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too low.")

        if easy_guess > number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too high.")

        if easy_guess == number:
            break

    if easy_guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries. So your score is:' + str(score))
    else:
        print('You did not guess the number, The number was ' + str(number) + ". Your score is:" + str(score))


# The hard stage function
def hard():
    # number between 1 to 50
    number = random.randint(1, 50)
    # ask for the user name
    player_name = input("Hello, Welcome to hard stage! What's your name?")
    # print out the user name
    print('Okay! ' + player_name + ' You are guessing a number between 1 and 50:')

    number_of_guesses = 0
    score = 10

    while number_of_guesses < 7:
        easy_guess = int(input("Enter an integer number from 1 to 50: "))
        # increase the number of guesses after each attempt
        number_of_guesses += 1
        if easy_guess < number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too low.")

        if easy_guess > number:
            # reducing the score after a failed attempt of guess
            score -= 1
            print("The number you guess is too high.")

        if easy_guess == number:
            break

    if easy_guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries. So your score is:' + str(score))
    else:
        print('You did not guess the number, The number was ' + str(number) + ". Your score is:" + str(score))


# The very hard stage function
def very_hard():
    # number between 1 to 100
    number = random.randint(1, 100)
    # ask for the user name
    player_name = input("Hello, Welcome to very hard stage! What's your name?")
    # print out the user name
    print('Okay! ' + player_name + ' You are guessing a number between 1 and 100:')

    number_of_guesses = 0
    score = 10

    while number_of_guesses < 10:
        easy_guess = int(input("Enter an integer number from 1 to 100: "))
        # increase the number of guesses after each attempt
        number_of_guesses += 1
        if easy_guess < number:
            # reducing the score after a failed attempt of guesses
            score -= 1
            print("The number you guess is too low.")

        if easy_guess > number:
            # reducing the score after a failed attempt of guesses
            score -= 1
            print("The number you guess is too high.")

        if easy_guess == number:
            break

    if easy_guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries. So your score is:' + str(score))
    else:
        print('You did not guess the number, The number was ' + str(number) + ". Your score is:" + str(score))


print("""
Hello, Welcome to guess my game!
There are three(3) stages in this game:
1.Easy
2.Medium
3.Hard
4.Very Hard
Kindly enter (1 for easy,  2 for medium, 3 for hard, 4 for very hard) to select the stage you wish to play below.
""")
while True:
    # asking for the user to input the stage they want to play
    stage = int(input("Enter an integer number between 1 to 4 to select your stage: "))
    # check if the input entered by the user is within the stages available  and invoke the stage
    if stage in range(1, 5):
        if stage == int(1):
            easy()

        elif stage == int(2):
            medium()

        elif stage == int(3):
            hard()

        elif stage == int(4):
            very_hard()

        # ask if the user wants to play another game
        another_game = input("Do you want to play another game? (yes/no): ")
        if another_game.lower() == "yes":
            continue
        else:
            break
    else:
        print("Invalid number! Try again ")
