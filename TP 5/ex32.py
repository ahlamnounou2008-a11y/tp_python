ID = ["EQ001", "EQ002", "EQ003", "EQ002",
      "EQ004", "EQ001", "EQ005", "EQ003"]
# 1
ens = set(ID)
# 2
print(ens)
# 3
print(len(ens))
# 4
print(len(ID))
print(len(ens))
# 5
for x in ens:
    if ID.count(x) > 1:
        print(x)