rapport = """Patient : AhmedExamen : ECGFrequence cardiaque : 78Resultat : Normal"""
# 1
print(rapport)
# 2
print(len(rapport))
# 3
print(rapport.count("ECG"))
# 4
if "Normal" in rapport:
    print("Existe")
else:
    print("N'existe pas")
# 5
nouveau = rapport.replace("Normal", "À vérifier")
print(nouveau)
# 6
lignes = rapport.splitlines()
print(lignes)