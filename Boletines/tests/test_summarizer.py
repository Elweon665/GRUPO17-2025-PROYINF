import unittest
from Article_Summarizer.program.summarizer import generarResumen
import os

# Para correr las pruebas usar: python manage.py test > tests/resultados.txt

class Test_summarizer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        actual_path = os.path.dirname(__file__)  # Carpeta tests/
        input_path = os.path.join(actual_path, "entradas")
        input_path = os.path.join(input_path, "test_summarizer")
        
        cls.texto_corto = "El objetivo principal de este programa es el de generar resumenes con el fin de poder automatizar la creacion de boletines del proyecto."
        cls.texto_repetido = " ".join(["Este es un texto de prueba."] * 100)
        
        with open(os.path.join(input_path, "test2.txt"), "r", encoding="utf-8") as arch:
            cls.texto_largo = arch.read()
        with open(os.path.join(input_path, "test4.txt"), "r", encoding="utf-8") as arch:
            cls.texto_ingles = arch.read()
    
    @classmethod      
    def tearDownClass(cls):
        return
        
    
    #test1
    def test_resumen_texto_corto(self):
        resumen = generarResumen(self.texto_corto)
        self.assertIsInstance(resumen, str)
        self.assertTrue(len(resumen.split()) < len(self.texto_corto.split()))

    #test2
    def test_resumen_texto_largo(self):
        resumen = generarResumen(self.texto_largo)
        self.assertIsInstance(resumen, str)
        self.assertTrue(len(resumen.split()) < len(self.texto_largo.split()))

    #test3
    def test_resumen_texto_vacio(self):
        resumen = generarResumen("")
        self.assertEqual(resumen, "")
     
    #test4   
    def test_resumen_texto_ingles(self):
        resumen = generarResumen(self.texto_ingles)
        self.assertTrue(len(resumen.split()) < len(self.texto_ingles.split()))
    
    #test5
    def test_resumen_texto_repetido(self):
        resumen = generarResumen(self.texto_repetido)
        self.assertTrue(len(resumen.split()) <= len(self.texto_repetido.split()) / 100)
        
        
if __name__ == '__main__':
    unittest.main()