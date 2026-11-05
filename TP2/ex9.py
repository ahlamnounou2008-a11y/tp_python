c = input("Entrez une lettre : ")
if "A" <= c <= "Z":
    print("Lettre majuscule")
elif "a" <= c <= "z":
    print("Lettre minuscule")
else:
    print("Autre caractère")