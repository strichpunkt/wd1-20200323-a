secret = 7
guess = None
current_attempt = 1
max_attempts = 3

while True:
    try:
        guess = int(input("Please enter your guess: "))
    except:
        continue

    if guess == secret:
        print(f"Congrats, you found out the secret on your {current_attempt}th attempt!")
        break
    elif current_attempt >= max_attempts:
        print(f"You reached your maximum number of attempts. ({current_attempt})")
    else:
        print(f"Oh no, {guess} was not the secret. :( Please try again.")

    current_attempt += 1


#####################


limit = 3
counter = 0
secret = "7"

while counter < limit:
    guess = input("Guess the secret number: ")
    if guess == secret:
        print("Great!!!!")
        break
    else:
        print("Oh no, please try again")
    counter += 1

print("Game Over")
