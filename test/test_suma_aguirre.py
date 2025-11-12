from funciones.funcion_suma_aguirre import suma

def test_suma_aguirre():
    assert suma(3, 5) == 8
    assert suma(-2, 2) == 0
    assert suma(0, 0) == 0
