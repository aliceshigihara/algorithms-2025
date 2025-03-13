a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
c=int(input("Digite mais um número: "))

if a < b < c:
    print("A sua ordem de números é:", a,b.c)
else:
    if b < a < c:
        print("A sua ordem de números é:", b,a,c)
    if c < a < b:
        print("A sua ordem de números é:", c,a,b)
    if c < b < a:
        print("A sua ordem de números é:", c,b,a)
    if b < c < a:
        print("A sua ordem de números é:", b,c,a)
    if a < c < b:
        print("A sua ordem de números é:", a,c,b)