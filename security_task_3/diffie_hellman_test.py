import unittest
from diffie_hellman import DiffieHellman

class TestDiffieHellman(unittest.TestCase):
    def test_diffie_hellman1(self):
        algorithm = DiffieHellman()
        key = algorithm.get_keys(19, 2, 6, 13)
        self.assertEqual(7, key[0])
        self.assertEqual(7, key[1])
    
    def test_diffie_hellman2(self):
        algorithm = DiffieHellman()
        key = algorithm.get_keys(353, 2, 97, 233)
        self.assertEqual(81, key[0])
        self.assertEqual(81, key[1])
    
    def test_diffie_hellman3(self):
        algorithm = DiffieHellman()
        key = algorithm.get_keys(353, 3, 97, 233)
        self.assertEqual(160, key[0])
        self.assertEqual(160, key[1])
    
    def test_diffie_hellman_new(self):
        algorithm = DiffieHellman()
        key = algorithm.get_keys(541, 10, 50, 100)
        self.assertEqual(449, key[0])
        self.assertEqual(449, key[1])

if __name__ == '__main__':
    unittest.main()