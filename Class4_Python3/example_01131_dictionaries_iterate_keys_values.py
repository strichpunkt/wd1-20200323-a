
capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Litauen": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Wien"}

print("Study the following list:")
print()
print(capitals.keys()) # outputs a list of all keys
print(capitals.values()) # outputs a list of all values
print()

# items gives a list
for country in capitals.keys():
    print(country)

# we can unpack in forloop
for capital in capitals.values():
    print("The capital:",capital)
