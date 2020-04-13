import random, json

secret = random.randint(1, 30)
attempts = 0

# We create a high score list
# and load it at the beginning of the game
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort() # we sort the scores from lowest to highest
    print("Top scores: " + str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        # now we want to save the number of attempts
        # into the high score list
        score_list.append(attempts)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")