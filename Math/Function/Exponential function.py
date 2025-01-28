import numpy as np
import matplotlib.pyplot as plt

def exponential(x):
    return np.exp(x)

x = np.arange(-5, 5, 0.1)
y = exponential(x)

plt.plot(x, y, color = "k", linewidth = "2")
plt.xlim(-5, 5)
plt.ylim(0, 140)
plt.grid()
plt.show()