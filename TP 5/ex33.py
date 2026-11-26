groupe_A = {"Python", "C", "SQL", "Git"}
groupe_B = {"Python", "Java", "SQL", "Linux"}
# 1
print(groupe_A.intersection(groupe_B))
# 2
print(groupe_A.difference(groupe_B))
# 3
print(groupe_B.difference(groupe_A))
# 4
tous = groupe_A.union(groupe_B)
print(tous)
# 5
if groupe_A.issuperset(groupe_B):
    print("Oui")
else:
    print("Non")