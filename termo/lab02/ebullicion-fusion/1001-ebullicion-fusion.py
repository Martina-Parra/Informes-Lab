"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>"""

#import módulos
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")


#Datos
tiempo = np.genfromtxt("Datos-agua.txt", usecols= 0)
temperatura = np.genfromtxt("Datos-agua.txt", usecols= 1)

#Grafico 1
"""Grafico termperatura vs tiempo, para una masa = 150[g] de agua, 
potencia = 250[W] y T°_inicial = -10 °C"""

plt.plot(tiempo, temperatura, label = "agua")
plt.ylabel("Temperatura [°C]")
plt.xlabel("Tiempo $[s]$")
plt.title("Termperatura vs Tiempo")
plt.legend()

#Grafico 2
"""Grafico termperatura vs tiempo, para una masa = 150[g] de benceno, 
potencia = 250[W] y T°_inicial = -10 °C"""

#Datos 2
tiempo2 = np.genfromtxt("Datos-benceno.txt", usecols= 0)
temperatura2 = np.genfromtxt("Datos-benceno.txt", usecols= 1)

plt.plot(tiempo2, temperatura2, label = "benceno")
plt.legend()



#Grafico 3
"""Grafico termperatura vs tiempo, para una masa = 150[g] de alcohol, 
potencia = 250[W] y T°_inicial = -10 °C"""

#Datos 3
tiempo3 = np.genfromtxt("Datos-alcohol.txt", usecols= 0)
temperatura3 = np.genfromtxt("Datos-alcohol.txt", usecols= 1)

plt.plot(tiempo3, temperatura3, label = "alcohol")
plt.legend()

plt.savefig("grafico-ebullicion-fusion.pdf")

