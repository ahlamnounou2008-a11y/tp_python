N = int(input("Entrez N (entier strictement positif) : "))
while N <= 0:
    N = int(input("N doit être > 0. Entrez N : "))
S = 0
for i in range(1, N + 1):
    S = S + 1 / i
print("S= ",S)