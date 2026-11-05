a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

if a == 0:
    if b != 0:
        solution = -c / b
        print("L'équation est du premier degré. Solution unique :", solution)
    else:
        if c == 0:
            print("L'équation est toujours vraie.")
        else:
            print("L'équation n'a pas de solution.")
else:
    delta = b**2 - 4*a*c
    print("Le discriminant (delta) est :", delta)

    if delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print("Deux solutions réelles : x1 =", x1, "et x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Une solution réelle unique : x =", x)
    else:
        print("Pas de solution réelle.")