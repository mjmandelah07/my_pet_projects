# make a program to add,multiply,subtract and divide

# function to add
def addition(a, b):
    x = a + b
    return x


# function to subtract
def subtraction(x, y):
    a = x - y
    return a


# function to multiply
def multiplication(a, b):
    y = a * b
    return y


# function to divide
def division(x, y):
    a = x / y
    return a


print("select operation")
print("1.Add (+) ")
print("2.Subtract (-) ")
print("3.Multiply (*) ")
print("4.Divide (/) ")

while True:
    # selecting which operation to use by taking input from users
    choice = input("Enter the operation you want to perform (+, -, *, /): ")

    # check if choice is within the given operations
    if choice in ("+", "-", "*", "/"):
        num1 = float(input("Enter the first number to operate on: "))
        num2 = float(input("Enter the second number to operate on: "))

        if choice == "+":
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == "-":
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == "*":
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == "/":
            print(num1, "/", num2, "=", division(num1, num2))

        # check if the user wants to do another calculation, if not break
        another_calculation = input("Do you want to do another calculation (yes/no): ")
        if another_calculation == "no":
            break

    else:
        print("invalid input! Try again")

