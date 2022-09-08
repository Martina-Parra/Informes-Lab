import matplotlib.pyplot as plt 
import numpy as np 
 

# a temperatura constante 
#partículas pesadas######################################################################################################################################################

# n =50
x = np.array([5,7,9,11,13,15])
y = np.array([11.7,8.3,6.5,5.3,4.6,3.8])
z = np.array([23.3,16.8,13.1,10.6,8.9,7.7])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,25)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas pesadas n = 50")
plt.legend()
plt.show()

# n = 100
x = np.array([5,7,9,11,13,15])
y = np.array([23.3,16.7,13.2,10.6,9.0,7.7])
z = np.array([46.6,33.5,26.0,21.1,17.9,15.6])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,49)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas pesadas n = 100")
plt.legend()
plt.show()

# n = 150
x = np.array([5,7,9,11,13,15])
y = np.array([35.1,24.9,19.5,15.9,13.4,11.7])
z = np.array([70.0,50.1,39.0,31.7,26.9,23.4])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,73)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas pesadas n = 150")
plt.legend()
plt.show()
plt.savefig("figura3.pdf")


#partículas ligeras #################################################################################################################################################### 

# n = 50
x = np.array([5,7,9,11,13,15])
y = np.array([11.7,8.1,6.5,5.1,4.5,3.8])
z = np.array([23.3,16.8,13.0,10.6,9.0,7.8])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,25)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas ligeras n = 50")
plt.legend()
plt.show()
plt.savefig("figura4.pdf")


# n = 100
x = np.array([5,7,9,11,13,15])
y = np.array([23.2,16.8,12.8,10.7,8.9,7.8])
z = np.array([46.6,33.4,25.9,21.3,17.9,15.5])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,49)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas ligeras n = 100")
plt.legend()
plt.show()
plt.savefig("figura5.pdf")


# n =150
x = np.array([5,7,9,11,13,15])
y = np.array([35.0,25.3,19.4,15.9,13.3,11.8])
z = np.array([70.1,50.2,38.8,31.8,26.9,23.4])

plt.plot(x,y, label="T = 300K")
plt.xlim(0,16)
plt.ylim(0,73)
plt.plot(x,z, label="T = 600K")
plt.xlabel("Volumen [nm]")
plt.ylabel("Presión [atm]")
plt.title("Partículas ligeras n = 150")
plt.legend()
plt.show()
plt.savefig("figura6.pdf")

# a presion constante ###################################################################################################################################################

# n = 50
x = np.array([150,225,375,450])
y = np.array([5.0,7.5,12.5,15])

plt.plot(x,y, label="P = 5.8 atm")
plt.xlim(0,600)
plt.ylim(0,17)
plt.xlabel("Temperatura [K]")
plt.ylabel("Volumen [nm]")
plt.title("Partículas pesadas n = 50")
plt.legend()
plt.show()
plt.savefig("figura7.pdf")

# n = 100
x = np.array([150,225,375,450])
y = np.array([5.0,7.5,12.5,15])

plt.plot(x,y, label="P = 17.5 atm")
plt.xlim(0,600)
plt.ylim(0,17)
plt.xlabel("Temperatura [K]")
plt.ylabel("Volumen [nm]")
plt.title("Partículas pesadas n = 100")
plt.legend()
plt.show()
plt.savefig("figura8.pdf")


# n = 150
x = np.array([150,225,375,450])
y = np.array([5.0,7.5,12.5,15])

plt.plot(x,y, label="P = 29.2 atm")
plt.xlim(0,600)
plt.ylim(0,17)
plt.xlabel("Temperatura [K]")
plt.ylabel("Volumen [nm]")
plt.title("Partículas pesadas n = 150")
plt.legend()
plt.show()
plt.savefig("figura9.pdf")














