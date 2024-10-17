import numpy as np

class FFT:
    """
    Classe pour l'utilisation de la transformée de Fourier rapide.
    """
    def __init__(self):
        pass

    def fft(self, x):
        x = np.asarray(x, dtype=complex)
        n = len(x)
        
        if n <= 1:
            return x
        
        # Si n n'est pas une puissance de 2, on complète avec des zéros pour garantir la performance 
        if n & (n-1) != 0:
            next_power_of_2 = 2**np.ceil(np.log2(n))
            x = np.pad(x, (0, int(next_power_of_2 - n)), 'constant')
            n = len(x)
        
        # Division en deux parties une pair et une autre impair
        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])
        
        # Calcul facteurs de rotation puis réunifucation des deux parties
        T = np.exp(-2j * np.pi * np.arange(n) / n)[:n//2] * odd
        return np.concatenate([even + T, even - T])
