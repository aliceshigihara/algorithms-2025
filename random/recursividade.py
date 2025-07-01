v = [3,6,9,10,14,18,20,26,29,30]
t = int(input("defina um valor a ser procurado: "))
i = 0
f = 10

def FuncRecursiva(t,v,i,f):

    if i > f:
        return -1
    
    l = ( i + f ) // 2
    
    if t == v[l]:
        return l
    elif t < v[l]:
            return FuncRecursiva(t,v,i,l + 1)
    else:
            return FuncRecursiva(t,v,l - 1,f)

resultado = FuncRecursiva(t,v,i,f)

if resultado != -1:
    print("resultado:",resultado)

else:
    print("nao encontrado")