import unittest



#Bloque base
def sumar(x, y):
    resultado = x+y
    return resultado

def restar(x, y):
    resultado = x-y
    return resultado

def multiplicar(x, y):
    resultado = x*y
    return resultado

def dividir(x, y):
    resultado = x/y
    return resultado

def elevar(x, y):
    resultado = x**y
    return resultado



#Bloque pytest
def test_sumar():
    x= 8
    y= 2
    resultado = 10
    assert resultado == sumar(x, y)
    
def test_restar():
    x= 8
    y= 2
    resultado = 6
    assert resultado == restar(x, y)
    
def test_multiplicar():
    x= 8
    y= 2
    resultado = 16
    assert resultado == multiplicar(x, y)
    
def test_dividir():
    x= 8
    y= 2
    resultado = 4
    assert resultado == dividir(x, y)
    
def test_elevar():
    x= 8
    y= 2
    resultado = 64
    assert resultado == elevar(x, y)
    
    

#Bloque unittest
class Pruebas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2,1),3)

    def test_restar(self):
        self.assertEqual(restar(2,1),1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2,1),2)

    def test_dividir(self):
        self.assertEqual(dividir(2,1),2)

    def test_elevar(self):
        self.assertEqual(elevar(2,1),2)