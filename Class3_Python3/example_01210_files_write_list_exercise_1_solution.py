# use the list: particles = ["protons", "neutrons", "electrons"]
# open a file and write the elements of the list separated by a comma into the file
particles = ["protons", "neutrons", "electrons"]
filename = "particles.txt"

with open(filename, "w") as f:
    f.write(",".join(particles))
