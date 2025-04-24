#define os intervalos (a),(b),(c) e (d)
a = 0
b = 0
c = 0
d = 0
#repete 20 vezes
for i in range(0,20):
    #pede um número (x)
    x = int(input("Digite um número: "))
    if x < 0:
        break
    #verifica se "x" for menor que 0, se for, então para aí

    #verifica se "x" estiver entre 0-25, se sim, soma 1 no contador deste intervalo
    if x >= 0 and x <= 25:
        a += 1
    #verifica se "x" estiver entre 26-50, se sim, soma 1 no contador deste intervalo
    if x >= 26 and x <= 50:
        b += 1
    #verifica se "x" estiver entre 51-75, se sim, soma 1 no contador deste intervalo
    if x >= 51 and x <= 75:
        c += 1
    #verifica se "x" estiver entre 76-100, se sim, soma 1 no contador deste intervalo
    if x >= 76 and x <= 100:
        d += 1

#imprime os contadores de cada intervalo (a),(b),(c) e (d)
print(a,b,c,d)
