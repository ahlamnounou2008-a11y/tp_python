N = int(input("Entrer un entier positif : "))
s = 0
for i in range(1, N):
    if N % i == 0:
        s = s + i
if s == N:
    print(N, "est un nbr parfait")
else:
    print(N, "n'est pas un nbr parfait")