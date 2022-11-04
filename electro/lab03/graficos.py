import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

########################ampolleta de linterna#################################
# vial_plus_volt = np.genfromtxt("ampolleta-positivo.txt", usecols=0)
# vial_plus_I = np.genfromtxt("ampolleta-positivo.txt", usecols=1)
# vial_less_volt = np.genfromtxt("ampolleta-negativo.txt", usecols=0)
# vial_less_I = np.genfromtxt("ampolleta-negativo.txt", usecols=1)


# fig, ax1 = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
# ax1.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
# ax1.spines[["top", "right"]].set_visible(False)

# plt.grid(True)
# ax1.plot(0,1 ,"^k", transform= ax1.get_xaxis_transform(), clip_on=False)
# ax1.plot(1,0, ">k", transform= ax1.get_yaxis_transform(), clip_on=False)
# ax1.plot(vial_plus_volt, vial_plus_I, color = "green", label = "positive")
# ax1.plot(vial_less_volt, vial_less_I, color="black", label ="negative")
# ax1.set_ylabel('Corriente [A]', loc='top')
# ax1.set_xlabel("Voltaje [v]", loc='right')
# plt.title("Ampolleta de linterna")
# plt.legend()
# plt.savefig("img/ampolleta.pdf")
# plt.show()




##################################### conductor metalico ################################################################
# delta_plus_volt = np.genfromtxt("rectangular-positivo.txt", usecols=0)
# delta_plus_I = np.genfromtxt("rectangular-positivo.txt", usecols=1)
# delta_less_volt = np.genfromtxt("rectangular-negativo.txt", usecols=0)
# delta_less_I = np.genfromtxt("rectangular-negativo.txt", usecols=1)

# fig, ax = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
# ax.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
# ax.spines[["top", "right"]].set_visible(False)

# plt.grid(True)
# ax.plot(0,1 ,"^k", transform= ax.get_xaxis_transform(), clip_on=False)
# ax.plot(0,-1 ,"vk", transform= ax.get_xaxis_transform(), clip_on=False)

# ax.plot(1,0, ">k", transform= ax.get_yaxis_transform(),clip_on=False)
# ax.plot(-1,0,"<k", transform= ax.get_yaxis_transform(), clip_on=False)

# plt.title("Conductor metálico")


# Some sample data.

# ax.plot(delta_plus_volt, delta_plus_I, label="positive")
# ax.plot(delta_less_volt, delta_less_I, label="negative")
# ax.set_ylabel('Corriente [A]', loc='top')
# ax.set_xlabel("Voltaje [v]", loc='right')

# plt.legend()

# plt.savefig("img/rectangulo.pdf")
# plt.show()



#################diodo######################
# diodo_less_volt = np.genfromtxt("diodo-negativo.txt", usecols=0)
# diodo_less_I = np.genfromtxt("diodo-negativo.txt", usecols=1)
# diodo_plus_volt = np.genfromtxt("diodo-positivo.txt", usecols=0)
# diodo_plus_I = np.genfromtxt("diodo-positivo.txt", usecols=1)




# fig, ax3 = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
# ax3.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
# ax3.spines[["top", "right"]].set_visible(False)

# plt.grid(True)
# ax3.plot(0,1.5 ,"^k", transform= ax3.get_xaxis_transform(), clip_on=False)
# ax3.plot(0,-1.5 ,"vk", transform= ax3.get_xaxis_transform(), clip_on=False)

# ax3.plot(1.5,0, ">k", transform= ax3.get_yaxis_transform(),clip_on=False)
# ax3.plot(-1.5,0,"<k", transform= ax3.get_yaxis_transform(), clip_on=False)

# plt.title("Diodo semiconductor común")


# Some sample data.

# ax3.plot(diodo_plus_volt, diodo_plus_I, label="positive")
# ax3.plot(diodo_less_volt, diodo_less_I, label="negative")
# ax3.set_ylabel('Corriente [A]', loc='top')
# ax3.set_xlabel("Voltaje [v]", loc='right')

# plt.legend()
# plt.show()



############# Emisor de luz ########################
emisor_luz = np.genfromtxt("emisor-luz.txt")
luz_plus_volt = emisor_luz[:,0]
luz_plus_I = emisor_luz[:,1]
luz_less_volt = emisor_luz[:,2]
luz_less_I = emisor_luz[:,3]

fig, ax4 = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax4.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
ax4.spines[["top", "right"]].set_visible(False)

plt.grid(True)
ax4.plot(0,1 ,"^k", transform= ax4.get_xaxis_transform(), clip_on=False)
ax4.plot(0,-1 ,"vk", transform= ax4.get_xaxis_transform(), clip_on=False)

ax4.plot(1,0, ">k", transform= ax4.get_yaxis_transform(),clip_on=False)
ax4.plot(-1,0,"<k", transform= ax4.get_yaxis_transform(), clip_on=False)

plt.title("Diodo emisor de luz")

# Some sample data.

ax4.plot(luz_plus_volt, luz_plus_I, label="positive")
ax4.plot(luz_less_volt, luz_less_I, label="negative")
ax4.set_ylabel('Corriente [A]', loc='top')
ax4.set_xlabel("Voltaje [v]", loc='right')

plt.legend()
plt.show()