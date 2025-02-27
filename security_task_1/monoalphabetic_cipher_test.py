import re
import unittest
from monoalphabetic_cipher import *

class TestMonoalphabeticCipher(unittest.TestCase):
    def test_encryption(self):
        key = "QWERTYUIOPASDFGHJKLZXCVBNM"
        plaintext = "HELLO WORLD"
        expected_cipher_text = "ITSSG VGKSR"

        actual_cipher_text = encrypt(plaintext, key)
        assert expected_cipher_text == actual_cipher_text

    def test_decryption(self):
        key = "QWERTYUIOPASDFGHJKLZXCVBNM"
        cipher_text = "ITSSG VGKSR"
        expected_plain_text = "HELLO WORLD"

        actual_plain_text = decrypt(cipher_text, key)
        assert expected_plain_text == actual_plain_text

    def test_find_key(self):
        main_plain = "meetmeafterthetogaparty".upper()
        main_cipher = "phhwphdiwhuwkhwrjdsduwb".upper()
        expected_pattern = "d.{3}hijk.{4}p.rs.u.w.{4}b.".upper()
        key = find_key(main_plain, main_cipher)

        # Validate key format against expected pattern
        assert re.match(expected_pattern, key), "Key does not match expected pattern."

if __name__ == '__main__':
    unittest.main()