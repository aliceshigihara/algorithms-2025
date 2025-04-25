p1 = input().split(" ")

p1[0] = int(p1[0])
p1[1] = int(p1[0])
p1[2] = float(p1[0])

p2 = input().split(" ")

p2[0] = int(p2[0])
p2[1] = int(p2[0])
p2[2] = float(p2[0])

valor1 = p1[1] * p1[2]
valor2 = p2[1] * p2[2]

v = valor1 + valor2

print(f'VALOR A PAGAR: R$ {v:.2f}')
