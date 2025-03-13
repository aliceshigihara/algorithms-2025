#peça o primeiro número que você quer
n1 = float(input("Digite um número: "))
#peça o segundo número que você deseja
n2 = float(input("Digite outro número: "))
#peça o terceiro número!
n3 = float(input("Digite mais um número: "))

#salve os números em uma variável
ordem = [n1,n2,n3]
#sorted para ordenar os números da variável
            #se n1 > n2 então n1,n2
            #se n1 < n2 então n2,n1
sorted(ordem)
#imprima o resultado da ordem
print("A ordem dos números escolhidos é:",sorted(ordem))