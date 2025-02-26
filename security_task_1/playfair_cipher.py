!pip install ordered-set
from ctypes import c_short
from ordered_set import OrderedSet
import re

class PlayfairCipher:
    def __init__(self, key):
        self.key_matrix = self.generate_key_matrix(key)

    # Generates the 5x5 key matrix for Playfair Cipher
    def generate_key_matrix(self, key):
        used = OrderedSet()
        key = key.upper()
        key = re.sub("[^A-Z]", "", key)
        key = key.replace("J", "I")
        for c in key:
            used.add(c)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for c in alphabet:
            if c != 'J':
                used.add(c)

        matrix = [['' for _ in range(5)] for _ in range(5)]
        it = iter(used)
        for i in range(0, 5):
            for j in range(0, 5):
                matrix[i][j] = next(it)
        return matrix

    # Prepares the text by removing invalid characters, replacing 'J' with 'I', and ensuring even length
    def prepare_text(self, text):
        text = text.upper()
        text = re.sub("[^A-Z]", "", text)
        text = text.replace("J", "I")
        sb = ""

        for i in range(0, len(text)):
            sb += text[i]
            # Insert 'X' if two consecutive letters are the same
            if i < len(text) - 1 and text[i] == text[i+1] and text[i] != 'X':
                sb += 'X'

        # Ensure even length
        if len(sb) % 2 != 0:
            sb += 'X'

        return sb

    # TODO: Implement this method to find the position of a character in the key matrix
    def find_position(self, c):
        # Students should complete this part
        return None

    # Encrypts the given plaintext using the Playfair cipher algorithm
    def encrypt(self, text):
        text = self.prepare_text(text)

        encrypted_text = ""

        for i in range(0, len(text), 2):
            pos1 = self.find_position(text[i])
            pos2 = self.find_position(text[i+1])
            if pos1 == None or pos2 == None: # Safety check
                continue

            if pos1[0] == pos2[0]: # Same row
                encrypted_text += self.key_matrix[pos1[0]][(pos1[1] + 1) % 5]
                encrypted_text += self.key_matrix[pos2[0]][(pos2[1] + 1) % 5]
            elif pos1[1] == pos2[1]: # Same column
                encrypted_text += self.key_matrix[(pos1[0] + 1) % 5][pos1[1]]
                encrypted_text += self.key_matrix[(pos2[0] + 1) % 5][pos2[1]]
            else: # Rectangle swap
                encrypted_text += self.key_matrix[pos1[0]][pos2[1]]
                encrypted_text += self.key_matrix[pos2[0]][pos1[1]]

        return encrypted_text

    # TODO: Implement this method to decrypt the ciphertext back to plaintext
    def decrypt(self, text):
        # Students should complete this part
        return plain_text
