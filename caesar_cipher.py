import string

from ciphers import Cipher


class Caesar(Cipher):
    plaintext = string.ascii_uppercase
    alphabet_size = len(plaintext)

    def __init__(self, key=3):
        if key == 0:
            raise ValueError("Message will not be encrypted when the offset is 0")
        self.key = key

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ""
        for char in message:
            try:
                index = self.plaintext.index(char)
            except ValueError:
                encrypted_message += char
            else:
                encrypted_message += self.plaintext[(index + self.key) % self.alphabet_size]
        return encrypted_message

    def decrypt(self, encrypted_message):
        encrypted_message = encrypted_message.upper()
        decrypted_message = ""
        for char in encrypted_message:
            try:
                index = self.plaintext.index(char)
            except ValueError:
                decrypted_message += char
            else:
                decrypted_message += self.plaintext[(index - self.key) % self.alphabet_size]
        return decrypted_message
