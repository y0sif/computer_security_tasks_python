# TODO: Implement this method to generate a substitution map from A-Z using the provided key
def generate_endcyption_map(key):
    encryption_map = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()

    # Students should complete this loop
    for i in range(0, len(alphabet)):
        # encryptionMap // Hint: Map plaintext letter to cipher letter
        pass
    return encryption_map

def generate_dectyption_map(key):
    decryption_map = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()

    # Students should complete this loop
    for i in range(0, len(alphabet)):
        # encryptionMap // Hint: Map plaintext letter to cipher letter
        pass
    return decryption_map


def encrypt(plaintext, key):
    encryption_map = {}
    plaintext = plaintext.upper()
    encrypted_text = ""

    for c in plaintext:
        # TODO: Use the encryption map to convert each letter
        pass

    return encrypted_text


def decrypt(plaintext, key):
    decryption_map = {}
    plaintext = plaintext.upper()
    decrypted_text = ""

    for c in plaintext:
        # TODO: Use the encryption map to convert each letter
        pass

    return decrypted_text


def find_key(plaintext, ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_map = [' ' for _ in range(0, 26)]

    plaintext = plaintext.upper()
    ciphertext = ciphertext.upper()

    for i in range(0, len(plaintext)):
        plain_char = plaintext[i]
        cipher_char = ciphertext[i]
        if plain_char.isalpha():
            index = alphabet.index(plain_char)
            # TODO: Ensure each letter is mapped only once
    return ''.join(key_map)

