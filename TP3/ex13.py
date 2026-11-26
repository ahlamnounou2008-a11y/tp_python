N=int(input("entrez un entier:"))
for i in range (2,N+1): 
    B=True
    for j in range (2,i):
        if i%j==0 :
            B=False
            break
    if B==True:
        print(i)
    