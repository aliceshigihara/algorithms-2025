C= float(input())
B= float(input())
A= float(input())

if (B+C) <= A:
    print("NAO FORMA TRIANGULO")

if A*A == (B*B + C*C):
    print("TRIANGULO RETANGULO")

if A*A > (B*B + C*C):
    print("TRIANGULO OBTUSANGULO")

if A*A < (B*B + C*C):
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")

if A == B < C:
    print("TRIANGULO ISOCELES")

if A == C < B:
    print("TRIANGULO ISOCELES")

if C == B < A:
    print("TRIANGULO ISOCELES")