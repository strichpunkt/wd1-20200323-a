# print the type of the variable number
number = 1
print(type(number))

# cast number to a string and print its type
number_text = str(number)
print(number_text)
print(type(number_text))


# cast the string digit_string to a float
digit_string = "123.12"
digit_float = float(digit_string)
print(digit_string)


# try to cast the following string to a number, what error do you get?
string = "1..2..3..Go!"

# int(string) -> ValueError