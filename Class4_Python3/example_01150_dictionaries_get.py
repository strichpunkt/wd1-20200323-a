capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Lithuania": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Vienna"}

print(capitals["France"])
print(capitals.get("France"))
print(capitals.get("Austria", "sometihng is wrong")) # second value is the return value
