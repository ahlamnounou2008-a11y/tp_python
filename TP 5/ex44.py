patients = {
    "P001": {"nom": "Ahmed", "age": 25, "temperature": 37.1},
    "P002": {"nom": "Sara", "age": 30, "temperature": 36.8},
    "P003": {"nom": "Youssef", "age": 40, "temperature": 37.5}
}
# 1
for x in patients:
    print(x, patients[x])
# 2
print(patients["P002"]["nom"])
# 3
print(patients["P003"]["temperature"])
# 4
patients["P004"] = {
    "nom": "Ali",
    "age": 22,
    "temperature": 37.0
}
# 5
patients["P001"]["age"] = 26
# 6
s = 0

for x in patients:
    s = s + patients[x]["temperature"]
print(s / len(patients))
# 7
for x in patients:
    if patients[x]["temperature"] > 37.0:
        print(patients[x]["nom"])
# 8
print(len(patients))