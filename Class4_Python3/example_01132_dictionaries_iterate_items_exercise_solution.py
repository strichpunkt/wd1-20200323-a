# coding=utf-8
# iterate through this dict, and print its keys and values
capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Litauen": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Wien"}

for country, capital in capitals.items():
    print("Country: " + country + ", Capital: " + capital)
