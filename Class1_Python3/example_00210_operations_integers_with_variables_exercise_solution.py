# Task 1

# define 2 variable and give them the values 2 and 10, then calculate the result of the division 2/10.
# print the result
print("division 2/10: ")
# write your code here
x = 2.0
y = 10.0
ergebnis = x / y
print(ergebnis)
print()



# Task 2

# save your first name and last name as string, and concat them to 1 variable,
# and print the result
print("printing first name and last name as strings: ")
# write your code here
vorname = "Arnold"
nachname = "Schwarzenegger"
name = vorname + " " + nachname
print(name)
print()


# Task 3

# divide a number by 0, what happens?
print("divide a number by '0' ")
# write your code here
print(5 / 0)
print()

"""
try:
    5/0
except ZeroDivisionError:
    print "Do not divide by zero"
"""
'''

try:
    int("abc")
except ValueError:
    print "Please enter a number"

try:
    int("abc")
except Exception:
    print "Please enter a number"
    
'''
