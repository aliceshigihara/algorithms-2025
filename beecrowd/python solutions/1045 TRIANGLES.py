valores = input().split()
valores = list(map(float,valores))

A,B,C = sorted(valores)[::-1]

continua = True

if A >= B+C:
    print("NAO FORMA TRIANGULO")
    continua = False

if A**2 == (B**2 + C**2) and continua:
    print("TRIANGULO RETANGULO")

if A**2 > B**2 + C**2 and continua:
    print("TRIANGULO OBTUSANGULO")

if A*A < B*B + C*C and continua:
    print("TRIANGULO ACUTANGULO")

if A == B == C and continua:
    print("TRIANGULO EQUILATERO")

if A == B < C and continua:
    print("TRIANGULO ISOCELES")

if A == C < B and continua:
    print("TRIANGULO ISOCELES")

if C == B < A and continua:
    print("TRIANGULO ISOCELES")
