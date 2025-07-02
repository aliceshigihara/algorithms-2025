l = []
m = ""
x = 0

file = open("textooo.txt", "r")

for p in file:
    l.append(p)

for p in l:
    t = 0
    for e in p:
        t += 1
        if t > len(m):
            m = p
            x = t
print(m)