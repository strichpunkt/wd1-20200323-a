text = "This is a new text now\n"

filename = "foo.txt"

# apart from reading a file you can also
# store data in it. This can be done by
# adding a parameter in the open() function.
# a : append -> will append at the end
# w : write -> will overwrite (clears the file)
# r : read
# no parameter : automatically read

# the file is created automatically,
# once the open(..., "w") - function
# in writing mode is initiated 

# we can use the "with" keyword to simplify
# the file opening process
with open(filename, "a") as f:
    f.write(text)

# the file is closed automatically after
# the "with" clause is over

print("FINISHED WRITING, START READING")

with open(filename, "r") as f:
    content = f.read()
    print(content)


print("Done")
