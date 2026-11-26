E = ["ECG", "IRM", "Scanner", "Échographe", "Moniteur multiparamétrique"]
#Afficher tous les équipements :
print(E)
#Ajouter un équipement : "Défibrillateur" :
E.append("Défibrillateur")
print(E)
#Supprimer "Scanner" :
E.remove("Scanner")
print(E)
#Vérifier si "ECG" existe dans la liste :
if "ECG" in E:
    print("ECG existe")
else:
    print("ECG n'existe pas")
#Afficher les équipements dont le nom contient plus de 8 caractères :
z = []
for i in range(0, len(E)):
    if len(E[i]) > 8:
        z.append(E[i])
print(z)
#Afficher le nombre total d'équipements :
n = len(E)
print("nbr =", n)
#Copier la liste dans une nouvelle variable :
C = E.copy()
#Afficher les deux listes :
print("Liste E :", E)
print("Liste C :", C)