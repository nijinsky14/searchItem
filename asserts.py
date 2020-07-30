import unittest

class Pruebas_de_standards(unittest.TestCase):
    
    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 5 + 1
        b = 8 + 20
        self.assertNotEqual(a,b)

    def test_algo_es_verdadero(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a==b, "a y b deberian ser iguales")
    
    def test_algo_es_falso(self):
        self.assertFalse(2+1 == 4, "Esto debería ser falso")

    def test_algo_es_mayor(self):
        a = 5
        b = 3
        self.assertTrue(a>b)   

    def test_algo_es_mayor_II(self):    
        a = 5
        b = 3
        self.assertGreater(a, b)

    def test_algo_es_mayor_o_igual(self):
        a = 5
        b = 5
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 5
        b = 8
        self.assertLess(a, b)    
    
    def test_algo_es_menor(self):
        a = 5
        b = 8
        self.assertLessEqual(a, b)        

    def test_comparar_listas(self):
        a=[1,2,"fruta"]
        b=[1,2,"fruta"]
        self.assertListEqual(a,b)

    def test_comparar_tuplas(self):
        a = (1,2,3,4)
        b = (1,2,3)
        self.assertTupleEqual(a, b)
    
    def test_comparar_diccionarios(self):
        a = {"id":1,"Nombre":"pepe","Apellido":"Suarez"}
        b = {"id":1,"Nombre":"pepe","Apellido":"Suarez"}

if __name__ == '__main__':
    unittest.main() 