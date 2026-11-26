patient_A = [36.8, 37.2, 37.0, 36.9]
patient_B = [37.1, 38.0, 37.5, 37.3]
# Fusionner les deux listes. 
mesures = patient_A + patient_B
print(mesures)
# Calculer la moyenne des mesures des deux patients.
s = 0
for x in mesures:
    s = s + x
print(s / len(mesures))
# Trouver la valeur maximale.
print(max(mesures))
# Trouver la valeur minimale. 
print(min(mesures))
# Afficher les mesures supérieures à 37.5.
for x in mesures:
    if x > 37.5:
        print(x)
# Créer une nouvelle liste contenant les mesures des deux patients triés par ordre croissant. 
mesures.sort()
print(mesures)