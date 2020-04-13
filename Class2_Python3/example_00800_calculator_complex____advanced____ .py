# print welcome to user
print("Welcome to the great Calculator Program!!")
print("="*40)

while True:
    # read user input for operation
    while True:
        operation_symbol = input("Please enter an operation (+,-,*,/): ")
        print("You entered " + operation_symbol)
        if operation_symbol in ["+", "-", "*", "/"]:
            break
        else:
            print("Please enter a valid operation, you entered: " + operation_symbol)

    # read user input for first value
    while True:
        try:
            num1 = input("Please enter you first number: ")
            num1 = float(num1)
            print("You entered " + str(num1))
            break
        except ValueError:
            print("Please enter a valid number, you entered: " + str(num1))

    while True:
        try:
            num2 = input("Please enter you second number: ")
            num2 = float(num2)
            print("You entered " + str(num2))
            break
        except ValueError:
            print("Please enter a valid number, you entered: " + str(num2))

    # calculate
    if operation_symbol == "+":
        print(num1 + num2)
    elif operation_symbol == "-":
        print(num1 - num2)
    elif operation_symbol == "*":
        print(num1 * num2)
    elif operation_symbol == "/":
        if num2 == 0:
            print("division by Zero!!!!!")
        else:
            print(num1 / num2)
    else:
        print("Invalid entry")

    # print result

    entry = input("One more time? (n to exit)")
    if entry == "n":
        break
