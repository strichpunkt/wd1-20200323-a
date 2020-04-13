# sometime we would like to save a whole list of items

planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter"]

filename = "planets.txt"

with open(filename, "w") as f:
    f.write(planets)  # ERROR - > argument must be string
