import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5, 5, 0.1)
y = sigmoid(x)

plt.plot(x, y, color = "k", linewidth = "2")
plt.xlim(-5, 5)
plt.ylim(0, 1)
plt.grid()
plt.show()