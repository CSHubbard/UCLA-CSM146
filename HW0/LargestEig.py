import numpy as np
import scipy.linalg as lg
A = np.mat("1 0; 1 3")

evals, evecs = lg.eig(A)
print("eigenvalues: ",evals, '/n')
print("eigenvectors: ",evecs)