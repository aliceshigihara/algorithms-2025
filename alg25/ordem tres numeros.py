# peça os três números
a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
c=int(input("Digite mais um número: "))

# se A for menor que B e menor que C, então a ordem será A,B,C
if a < b < c:
    print("A sua ordem de números é:", a,b.c)
# senão:
else:
#senão a ordem será B,A,C
    if b < a < c:
#então imprime:
        print("A sua ordem de números é:", b,a,c)
#senão a ordem será C,A,B
    if c < a < b:
        print("A sua ordem de números é:", c,a,b)
#senão a ordem será C,B,A
    if c < b < a:
        print("A sua ordem de números é:", c,b,a)
#senão a ordem será B,C,A
    if b < c < a:
        print("A sua ordem de números é:", b,c,a)
#senão a ordem será A,C,B
    if a < c < b:
        print("A sua ordem de números é:", a,c,b)