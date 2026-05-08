import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    # SUMA
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    # RESTA
    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)

    # MULTIPLICACIÓN
    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 5), 10)

    # DIVISIÓN
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    # DIVISIÓN POR CERO
    def test_dividir_por_cero(self):
        self.assertEqual(
            dividir(5, 0),
            "Error: no se puede dividir por cero"
        )

if __name__ == '__main__':
    unittest.main()