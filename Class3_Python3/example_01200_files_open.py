# imagine you want to save a text to a file

text = "This text should be in a nice file"

# open file to read
my_file = open("my_text.txt")

# my_file is now a "file object"
# we can extract data from the file using
# various methods

# .read() saves the data from the file as a string
my_lines = my_file.read()

# closing the file after using it is important
# an open file is temporarily stored in RAM
# too many open files will slow down your program
my_file.close()

print(my_lines)