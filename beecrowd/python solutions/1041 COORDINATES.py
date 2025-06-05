X,Y = [float(x) for x in input().split()]

if X > 0.0:
    if Y > 0.0:
        print("Q1")
    elif Y <0.0:
        print("Q4")
    else:
        print("Eixo X")

elif X < 0.0:
    if Y > 0.0:
        print("Q2")
    elif Y < 0.0:
        print("Q3")
    else:
        print("Eixo X")

else:
    if Y > 0.0:
        print("Eixo Y")
    elif Y < 0.0:
        print("Eixo Y")
    else:
        print("Origem")
