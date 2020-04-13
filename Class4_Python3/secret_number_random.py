import random

secret_number = random.randint(1, 3)

counter = 0

while True:
    guess_str = input("Please guess the secret number:\n")

    if not guess_str.isdigit():
        print("Try again, please")
        continue

    guess = int(guess_str)

    counter += 1

    if guess == secret_number:
        print("Supa gmacht!")
        with open("results.txt", "w") as f_out:
            f_out.write(f"You needed {counter} attempts")
        break
    else:
        print("Leider nein")





