import numpy as np
import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import tfd

def run_tfd_analysis():
    # Générer un signal d'exemple
    N = 1000  # Nombre de points
    fs = 1000  # Fréquence d'échantillonnage en Hz
    t = np.linspace(0, (N-1)/fs, N)  # Vecteur temps

    # Création du signal
    f1, f2 = 50, 120  # Fréquences des composantes du signal en Hz
    signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

    # Calcul de la TFD
    tfd_result = tfd(signal)

    # Calcul du spectre d'amplitude
    spectre = np.abs(tfd_result) / N  # Normalisation

    # Calcul des fréquences
    freqs = np.fft.fftfreq(N, 1/fs)

    # Création de la figure
    plt.figure(figsize=(12, 6))

    # Affichage du spectre d'amplitude
    plt.plot(freqs[:N//2], 2*spectre[:N//2])  # On ne montre que la partie positive du spectre
    plt.title("Spectre d'amplitude de la TFD")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude")

    # Mise en évidence de l'axe des fréquences
    plt.axhline(y=0, color='r', linestyle='-', linewidth=0.5)
    plt.text(freqs[N//4], -0.02, "Axe des fréquences", color='r', ha='center')

    # Identification des pics de fréquence
    threshold = 0.1  # Seuil pour considérer un pic
    peaks = np.where(spectre[:N//2] > threshold)[0]
    for peak in peaks:
        plt.annotate(f'{freqs[peak]:.1f} Hz', 
                     xy=(freqs[peak], 2*spectre[peak]), 
                     xytext=(5, 5), 
                     textcoords='offset points',
                     ha='left', 
                     va='bottom',
                     bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    plt.xlim(0, fs/2)  # Limite l'affichage à la fréquence de Nyquist
    plt.grid(True)
    plt.tight_layout()
    plt.show()