# nested!
# dictionaries in dictionaries
account = {"name": "Zara", "age": 7, "occupation": "scientist"}

# now you can add another field, which is a new dictionary
account["skills"] = {}

# and add items to that dictionary within.
account["skills"]["Maths"] = "expert"
account["skills"]["Chemistry"] = "best"
print(account)
