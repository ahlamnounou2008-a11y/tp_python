chaine= input("Entrez une chaîne : ")
caractere= input("Entrez un caractère : ")
s = 0
for c in chaine:
    if c == caractere:
        s = s + 1
print("le caractere apparait", s, "fois")