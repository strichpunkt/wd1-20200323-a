# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat

eingabe = None

while eingabe not in ["yes", "no"]:
    eingabe = input("Deine Eingabe: ")
else:
    print(f"Du hast endlich {eingabe} eingegeben und damit die Schleife beendet. DANKE!")