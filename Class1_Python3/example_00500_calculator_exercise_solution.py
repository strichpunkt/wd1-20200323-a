# print welcome to user
print("Welcome to the great Calculator Program!!")
print("-"*40)

# read user input for operation
operation_symbol = input("Please enter an operation (+,-,*,/): ")
print("You entered " + operation_symbol)

# read user input for first value
num1 = int(input("Please enter you first number: "))
print("You entered " + str(num1))

# read user input for second value
num2 = float(input("Please enter you second number: "))
print("You entered " + str(num2))

# calculate depending on operators
# and print result

if operation_symbol == "+":
    print(num1 + num2)
elif operation_symbol == "-":
    print(num1 - num2)
elif operation_symbol == "*":
    print(num1 * num2)
elif operation_symbol == "/":
    print(num1 / num2)
else:
    print("Invalid entry")
