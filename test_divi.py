import unittest
from divi import divi

class TestDivi(unittest.TestCase):
 
 def test_divi(self):
  self.assertEqual(divi(6, 2), 3)
  self.assertEqual(divi(-1, 1), -1)
  self.assertEqual(divi(-1, 0), "No se puede dividir por cero")

if __name__ == '__main__':
 unittest.main()