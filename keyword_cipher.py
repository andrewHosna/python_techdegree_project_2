import string

from ciphers import Cipher


class Keyword(Cipher):
    plaintext = string.ascii_uppercase

    def __init__(self, key_word=""):
        if self.is_plaintext_letter(key_word):
            self.key_word = key_word.upper()
        self.ciphertext = self.generate_ciphertext()

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

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ""
        for char in message:
            try:
                index = self.plaintext.index(char)
            except ValueError:
                encrypted_message += char
            else:
                encrypted_message += self.ciphertext[index]
        return encrypted_message

    def decrypt(self, encrypted_message):
        encrypted_message = encrypted_message.upper()
        decrypted_message = ""
        for char in encrypted_message:
            try:
                index = self.ciphertext.index(char)
            except ValueError:
                decrypted_message += char
            else:
                decrypted_message += self.plaintext[index]
        return decrypted_message
