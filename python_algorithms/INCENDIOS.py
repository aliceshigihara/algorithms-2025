from mysplit import *

file = open("/home/ifc/Downloads/prog25-main/algorithms/amazon.csv", "r")
if file:
    incendios = 0
    
    for linha in file:
        ano = get_part(linha,",",1)
        estado = get_part(linha,",",2)
        numeros = get_part(linha,",",4)
        
        if estado == '"Santa Catarina"' and ano == "2010":
            incendios += int(numeros)
    
file.close()

print(incendios)
