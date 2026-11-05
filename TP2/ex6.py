A=int(input("A="))
B=int(input("B="))
if A>0 and B>0:
    r=A%B
    if r==0:
        print(A ,"est divisible par",B)
    else:
        print(A,"n'est pas divisible par",B)
else:
    print("veuillez saisir des nombres strictement positifs")