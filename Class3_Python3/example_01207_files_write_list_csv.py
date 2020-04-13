import csv

# using the csv writer, makes sure that you can also save entries,
# which have a ',' (comma) in the string

planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter"]

filename = "planets.csv"

# CSV = Comma Separated Values

# if you want to store a list
# you can use the "join" method
with open(filename, "w") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(planets)

# if you want to read from a file
# and save the data as a list
# you can use the "split" method
with open(filename, "r") as f:
    spamreader = csv.reader(f, delimiter=',')
    for row in spamreader:
        print(', '.join(row))
