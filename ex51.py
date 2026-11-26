identifiant = " p001-2026 "
# 1
print(identifiant)
# 2
identifiant = identifiant.strip()
# 3
identifiant = identifiant.upper()
# 4
identifiant = identifiant.replace("-", "_")
# 5
print(identifiant.startswith("P001"))
# 6
if "2026" in identifiant:
    print("Existe")
else:
    print("N'existe pas")
# 7
print(identifiant)