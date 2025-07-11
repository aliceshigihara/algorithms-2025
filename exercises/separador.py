c = 1

x = str(input("digite uma string: "))
s = str(input("qual será o separador?: "))

for i in x:
    if i == s:
        c += 1
print(c,"partes")