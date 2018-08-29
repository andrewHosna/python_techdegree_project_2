from affine_cipher import Affine


class Atbash(Affine):
    def __init__(self):
        super().__init__(var_a=1, var_b=1)

    def encryption_function(self, index):
        return (-((self.var_a * index) + self.key_b)) % self.alphabet_size

    def decryption_function(self, index):
        return self.encryption_function(index)
