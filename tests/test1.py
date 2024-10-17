import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import tfd

def test1():
    signal = [1, 2, 3, 4]
    resultat = tfd(signal)
    
    # Vérification de la longueur du résultat
    assert len(resultat) == len(signal)