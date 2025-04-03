valores = (input()).split()

valores = list(map(float,valores))

A,B,C = sorted(valores)[::-1]

if(A < B + C and B < C + A and C < A + B):
    print(f"Perimetro = {(A + B + C):.1f}")
else:
    print(f"Area = {(((A + B)/2) * C):.1f}")