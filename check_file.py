from scipy.sparse import coo_matrix, linalg, hstack, vstack
import numpy as np
from scipy.sparse.linalg import spsolve
A = np.eye(5)*5
A_coo = coo_matrix(A)
print(hstack([A_coo, A]))

B = np.ones((5,1))
B_coo = coo_matrix(B)

P = np.linalg.solve(A,B)
print(P)

Ainv_coo = linalg.inv(A_coo)
P_coo = Ainv_coo.multiply(B)
print(P_coo)

A_csr = A_coo.tocsr()
B_csr = B_coo.tocsr()
P_csr = spsolve(A_csr, B)
print(P_csr)

all_cols = np.arange(A_csr.shape[1])
print(all_cols)
cols_to_keep = np.where(np.logical_not(np.in1d(all_cols, [1])))[0]
m = A_csr[:, cols_to_keep]
M = m[cols_to_keep, :]
b = np.delete(B, 1)
print(M.toarray())
P = spsolve(M, b)
print(P)

import numpy as np
import matplotlib.pyplot as plt

phi = np.random.randn(20, 20) # initial value for phi
F = 1
dt = 1
it = 100

for i in range(it):
    dphi = np.gradient(phi)
    dphi2 = [i**2 for i in dphi]
    print(type(dphi))
    dphi_norm = np.sqrt(np.sum(dphi2, axis=0))

    phi = phi + dt * F * dphi_norm

    # plot the zero level curve of phi
    plt.contour(phi, 0)
    plt.show()