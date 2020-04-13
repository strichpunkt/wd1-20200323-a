friends_dict = {}

friends_dict["Monika"] = "Good Friend"
friends_dict["Moritz"] = "Bad Friend"

print(friends_dict)

# you can delete entries using del
del friends_dict["Moritz"]

print(friends_dict)

friends_dict["Moritz"] = "Bad Friend"

print(friends_dict)
# you can update entries
# friends_dict["Moritz"] = "Good Friend"
friends_dict.update({"Moritz": "Good Friend"})

print(friends_dict)
