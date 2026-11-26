service_A = {"P001", "P002", "P003", "P004", "P005"}
service_B = {"P003", "P004", "P006", "P007"}
# 1
print(service_A)
# 2 
print(service_B)
# 3
print(service_A.intersection(service_B))
# 4
print(service_A.difference(service_B))
# 5
print(service_B.difference(service_A))
# 6
tous = service_A.union(service_B)
print(tous)
# 7
print(len(tous))