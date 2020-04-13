# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt


secret = 7
guess = 0
versuche = 0

while True:
    versuche += 1
    guess = input("Guess the secret number")
    guess = int(guess)

    if guess == secret:
        print(f"Oh, so great!, you won! number of attempts: {versuche}")
        break
    else:
        print(f"Oh no, please try again. You already tried it {versuche} times.")