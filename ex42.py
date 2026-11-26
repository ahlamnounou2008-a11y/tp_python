equipements = {
    "ECG001": "Fonctionnel",
    "IRM001": "En maintenance",
    "SCN001": "Fonctionnel",
    "ECH001": "Hors service"
}
# 1
print(equipements)
# 2
print(equipements["IRM001"])
# 3
equipements["DEF001"] = "Fonctionnel"
# 4
equipements["ECH001"] = "En maintenance"
# 5
del equipements["SCN001"]
# 6
for x in equipements:
    if equipements[x] == "Fonctionnel":
        print(x)
# 7
print(len(equipements))
# 8
c = 0
for x in equipements:
    if equipements[x] == "Fonctionnel":
        c = c + 1
print(c)