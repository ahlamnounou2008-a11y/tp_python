Q=int(input("quantité achetée:"))
P=float(input("prix unitaire:"))
PT=Q*P
print("prix total avant réduction:",PT)
M=15*PT/100
print("le montant de la réduction:",M)
PF=PT-M
print("prix final à payer:",PF)