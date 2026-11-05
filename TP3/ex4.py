N = int(input("Entrez un entier positif : "))
S = 0
for i in range(1, N):
    if N % i == 0:
        S = S + i
if S == N:
    print(N, "est un nombre parfait")
else:
    print(N, "n'est pas un nombre parfait")