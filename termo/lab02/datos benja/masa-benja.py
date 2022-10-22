"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>"""

#import módulos
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

#datos
"""datos para una masa de 100 g """
t1 = np.genfromtxt("masa-alcohol-100.txt", usecols= 0)
temp1 = np.genfromtxt("masa-alcohol-100.txt", usecols= 1)

"""datos para una masa de 150 g """
t2= np.genfromtxt("masa-alcohol-150.txt", usecols= 0)
temp2 = np.genfromtxt("masa-alcohol-150.txt", usecols= 1)

"""datos para una masa de 200 g """
t3 = np.genfromtxt("masa-alcohol-200.txt", usecols= 0)
temp3 = np.genfromtxt("masa-alcohol-200.txt", usecols= 1)

#grafico
plt.plot(t1, temp1, label = "100 g")
plt.plot(t2, temp2, label = "150 g")
plt.plot(t3, temp3, label = "200 g")
plt.ylabel("Temperatura [ °C]")
plt.xlabel("Tiempo $[s]$")
plt.title("Alcohol en diferentes cantidades")
plt.legend()
plt.savefig("grafico-alcohol-masa.pdf")