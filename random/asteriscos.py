n = []

v = int(input("digite um numero: "))

for x in range(v):
    x = int(input("digite um numero: "))
    n.append(x)

for i in range(len(n)):
    print("*" * n[i])