# print welcome to user
print("Hallo, willkommen zu deinem persönlichen calculator! ")

# read user input for operation
# innerhalb vom string " wird zu ' sonst ist das argument zu Ende
operation = input("Please enter one of: '*', '/', '+', '-' ")

# read user input for first value
number_1 = float(input("Please enter first number: "))

# read user input for second value
number_2 = float(input("Please enter second number: "))

# calculate depending on operators
# also eine Definition von None ist notwendig für alle Werte, die über die if, else,... nicht abgedeckt sind?
result = None

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
# hier wird eine divison durch 0 abgefangen
elif operation == "/" and number_2 != 0:
    result = number_1 / number_2

# and print result
if result is None:
    print("Result could not be calculated, please try again")
else:
    print(f"{number_1} {operation} {number_2} = {result}")





