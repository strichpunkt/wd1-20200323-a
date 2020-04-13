# ask for a number to be inputted, and save it in a variable
# if the number is bigger than 1000, print You entered a very big number
# otherwise print The number is cute

number = input("Trag bitte eine Zahl ein: ")

number = int(number)

if number > 1000:
    print("You entered a very big number")
else:
    print ("The number is cute")

# ist genau das gleiche nur schon am anfang das "int"

number = int(input("Trag bitte eine Zahl ein: "))

if number > 1000:
    print("You entered a very big number")
else:
    print ("The number is cute")