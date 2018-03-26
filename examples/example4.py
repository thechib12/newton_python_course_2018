import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("tempdata.txt", skiprows=1, delimiter=", ")


plt.plot(a[:, 0], a[:, 1])
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.savefig("plot4_1.png")
plt.clf()

plt.scatter(a[:, 1], a[:, 2])
plt.savefig("plot4_2.png")
plt.clf()

plt.hist(a[:, 1], bins=4, rwidth=0.9)
plt.savefig("plot4_3.png")
