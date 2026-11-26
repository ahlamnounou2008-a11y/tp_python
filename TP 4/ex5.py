n = int(input("Entrer un entier positif : "))
p = len(str(n))
s = 0
x = n
while x > 0:
    c = x % 10
    s = s + c ** p
    x = x // 10
if s == n:
    print(n, "est un nombre d'Armstrong")
else:
    print(n, "n'est pas un nombre d'Armstrong")
print("Les nombres d'Armstrong entre 1 et", n, "sont :")
for i in range(1, n + 1):
    p = len(str(i))
    s = 0
    x = i
    while x > 0:
        c = x % 10
        s = s + c ** p
        x = x // 10
    if s == i:
        print(i)