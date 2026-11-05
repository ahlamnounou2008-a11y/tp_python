N1=str(input("saisir le premier nom:"))
N2=str(input("saisir le 2éme nom:"))
N3=str(input("saisir le 3éme nom:"))
A1=int(input("saisir l'age du premier:"))
A2=int(input("saisir l'age du 2éme :"))
A3=int(input("saisir l'age du 3éme:"))
if A3>A2>A1:
    print(N3)
elif A1>A2>A3:
    print(N1)
elif A2>A1>A3:
    print(N2)