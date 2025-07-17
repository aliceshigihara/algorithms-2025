v = [2,4,3,7,8,9]

for n in range(len(v)-1):
    if v[n] < v[n+1]:
        print("ordem crescente")
        
    elif v[n] > v[n+1]:
        print("ordem decrescente")
    else:
        print("nao está em crescente, decrescente e muito menos ordenado.")