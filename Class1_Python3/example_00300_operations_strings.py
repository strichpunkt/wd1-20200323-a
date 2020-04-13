greeting = "Hello World!"
name = "Smartninja!"

# ADDING STRINGS (CONCAT)
print(greeting)
print(greeting + " - AI ")

# MULTIPLYING STRINGS
print("*" * 20)

# PRINTING THEM BY INSERTING
print("Greeting: {}, Name: {}".format(greeting, name))
# new in Python 3:
print(f"Greeting: {greeting}, Name: {name}")

# CHECKING FOR (UN)EQUALITY
print(greeting == name)
print(greeting == "Hello World!")

# CHECKING FOR OCCURRENCE
print(greeting in "Hello World! is the first greeting in a computer language")

# WATCH OUT FOR USING THE CORRECT TYPES
print("3" + "3")
print(int("3") + int("3"))
print(str(3))

# print int("3") + "3"      # TypeError
# print int("a")            # ValueError
