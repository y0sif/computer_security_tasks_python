import math

class ColumnarCipher:
    
    def analyse(self, plain_text, cipher_text):
        # TODO: Analyze the plainText and cipherText to determine the key(s)
        return []  # Placeholder return
    
    def decrypt(self, cipher_text, key):
        cipher_size = len(cipher_text)
        rows = math.ceil(cipher_size / len(key))
        # list comprehension to create a 2D grid
        # Initialize the grid with empty characters
        grid = [['' for _ in range(len(key))] for _ in range(rows)]
        count = 0
        
        key_map = {}
        for i in range(len(key)):
            key_map[key[i] - 1] = i
        
        remaining_cols = cipher_size % len(key)
        for i in range(len(key)):
            for j in range(rows):
                if remaining_cols != 0 and j == rows - 1 and key_map.get(i) >= remaining_cols:
                    continue
                grid[j][key_map.get(i)] = cipher_text[count]
                count += 1
        
        result = ""
        for i in range(rows):
            for j in range(len(key)):
                result += grid[i][j]
        
        return result.upper().strip()
    
    def encrypt(self, plain_text, key):
        pt_size = len(plain_text)
        rows = math.ceil(pt_size / len(key))
        grid = [['' for _ in range(len(key))] for _ in range(rows)]
        count = 0
        
        for i in range(rows):
            for j in range(len(key)):
                if count >= pt_size:
                    grid[i][j] = 'x'
                else:
                    grid[i][j] = plain_text[count]
                    count += 1
        
        key_map = {}
        for i in range(len(key)):
            key_map[key[i] - 1] = i
        
        cipher_text = ""
        for i in range(len(key)):
            for j in range(rows):
                cipher_text += grid[j][key_map.get(i)].upper()
        
        return cipher_text