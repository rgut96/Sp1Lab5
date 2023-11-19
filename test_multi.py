import unittest
from multi import multi

class TestMulti(unittest.TestCase):
 
 def test_multi(self):
  self.assertEqual(multi(3, 2), 6)
  self.assertEqual(multi(-1, 1), -1)
  self.assertEqual(multi(-1, -1), -1)

if __name__ == '__main__':
 unittest.main()