# now read the continents you have written previously

# option 1 : JSON
import json

with open("continents.json", "r") as f:
    continents = json.load(f)
    print(continents)

# option 2: csv

import csv

with open("continents.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(', '.join(row))

# option 3: simple python

with open("continents.txt", "r") as f:
    content = f.read()
    continents = content.split(",")  # separate by "," and create list
    print(continents)
