while True:
    entry = input("Do you want to continue? (y,n)")
    if entry.lower() == "y":
        print("lets continue")
    elif entry.lower() == "n":
        break
    else:
        print("Invalid input, restart")

print("finished")
