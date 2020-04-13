counter = 0
while True:
    counter += 1
    if counter == 10:
        break
    elif counter % 2 == 0:
        # unterbricht die schleife und geht an den anfang zurück
        continue
    else:
        print(counter)

#

counter = 0
while True:
    counter += 1
    if counter == 10:
        break
    elif counter % 2 == 0:
        # unterbricht die schleife und geht an den anfang zurück
        continue
    else:
        print(counter)
    print("========================="*3)