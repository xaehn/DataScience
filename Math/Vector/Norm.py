import numpy as np
from scipy.spatial import distance

x = (1, 2, 3)
y = (4, 5, 6)
mangattan_distance = sum(abs(a - b) for a, b in zip(x, y))
print(f"mangattan_distance : {mangattan_distance}")
euclidean_distance = distance.euclidean(x, y)
print(f"euclidean_distance : {euclidean_distance}", end = "\n\n")

v = np.array([1, 2, 3])
default_norm = np.linalg.norm(v)
print(f"default_norm : {default_norm}")
l1_norm = np.linalg.norm(v, ord = 1)
print(f"l1_norm : {l1_norm}")
l2_norm = np.linalg.norm(v, ord = 2)
print(f"l2_norm : {l2_norm}")