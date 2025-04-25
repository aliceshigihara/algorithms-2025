#cria uma variável (soma)
soma = 0
#quantidade de números para calcular ( de 1 a 4 )
for i in range(1, 5):
    #pede um número (numero) de acordo com a quantidade de pedidos
    numero = int(input(f"Digite o {i}º número: "))
    #faça a soma do (numero) multiplicado pela quantidade de números (i) respectivamente
    soma += numero * (i + 1)
#mostra a soma
print(soma)
