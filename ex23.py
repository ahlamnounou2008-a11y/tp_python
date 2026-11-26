appareil_1 = (72, 75, 78, 80)
appareil_2 = (74, 76, 79, 82)
# 1
print(appareil_1 == appareil_2)
# 2
appareil_3 = appareil_1 + appareil_2
print(appareil_3)
# 3
print(appareil_1)
print(appareil_2)
# 4
s1 = 0
for x in appareil_1:
    s1 = s1 + x
m1 = s1 / len(appareil_1)
s2 = 0
for x in appareil_2:
    s2 = s2 + x
m2 = s2 / len(appareil_2)
print(m1)
print(m2)
# 5
if m1 > m2:
    print("Appareil 1")
else:
    print("Appareil 2")