X = int(input("Entrez X : "))
N = int(input("Entrez N : "))
s = 1
for i in range(N):
    s = s * X
print(X, "**", N, "=", s)