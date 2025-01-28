import numpy as np
from scipy import linalg

v = np.array([1, 2, 3])
uv = v / linalg.norm(v)
print(uv)