phrase = input("Donner une phrase : ")
# 1
print(phrase.upper())
# 2
print(phrase.lower())
# 3
print(len(phrase))
# 4
mots = phrase.split()
print(len(mots))
# 5
c = 0
for x in phrase:
    if x in "aeiouyAEIOUY":
        c = c + 1
print(c)
# 6
for x in mots:
    print(x)
# 7
plus_long = mots[0]

for x in mots:
    if len(x) > len(plus_long):
        plus_long = x
print(plus_long)