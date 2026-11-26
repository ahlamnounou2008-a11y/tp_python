T=[36.8, 37.1, 37.5, 38.2, 37.9, 37.4]
#affichage de la liste de temperature:
print (T)
#affichage de la premiere et la derniere valeur:
print(T[0])
print(T[-1])
#affichage de la temperature dans la 3eme heure:
print(T[2])
#ajouter une nouvelle temperature:
T.append(37.2)
print(T)
#modifier la deuxième température par 37.0:
T[1]=37.0
print(T)
#supprimer la température 38.2:
T.remove(38.2)
print(T)
#afficher le nombre de températures enregistrées:
nbr=len(T)
print("nbr=",nbr)
#calculer la température moyenne:
my = sum(T) / len(T)
print("Moyenne=",my)
#afficher la température maximale et minimale:
print("Température maximale :", max(T), "°C")
print("Température minimale :", min(T), "°C")
#afficher les températures supérieures à 37.5 °C:
z = []
for i in range(0, len(T)):
    if T[i] > 37.5:
        z.append(T[i])
print(z)