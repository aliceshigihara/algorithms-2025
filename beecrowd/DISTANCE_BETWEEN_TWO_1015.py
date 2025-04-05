import math

VALORES = input().split()
VALORES1 = input().split()

X1,Y1 = list(map(float,VALORES))
X2,Y2 = list(map(float,VALORES1))

DISTANCIA = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

print(f"{DISTANCIA:.4f}")
