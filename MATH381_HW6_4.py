# Three balls divided into two containers

import numpy as np

# P is the transition probability matrix, q is the initial
# distribution. Please note the double bracketing in the
# definition of P.
P = np.array([[0.9409, 0.0291, 0.027, 0.003],[0.873, 0.027, 0.09, 0.01], [0.9409, 0.0291, 0.027, 0.003],
              [0.873, 0.027, 0.09, 0.01]])
q = np.array([0.25, 0.25, 0.25, 0.25])


# Compute q*P^1000, which gives the distribution of X_1000.
k = 1000
M = q @ np.linalg.matrix_power(P, k)

print(M)



# Calculates the eigenvalues of P and a left eigenvector
# for each eigenvalue.
# We need to transpose P to find the left eigenvectors.
u,v = np.linalg.eig(np.transpose(P))
v *= 1/sum(v) # See note at the end.

# Prints eigenvalues, then eigenvectors. The *columns* of v
# are the eigenvectors. To find the stationary distribution,
# look at the column under the eigenvalue 1.
print(u)
print(v)

# To get an eigenvector which is a probability distribution,
# you will need to multiply by 1/sum(v) so the sum of
# coordinates is 1.

