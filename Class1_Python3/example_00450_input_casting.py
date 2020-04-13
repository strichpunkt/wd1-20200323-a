entry = input("Enter a number: ")

my_number = float(entry)

print("You entered {}".format(my_number))

print(type(my_number))

bigger_than_30 = my_number > 30

if bigger_than_30:
    print("You entered a high number")
else:
    print("You entered a low number")
