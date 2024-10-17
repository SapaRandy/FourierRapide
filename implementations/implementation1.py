import numpy as np

def tfd(u):
    N = len(u)
    F = np.zeros(N, dtype=np.complex64)
    for n in range(N):
        for k in range(N):
            F[n] += u[k] * np.exp(-2j * np.pi * n * k / N)
    return F
