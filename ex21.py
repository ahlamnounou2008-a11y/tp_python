patient = ("P001", "Ahmed", 25, 1.75, 70.5)
# Afficher le tuple complet.
print(patient)
# Afficher l'identifiant du patient. 
print(patient[0])
# Afficher le nom du patient.
print(patient[1])
# Afficher son âge. 
print(patient[2])
# Afficher sa taille et son poids. 
print(patient[3])
print(patient[4])
# Afficher le nombre d'éléments du tuple.
print(len(patient))
# Vérifier si le nom "Ahmed" existe dans le tuple.
if "Ahmed" in patient:
    print("Existe")
else:
    print("N'existe pas")
