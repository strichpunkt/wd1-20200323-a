
capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Litauen": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Wien"}

print("Study the following list:")
print()
print(capitals.items())  # [('Canada', 'Ottawa'), ('\xc3\x96sterreich', 'Wien'), ('Iceland', 'Reykjavik'), ('France', 'Paris'), ('Denmark', 'Copenhagen'), ('Litauen', 'Vilnius')]
print()

# items gives a list of tuples
for country_capital in capitals.items():
    print(country_capital)

print()
print("="*40)
print()

# we can unpack in forloop
for country, capital in capitals.items():
    print(country, capital)

print(("Franek","Bartnik"))