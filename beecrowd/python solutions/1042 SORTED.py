VALORES = input().split()
VALORES = list(map(int,VALORES))

V1,V2,V3 = sorted(VALORES)[::+1]
V4,V5,V6 = (VALORES)

print(V1, end='\n')
print(V2, end='\n')
print(V3, end='\n\n')
print(V4, end='\n')
print(V5, end='\n')
print(V6)
