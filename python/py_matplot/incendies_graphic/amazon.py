
import matplotlib.pyplot as plt
from libslinha import *


file = open("amazonutf.csv", "r")

anosincendio = []
numerosincendio = []

if file:
    for linha in file:
        y = getpart(linha,",",3)
        converte = y.replace(".","")
        numeros = int(converte)

        ano = int(getpart(linha,",",0))
        if ano in anosincendio:
            i = anosincendio.index(ano)
            numerosincendio[i] +=  numeros
        else:
            anosincendio.append(ano)
            numerosincendio.append(numeros)

print(anosincendio)
print(numerosincendio)

plt.plot(anosincendio,numerosincendio)

plt.ylabel("Forest Fires")

plt.xlabel("Year")

plt.title("Forest fires in Brazil",
          fontdict = {'fontsize': 16,'fontweight': 'bold', 'color': 'darkblue'},
          loc = 'center',
          pad = 20)

plt.show()

file.close()

