constantes = {
    "temperature": 37.2,
    "frequence_cardiaque": 78,
    "frequence_respiratoire": 16,
    "saturation_oxygene": 98
}
# 1
print(constantes)
# 2
print(constantes["temperature"])
# 3
constantes["frequence_cardiaque"] = 82
# 4
constantes["pression_arterielle"] = 120
# 5
for x in constantes:
    print(x, constantes[x])
# 6
s = 0
for x in constantes:
    s = s + constantes[x]
moyenne = s / len(constantes)
print(moyenne)
# 7
noms = []
for x in constantes:
    noms.append(x)

print(noms)