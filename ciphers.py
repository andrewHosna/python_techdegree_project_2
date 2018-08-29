import string


class Cipher:
    ALPHABET = string.ascii_uppercase

    def encrypt(self, message):
        raise NotImplementedError()

    def decrypt(self, encrypted_message):
        raise NotImplementedError()
