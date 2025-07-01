#procedural

v = [2,6,8,9,10,22,45,47,50,66]

x = 0 #inicio
y = 9 #fim
t = int(input("qual é o valor a ser procurado?:"))

while x <= y:
    l = ( x + y ) // 2
    if t == v[int(l)]:
        print("resultado:",int(l))
        break
    else:
        if t < v[int(l)]:
            y = l-1
        else:
            x = l + 1
    
else:
    print("valor nao encontrado:")