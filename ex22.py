resultat = ("ECG001", "Patient A", 78, "Normal")
# 1
a, b, c, d = resultat
# 2
print(a)
print(b)
print(c)
print(d)
# 3
temp = a
a = b
b = temp
print(a)
print(b)
# 4
nouveau = (a, c, d)
print(nouveau)
# 5
date = ("25/11/2026",)
final = nouveau + date
print(final)