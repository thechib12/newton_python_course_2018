import numpy as np

a = np.loadtxt("tempdata.txt", skiprows=1, delimiter=", ")

print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

print(np.min(a, axis=0))

print(np.std(a, axis=0))