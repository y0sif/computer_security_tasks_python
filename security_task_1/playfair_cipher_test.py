import unittest
from playfair_cipher import *

class TestPlayfairCipher(unittest.TestCase):
    def test_encryption(self):
        cipher = PlayfairCipher("KEYWORD")
        assert "GYIZSCOKCFBU" == cipher.encrypt("HELLO WORLD")
        
    def test_decryption(self):
        cipher = PlayfairCipher("KEYWORD")
        assert "HELLOWORLD" == cipher.decrypt("GYIZSCOKCFBU")
        
    def test_different_key(self):
        cipher = PlayfairCipher("SECRET")
        assert "HELLOWORLD" == cipher.decrypt("GATLMZCLRQX")

if __name__ == '__main__':
    unittest.main()