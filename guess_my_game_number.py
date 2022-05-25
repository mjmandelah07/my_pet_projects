# GUESS MY GAME NUMBER
# game number to guess
guess_number = 15
number_of_tries = 3
# get user  name and guessing number
try:
    user_name = input("Hello! Welcome to guess my game, what is your name? ")
    print("Hi " + user_name + "," + " You have ", number_of_tries, " tries to guess the right number")
    user_guess_number = int(input("Enter a valid guessed number: "))
except:
        print("Please enter a valid number")
        user_guess_number = int(input("Enter a valid  guessed number: "))

# compare users input with game number
while number_of_tries != 0:
    if user_guess_number < guess_number:
        # if users fail to get the right answer, minus the number of tries by 1
        number_of_tries -= 1
        print("Sorry, you got it wrong. Your number is lower than the guess number")
        print("You have ", number_of_tries, " more time to guess.")
        # ask the user to input another number to try again
        user_guess_number = int(input("Enter another valid  guessed number to try again: "))
    elif user_guess_number > guess_number:
        # if users fail to get the right answer, minus the number of tries by 1
        number_of_tries -= 1
        print("Oh, you got it wrong. Your number is greater than the guess number")
        print("You have ", number_of_tries, " more time to guess.")
        # ask the user to input another number to try again
        user_guess_number = int(input("Enter another valid  guessed number to try again: "))
    else:
        print("Congratulations, " + user_name + " You got it right!")
        break
else: 
    # Inform the users that they have exceeded their times of tries
    print("Oh, " + user_name + " you have exceeded the number of tries!")
    print("Please try again after 24 hours.")
    


    
        
    