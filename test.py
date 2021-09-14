from _typeshed import Self
import unittest

class TestRomano(unittest.TestCase):



    def test_number_repeat_max(self):
        
        self.assertEqual(333,"CCCXXXIII")
        self.assertEqual("CCCXXXIII",333)

    def test_number_more_of_(self):

        self.assertEqual(62,"LXII")
        self.assertEqual("LXII",62)
    def test_number_repeat_max(self):

        self.assertEqual(90,"XC")
        self.assertEqual("XC",90)
        