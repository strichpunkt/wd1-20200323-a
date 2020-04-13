# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat

user_input = None

while user_input.lower() not in ["yes", "no", "y", "n"]:
    user_input = input("Please enter one of: 'yes', 'y' , 'no', 'n'")

print(f"You entered {user_input}")
