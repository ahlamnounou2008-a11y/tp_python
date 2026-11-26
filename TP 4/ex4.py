t = input("Entrez la chaîne principale : ")
m = input("Entrez le motif : ")
trouve = False
for i in range(len(t) - len(m) + 1):
    c = 0
    for j in range(len(m)):
        if t[i + j] == m[j]:
            c=c+1
            
    if c== len(m):
        print("Motif trouvé à l'indice :", i)
        trouve = True
if not trouve:
    print("Motif non trouvé")