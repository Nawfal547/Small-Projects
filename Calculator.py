"""Creating a Simple Calculator with Python"""

print("Select an operation to perform: ")
print("Type 1 for Addition ")
print("Type 2 for Subtraction ")
print("Type 3 for Multiplication ")
print("Type 4 for Division ")
their_input: int = int(input("What operation would you like to do? "))

def addition(first_number, second_number):
    print(first_number + second_number)

def subtraction(first_number, second_number):
    print(first_number - second_number)

def mult(first_number, second_number):
    print(first_number  * second_number)

def div(first_number, second_number):
    print(first_number / second_number)

if their_input == 1:
    first_number: int = int(input("What is your first number? "))
    second_number: int = int(input("What is your second number? "))
    addition(first_number, second_number)

if their_input == 2:
    first_number: int = int(input("What is your first number? "))
    second_number: int = int(input("What is your second number? "))
    subtraction(first_number, second_number)

if their_input == 3:
    first_number: int = int(input("What is your first number? "))
    second_number: int = int(input("What is your second number? "))
    mult(first_number, second_number)

if their_input == 4:
    first_number: int = int(input("What is your first number? "))
    second_number: int = int(input("What is your second number? "))
    div(first_number, second_number)
    