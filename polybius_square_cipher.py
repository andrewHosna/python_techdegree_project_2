import string

from ciphers import Cipher


class PolybiusSquare(Cipher):
    plaintext = string.ascii_uppercase
    digits = string.digits

    def __init__(self, key_word=""):
        if self.is_plaintext_letter(key_word):
            self.key_word = key_word.upper()
        self.ciphertext = self.generate_ciphertext()
        self.polybius_square = self.generate_polybius_square()

    def is_plaintext_letter(self, text):
        for char in text:
            if char.upper() not in self.plaintext:
                raise ValueError("Keyword can only contain the following letters: {}".format(self.plaintext))
        return True

    def generate_ciphertext(self):
        ciphertext = ""
        for char in self.key_word + self.plaintext:
            if char not in ciphertext:
                ciphertext += char
        return ciphertext

    def generate_polybius_square(self):
        polybius_square = [str(x+y) for x in range(10, 60, 10) for y in range(1, 6)]
        index_i, index_j = self.ciphertext.index("I"), self.ciphertext.index("J")

        if index_i < index_j:
            polybius_square.insert(index_j, polybius_square[index_i])
        else:
            temp_list = list(self.ciphertext)
            temp_list[index_j], temp_list[index_i+1] = temp_list[index_i+1], "J"
            self.ciphertext = "".join(temp_list)
            polybius_square.insert(index_i+1, polybius_square[index_i])
        return polybius_square

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ""
        for char in message:
            try:
                index = self.ciphertext.index(char)
            except ValueError:
                encrypted_message += char
            else:
                encrypted_message += self.polybius_square[index]
        return "".join(encrypted_message)

    def decrypt(self, encrypted_message):
        encrypted_message = encrypted_message.upper()
        decrypted_message = ""
        digit_queue = []
        for char in encrypted_message:
            if char in self.digits:
                digit_queue.append(char)
            else:
                decrypted_message += char
            if len(digit_queue) == 2:
                index = self.polybius_square.index(digit_queue.pop(0)+digit_queue.pop(0))
                decrypted_message += self.ciphertext[index]
        return decrypted_message
