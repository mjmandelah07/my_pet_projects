# POSITIVE NUMBER DETECTOR
# ask user to enter a number 
user_number = input("Enter a number: ")

try:
    user_number = int(user_number)
    if user_number >= 0:
        print("The number (", user_number, ") you entered is a positive number.")
    else:
        print("The number (", user_number, ") you entered is not a positive number.")   
except:
    print("This is not a number")         