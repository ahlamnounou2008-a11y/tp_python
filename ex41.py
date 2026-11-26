patient = {
    "id": "P001",
    "nom": "Ahmed",
    "age": 25,
    "taille": 1.75,
    "poids": 70.5,
    "groupe_sanguin": "O+"
}

# 1
print(patient)
# 2
print(patient["nom"])
# 3
print(patient["age"])
# 4
print(patient["groupe_sanguin"])
# 5
patient["poids"] = 72.0
# 6
patient["sexe"] = "M"
# 7
del patient["taille"]
# 8
for x in patient:
    print(x)
# 9
for x in patient:
    print(patient[x])
# 10
for x in patient:
    print(x, patient[x])