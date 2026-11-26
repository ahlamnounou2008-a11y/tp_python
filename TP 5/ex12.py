F = [72, 75, 80, 78, 85, 90, 76, 82]
#Afficher toutes les fréquences :
print(F)
#Ajouter une nouvelle mesure (par exemple 88) :
F.append(88)
print(F)
#Trier les fréquences par ordre croissant :
F.sort()
print("Ordre croissant :", F)
#Trier les fréquences par ordre décroissant :
F.sort(reverse=True)
print("Ordre décroissant :", F)
#Compter le nombre de mesures égales à 80 :
n = F.count(80)
print("nbr =", n)
#Rechercher si la fréquence 90 existe dans la liste :
if 90 in F:
    print("90 existe")
else:
    print("90 n'existe pas")
#Créer une nouvelle liste contenant uniquement les fréquences supérieures à 80 :
z = []
for i in range(0, len(F)):
    if F[i] > 80:
        z.append(F[i])
print(z)
#Calculer la moyenne des fréquences :
m = sum(F) / len(F)
print("Moyenne =", round(m, 2))