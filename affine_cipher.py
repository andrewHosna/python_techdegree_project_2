from ciphers import Cipher


class Affine(Cipher):
    plaintext = Cipher.ALPHABET
    alphabet_size = len(plaintext)
    COPRIMES = (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)

    def __init__(self, var_a=5, var_b=8):
        if var_a not in self.COPRIMES:
            raise ValueError("Key a must be one of the following values: {}".format(self.COPRIMES))
        if var_a == 1 and var_b % self.alphabet_size == 0:
            raise ValueError("Key b cannot be a multiple of {} when key a equals 1".format(self.alphabet_size))
        self.var_a = var_a
        self.key_b = var_b
        self.inverse_var_a = self.calculate_inverse_var_a()

    def calculate_inverse_var_a(self):
        for index in range(self.alphabet_size):
            if (self.var_a * index) % self.alphabet_size == 1:
                return index

    def encryption_function(self, index):
        return ((self.var_a * index) + self.key_b) % self.alphabet_size

    def decryption_function(self, index):
        return (self.inverse_var_a * (index - self.key_b)) % self.alphabet_size

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ""
        for char in message:
            try:
                index = self.plaintext.index(char)
            except ValueError:
                encrypted_message += char
            else:
                encrypted_message += self.plaintext[self.encryption_function(index)]
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
                decrypted_message += self.plaintext[self.decryption_function(index)]
        return decrypted_message
