import numpy as np
import matplotlib.pyplot as plt

class FFT:
    def __init__(self):
        pass

    def bit_reverse(self, n, bits):
        return int('{:0{width}b}'.format(n, width=bits)[::-1], 2)

    def fft(self, x):
        n = len(x)
        bits = int(np.log2(n))
        
        if n != 1 << bits:
            raise ValueError("La taille de l'entrée doit être une puissance de 2")

        # Réorganisation des éléments
        for i in range(n):
            j = self.bit_reverse(i, bits)
            if i < j:
                x[i], x[j] = x[j], x[i]

        # Calcul de la FFT
        for step in range(1, bits + 1):
            m = 1 << step
            omega_m = np.exp(-2j * np.pi / m)
            for k in range(0, n, m):
                omega = 1
                for j in range(m // 2):
                    t = omega * x[k + j + m // 2]
                    u = x[k + j]
                    x[k + j] = u + t
                    x[k + j + m // 2] = u - t
                    omega *= omega_m

        return x