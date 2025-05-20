import unittest
from rsa import RSA

class TestRSA(unittest.TestCase):
    def test_enc1(self):
        algorithm = RSA()
        cipher = algorithm.encrypt(11, 17, 88, 7)
        self.assertEqual(11, cipher)
    
    def test_dec1(self):
        algorithm = RSA()
        plain = algorithm.decrypt(11, 17, 11, 7)
        self.assertEqual(88, plain)
    
    def test_enc2(self):
        algorithm = RSA()
        cipher = algorithm.encrypt(13, 19, 65, 5)
        self.assertEqual(221, cipher)
    
    def test_dec2(self):
        algorithm = RSA()
        plain = algorithm.decrypt(13, 19, 221, 5)
        self.assertEqual(65, plain)
    
    def test_enc3(self):
        algorithm = RSA()
        cipher = algorithm.encrypt(61, 53, 70, 7)
        self.assertEqual(2338, cipher)
    
    def test_dec3(self):
        algorithm = RSA()
        plain = algorithm.decrypt(61, 53, 2338, 7)
        self.assertEqual(70, plain)
    
    def test_new_enc(self):
        algorithm = RSA()
        cipher = algorithm.encrypt(257, 337, 18537, 17)
        self.assertEqual(12448, cipher)
    
    def test_new_dec4(self):
        algorithm = RSA()
        plain = algorithm.decrypt(257, 337, 12448, 17)
        self.assertEqual(18537, plain)

if __name__ == '__main__':
    unittest.main()