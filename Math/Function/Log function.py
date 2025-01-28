import math
import numpy as np
import matplotlib.pyplot as plt

def log2(x):
    return np.log2(x)

def log10(x):
    return np.log10(x)

x = np.arange(0.1, 16, 0.1)
y1 = log2(x)
y2 = log10(x)

plt.plot(x, y1, color = "k", linewidth = "2")
plt.plot(x, y2, color = "k", linewidth = "2")
plt.xlim(0, 16)
plt.ylim(-4, 5)
plt.grid()
plt.show()