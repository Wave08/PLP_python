# A program that asks the user for two nmbers and a math operation and performs it

# User input numbers
num1 = int(input("Please type in a number:"))
num2 = int(input("Please type in a number:"))

# Choose operation
operation = input("Choose operation (+, -, * , /):")

if operation == "+":
    print(f"{num1} {operation} {num2} = {num1+num2}")
elif operation == "-":
    print(f"{num1} {operation} {num2} = {num1-num2}")
elif operation == "*":
    print(f"{num1} {operation} {num2} = {num1*num2}")
elif operation == "/":
    print(f"{num1} {operation} {num2} = {num1/num2}")