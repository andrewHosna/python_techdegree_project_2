from affine_cipher import Affine


class Atbash(Affine):
    def __init__(self):
        super().__init__(key_a=1, key_b=1)

    def encryption_function(self, index):
        return (-((self.key_a * index) + self.key_b)) % self.alphabet_size

    def decryption_function(self, index):
        return self.encryption_function(index)
