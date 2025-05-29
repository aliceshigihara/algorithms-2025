#peça uma string (a)
a = input("Dê uma string: ") #a = input()
#percorre "a" de trás pra frente (i)
for i in range(len(a)-1, -1, -1):       
    print(a[i], end="") #imprime a[i]
