import sys
import unittest
import numpy as np
from numpy.testing import assert_array_almost_equal
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import tfd

class TestTFD(unittest.TestCase):

    def test_tfd_simple_signal(self):
        signal = [1, 2, 1, -1]
        expected = np.fft.fft(signal)  # Utilisation de la FFT de NumPy comme référence
        result = tfd(signal)
        assert_array_almost_equal(result, expected)

    def test_tfd_zero_signal(self):
        signal = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        result = tfd(signal)
        assert_array_almost_equal(result, expected)

    def test_tfd_constant_signal(self):
        signal = [1, 1, 1, 1]
        expected = [4, 0, 0, 0]
        result = tfd(signal)
        assert_array_almost_equal(result, expected)

    def test_tfd_length(self):
        signal = [1, 2, 3, 4, 5]
        result = tfd(signal)
        self.assertEqual(len(result), len(signal))

if __name__ == '__main__':
    unittest.main()