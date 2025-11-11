from funciones.suma_aguirre import suma_aguirre

def test_suma_aguirre():
    assert suma_aguirre(3, 5) == 8
    assert suma_aguirre(-2, 2) == 0
    assert suma_aguirre(0, 0) == 0
