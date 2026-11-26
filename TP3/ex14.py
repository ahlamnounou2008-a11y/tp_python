N=str(input("entrez un mot:"))
A=""
for i in N:
    if i not in A :
        A=A+i
print("resultat:",A)