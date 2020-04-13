planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter"]

filename = "planets.csv"

# CSV = Comma Separated Values

# if you want to store a list
# you can use the "join" method
with open(filename, "w") as f:
    content = ",".join(planets)  # join elements by adding a "," in-between, creates a string
    f.write(content)

# if you want to read from a file
# and save the data as a list
# you can use the "split" method
with open(filename, "r") as f:
    content = f.read()
    a_list = content.split(",")  # separate by "," and create list
    print(a_list)
