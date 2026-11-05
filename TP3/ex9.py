chaine = input("Entrez une chaine : ")
n = ""
for c in chaine:
    if c != " ":
        n=n+c
inverse = ""
for c in n:
    inverse = c + inverse
if n == inverse:
    print(chaine, "est un palindrome")
else:
    print(chaine, "n'est pas un palindrome")