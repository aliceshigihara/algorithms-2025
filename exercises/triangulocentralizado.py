altura = int(input("qual será o tamanho do triangulo?: "))

c = 1

for i in range(1,altura):
    e = altura - i
    r = "*" * c
    c += 2
    print(" " * e,r," " * e)
    