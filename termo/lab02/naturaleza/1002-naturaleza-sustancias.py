"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>
p = 250W, m= 150 g y T_inicial = 0°C """

#import módulos
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

#datos
"""datos para agua  """
t1 = np.genfromtxt("datos-agua-1.txt", usecols= 0)
temp1 = np.genfromtxt("datos-agua-1.txt", usecols= 1)

"""datos para alcohol  """
t2= np.genfromtxt("datos-alcohol-2.txt", usecols= 0)
temp2 = np.genfromtxt("datos-alcohol-2.txt", usecols= 1)

"""datos para benceno """
t3 = np.genfromtxt("datos-benceno-3.txt", usecols= 0)
temp3 = np.genfromtxt("datos-benceno-3.txt", usecols= 1)


#grafico
plt.plot(t1, temp1, label = "agua")
plt.plot(t2, temp2, label = "alcohol")
plt.plot(t3, temp3, label = "benceno")
plt.ylabel("Temperatura [ °C]")
plt.xlabel("Tiempo $[s]$")
plt.title(" Diferentes sustancias")
plt.legend()
plt.savefig("grafico-naturaleza-sustancias.pdf")