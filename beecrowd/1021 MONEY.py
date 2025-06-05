ValorMonetario = (float(input()))
format(ValorMonetario, '.2f')

v100 = ValorMonetario // 100
ValorMonetario %= 100

V50 = ValorMonetario // 50
ValorMonetario %= 50

V20 = ValorMonetario // 20
ValorMonetario %= 20

v10 = ValorMonetario // 10
ValorMonetario %= 10

V05 = ValorMonetario // 5
ValorMonetario %= 5

V02 = ValorMonetario // 2
ValorMonetario %= 2

m1 = ValorMonetario // 1
ValorMonetario %= 1

m50 = ValorMonetario // 0.50
ValorMonetario %= 0.50

m25 = ValorMonetario // 0.25
ValorMonetario %= 0.25

m10 = ValorMonetario // 0.10
ValorMonetario %= 0.10

m05 = ValorMonetario // 0.05
ValorMonetario %= 0.05

m01 = ValorMonetario // 0.01
ValorMonetario %= 0.01

print("NOTAS:")
print(f"{int(v100)} nota(s) de R$ 100.00")
print(f"{int(V50)} nota(s) de R$ 50.00")
print(f"{int(V20)} nota(s) de R$ 20.00")
print(f"{int(v10)} nota(s) de R$ 10.00")
print(f"{int(V05)} nota(s) de R$ 5.00")
print(f"{int(V02)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(m1)} moeda(s) de R$ 1.00")
print(f"{int(m50)} moeda(s) de R$ 0.50")
print(f"{int(m25)} moeda(s) de R$ 0.25")
print(f"{int(m10)} moeda(s) de R$ 0.10")
print(f"{int(m05)} moeda(s) de R$ 0.05")
print(f"{int(m01)} moeda(s) de R$ 0.01")
