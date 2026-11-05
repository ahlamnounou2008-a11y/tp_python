n = int(input("Entrez un entier positif : "))
s = 0
t = n
while t > 0:
    chiffre = t % 10
    fact = 1
    for i in range(1, chiffre + 1):
        fact =fact*i
    s =s+fact
    t =t//10
if s == n:
    print(n, "est un nombre fort")
else:
    print(n, "n'est pas un nombre fort")