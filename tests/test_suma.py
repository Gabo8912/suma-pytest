# archivo: test_suma.py
from suma import sumar

def test_sumar_correcto():
    assert sumar(2, 3) == 5

def test_sumar_falla():
    assert sumar(2, 2) == 5  # Esto fallará a propósito
