matrizA = [
    [1,5,6],
    [2,7,4],
    [8,2,3]

]

matrizB = [
    [3,2,3],
    [4,1,1],
    [2,6,1]
    
]

linhasA = len(matrizA)
colunasA = len(matrizA[0])
colunasB = len(matrizB[0])

matrizC = []

for i in range(linhasA):
    linha = []
    for colunas in range(colunasB):
        linha.append(0)
    matrizC.append(linha)

for linhas in range(linhasA):
    for colunas in range(colunasB):
        for colunas2 in range(colunasA):
         matrizC[linhas][colunas] += matrizA[linhas][colunas2] * matrizB[colunas2][colunas]
         
for linha in matrizC:
    print(linha)