from affine_cipher import Affine


class Atbash(Affine):
    def __init__(self):
        """Create an instance of Atbash(), a special case of the Affine Cipher where keys a and b both equal 1."""
        super().__init__(key_a=1, key_b=1)

    def encryption_function(self, index):
        """Return an index for a letter in an alphabet based on the following function:
            -((key_a * index) + key_b) mod alphabet_size

        Parameter:
        index -- integer, the index of a letter in a string containing an alphabet
        """
        return (-((self.key_a * index) + self.key_b)) % self.alphabet_size

    def decryption_function(self, index):
        """Return the result of the encryption function with an index for a letter in an alphabet as the argument.

        Parameter:
        index -- integer, the index of a letter in a string containing an alphabet

        The decryption function for an Atbash cipher is equal to the encryption function.
        """
        return self.encryption_function(index)
