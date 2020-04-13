# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]
print("+-" in "+-/*")                # True
print("+-" in ["*", "+", "-", "/"])  # False

user_input = None

while user_input not in ["*", "+", "-", "/"]:
    user_input = input("Please enter one of the following: '*', '+', '-', '/'")

print(f"You entered {user_input}")
