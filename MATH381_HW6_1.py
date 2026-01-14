# Gambler's ruin

import numpy as np

# P is the transition probability matrix, q is the initial
# distribution. Please note the double bracketing in the
# definition of P.
P = np.array([[1, 0, 0, 0, 0],[0.5, 0, 0.5, 0, 0], [0, 0.5, 0, 0.5, 0],[0, 0, 0.5, 0, 0.5], [0, 0, 0, 0, 1]])
q = np.array([0, 0, 1, 0, 0])


# Compute P^1000
k = 1000
M = np.linalg.matrix_power(P, k)

print(M)

