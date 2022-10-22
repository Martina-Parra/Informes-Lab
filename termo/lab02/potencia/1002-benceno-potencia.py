"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>"""

#import módulos
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

#datos
"""datos para 250 W  """
t1 = np.genfromtxt("datos-benceno-250W.txt", usecols= 0)
temp1 = np.genfromtxt("datos-benceno-250W.txt", usecols= 1)

"""datos para 500 W  """
t2= np.genfromtxt("datos-benceno-500W.txt", usecols= 0)
temp2 = np.genfromtxt("datos-benceno-500W.txt", usecols= 1)

"""datos para 1000 W """
t3 = np.genfromtxt("datos-benceno-1000W.txt", usecols= 0)
temp3 = np.genfromtxt("datos-benceno-1000W.txt", usecols= 1)

#grafico
plt.plot(t1, temp1, label = "250 W")
plt.plot(t2, temp2, label = "500 W")
plt.plot(t3, temp3, label = "1000 W")
plt.ylabel("Temperatura [ °C]")
plt.xlabel("Tiempo $[s]$")
plt.title("Benceno en diferentes potencias")
plt.legend()

plt.savefig("grafico-benceno-potencia.pdf")