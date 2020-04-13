# save the following list in a file
continents = ["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", "Oceania"]
# using one of the methods discussed previously


# option 1 : JSON
# ===============
import json

with open("continents.json", "w") as f:
    json.dump(continents, f)

# json can be also written with this:
# with open("continents.json", "w") as f:
#     f.write(json.dumps(continents))
#     json.dump(continents, f)
# however the first method with json.dump is preferable


# option 2: csv
# ===============
import csv

with open("continents.csv", "w") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(continents)


# option 3: simple python
# ==============================
with open("continents.txt", "w") as f:
    f.write(",".join(continents))
