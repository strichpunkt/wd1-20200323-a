# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]
print("+-" in "+-/*")                # True -- hier könnte der user alle zeichen eingeben und es würde durchgehen
print("+-" in ["*", "+", "-", "/"])  # False -- hier wird nur ein zeichen akzeptiert

operation = None

while operation not in ["+", "-", "*", "/"]:
    operation = input("Please insert one of: '+', '-', '*', '/'")
else:
    print(f"Thank you, you entered: {operation}")