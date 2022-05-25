# ask user for the numbers they want to perform operations on
number_1 = float(input("Please enter the first number to perform operations on: "))
number_2 = float(input("Please enter the second number to perform operations on: "))

# ask user which operation they want to perform
print("Which of these operations do you want to perform")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Division")
print("4 = modulus")

operation = float(input("Please enter 1 or 2 or 3 or 4 to select the operation to be performed on your numbers: "))


# declare function for addition, subtraction, and multiplication and modulus
def adds():
    print(number_1 + number_2)
 
 
def subtract():
    print(number_1 - number_2)
    
    
def divide():
    print(number_1 / number_2)
    
    
def modulo():
    print(number_1 % number_2)        
 
    

 
if operation == float(1):
        adds()
     
elif operation == float(2):
    subtract()
    
elif operation == float(3):
    divide()
    
elif operation == float(4):
    modulo()
else:
    print("Please choose a number between 1 and 4")