import numpy as np
import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import tfd
# Générer un signal d'exemple
# N = 64
# t = np.linspace(0, 1, N, endpoint=False)
# signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
signal = np.array([1, 2, 3, 4])
N = len(signal)

# Calculer la TFD
tfd = tfd(signal)

# Calculer le spectre d'amplitude
spectre = np.abs(tfd) * 2 / N

# Afficher le résultat
plt.figure(figsize=(10, 4))
plt.stem(np.arange(N), spectre)
plt.title("Spectre d'amplitude")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.show()