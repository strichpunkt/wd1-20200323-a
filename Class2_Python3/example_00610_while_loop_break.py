counter = 0
while True:
    counter += 1

    if counter == 10000:
        # wenn ich in dieser Zeile ankomme, bringst du die Schleife ab und springst ans Ende
        break
    else:
        print(counter)

print("finished")
