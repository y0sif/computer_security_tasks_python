import unittest
from elgamal import ElGamal

class TestElGamal(unittest.TestCase):
    def test_el_gamal_enc1(self):
        algorithm = ElGamal()
        cipher = algorithm.encrypt(7187, 4842, 4464, 19, 19)  # privateKey = 191
        self.assertEqual(2781, cipher[0])
        self.assertEqual(437, cipher[1])
    
    def test_el_gamal_enc2(self):
        algorithm = ElGamal()
        cipher = algorithm.encrypt(6323, 4736, 2231, 58, 111)  # privateKey = 118
        self.assertEqual(6066, cipher[0])
        self.assertEqual(899, cipher[1])
    
    def test_el_gamal_dec1(self):
        algorithm = ElGamal()
        plain = algorithm.decrypt(2781, 437, 191, 7187)
        self.assertEqual(19, plain)
    
    def test_el_gamal_dec2(self):
        algorithm = ElGamal()
        plain = algorithm.decrypt(6066, 899, 118, 6323)
        self.assertEqual(111, plain)

if __name__ == '__main__':
    unittest.main()