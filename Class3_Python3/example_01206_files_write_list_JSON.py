import json
# JSON = JavaScript Object Notation
# can be used to save lists

planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter"]

filename = "planets.txt"

with open(filename, "w") as f:
    f.write(json.dumps(planets))

# the file is closed automatically after
# the "with" clause is over

print("FINISHED WRITING, START READING")

with open(filename, "r") as f:
    content = json.loads(f.read())
    print(content)


print("Done")