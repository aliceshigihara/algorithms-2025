A = int(input())
B = int(input())
C = int(input())
D = int(input())

if B > C and D > A and C+D > A+B and 0 <= C and D and A % 2 == 0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")