import sys
import os
import unittest
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation2 import FFT

class TestFFT(unittest.TestCase):
    def setUp(self):
        self.fft = FFT()

    def test_fft_length(self):
        """Test si la longueur du résultat est égale à celle de l'entrée"""
        signal = [1, 2, 3, 4]
        result = self.fft.fft(signal)
        self.assertEqual(len(result), len(signal))

    def test_simple_signal(self):
        """Test avec un signal simple"""
        signal = [1, 0, 0, 0]
        result = self.fft.fft(signal)
        expected = [1, 1, 1, 1]
        self.assertTrue(np.allclose(result, expected))

    def test_linearity(self):
        """Test de la propriété de linéarité"""
        signal1 = [1, 2, 3, 4]
        signal2 = [5, 6, 7, 8]
        result1 = self.fft.fft(signal1)
        result2 = self.fft.fft(signal2)
        result_sum = self.fft.fft([a + b for a, b in zip(signal1, signal2)])
        self.assertTrue(np.allclose(result_sum, [a + b for a, b in zip(result1, result2)]))

    def test_compare_numpy(self):
        """Comparaison avec numpy.fft"""
        signal = [1, 2, 3, 4, 5, 6, 7, 8]
        result = self.fft.fft(signal)
        np_result = np.fft.fft(signal)
        self.assertTrue(np.allclose(result, np_result))

    def test_sine_wave(self):
        """Test avec une onde sinusoïdale"""
        t = np.linspace(0, 1, 128, endpoint=False)
        signal = np.sin(2 * np.pi * 10 * t)  # 10 Hz sine wave
        result = self.fft.fft(signal)
        freq = np.fft.fftfreq(len(t), t[1] - t[0])
        peak_freq = abs(freq[np.argmax(np.abs(result))])
        self.assertAlmostEqual(peak_freq, 10, delta=1)

    def test_power_of_two(self):
        """Test avec des longueurs qui sont des puissances de 2"""
        for n in [2, 4, 8, 16, 32, 64]:
            signal = [np.random.random() for _ in range(n)]
            result = self.fft.fft(signal)
            self.assertEqual(len(result), n)

if __name__ == '__main__':
    unittest.main()