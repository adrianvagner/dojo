import unittest
from  transforma_romano  import  romano
from  transforma_indo  import  indoara

class TestRomano(unittest.TestCase):



    def test_number_repeat_maximum(self):
        self.assertEqual(romano.transformaRomano(333),"CCCXXXIII",)
        self.assertEqual(indoara.transformaIndoAra("CCCXXXIII"),333)

    def test_number_more_of_(self):

        self.assertEqual(romano.transformaRomano(62),"LXII")
        self.assertEqual(indoara.transformaIndoAra("LXII"),62)


    def test_number(self):

        self.assertEqual(romano.transformaRomano(90),"XC")
        self.assertEqual(indoara.transformaIndoAra("XC"),90)


