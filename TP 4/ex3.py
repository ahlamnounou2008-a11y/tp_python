s = input("Entrer une chaîne : ")
r = ""
c = 1
for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        c = c + 1
    else:
        r = r + s[i] + str(c)
        c = 1
print(r)