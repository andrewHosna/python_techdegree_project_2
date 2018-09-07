import string

from ciphers import Cipher


class Affine(Cipher):
    plaintext = string.ascii_uppercase  # uppercase letters in the English alphabet
    alphabet_size = len(plaintext)
    COPRIMES = (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)  # list of numbers coprime with 26, the size of the alphabet

    def __init__(self, key_a=5, key_b=8):
        """Create an instance of Affine().

        Keyword arguments:
        key_a -- integer, variable a for use in the encryption/decryption functions (default 5)
        key_b -- integer, variable b for use in the encryption/decryption functions (default 8)

        If key a is not in the list COPRIMES, raise a ValueError and alert the user that key a must be chosen from
        that list.
        If key a is 1 and key b is a multiple of 26, raise a ValueError and alert the user that key b cannot be a
        multiple of 26 in this case.
        Assign key_a to self.key_a.
        Assign key_b to self.key_b.
        Calculate the modular multiplicative inverse of key_a mod alphabet_size and assign to self.inverse_key_a
        """
        if key_a not in self.COPRIMES:
            raise ValueError("Key a must be one of the following values: {}".format(self.COPRIMES))
        if key_a == 1 and key_b % self.alphabet_size == 0:
            raise ValueError("Key b cannot be a multiple of {} when key a equals 1".format(self.alphabet_size))
        self.key_a = key_a
        self.key_b = key_b
        self.inverse_key_a = self.calculate_inverse_key_a()

    def calculate_inverse_key_a(self):
        """Calculate the modular multiplicative inverse of key_a mod alphabet_size and return this value.

        Iterate over numbers from 0 to alphabet_size.
        Return a value for inverse_key_a once the following equation is satisfied:
            (key_a * inverse_key_a) mod alphabet_size = 1
        """
        for index in range(self.alphabet_size):
            if (self.key_a * index) % self.alphabet_size == 1:
                return index

    def encryption_function(self, index):
        """Return an index for a letter in an alphabet based on the following function:
            ((key_a * index) + key_b) mod alphabet_size

        Parameter:
        index -- integer, the index of a letter in a string containing an alphabet
        """
        return ((self.key_a * index) + self.key_b) % self.alphabet_size

    def decryption_function(self, index):
        """Return an index for a letter in an alphabet based on the following function:
            (inverse_key_a * (index - key_b)) mod alphabet_size

        Parameter:
        index -- integer, the index of a letter in a string containing an alphabet
        """
        return (self.inverse_key_a * (index - self.key_b)) % self.alphabet_size

    def encrypt(self, message):
        """Return a string containing an encrypted message

        Parameter:
        message -- string, the text to be encrypted

        Convert the message to its uppercase equivalent.
        For each character in the message, try to find the index of that character in the alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Pass the index of the character to the encryption function and get back the index of the encrypted letter.
        Use the returned index to look up the encrypted letter in the alphabet and append to the output string.
        Return a string containing the encrypted message.
        """
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
        """Return a string containing a decrypted message

        Parameter:
        encrypted_message -- string, the text to be decrypted

        Convert the encrypted message to its uppercase equivalent.
        For each character in the encrypted message, try to find the index of that character in the alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Pass the index to the decryption function and get back the index of the decrypted letter.
        Use the returned index to look up the decrypted letter in the alphabet and append to the output string.
        Return a string containing the decrypted message.
        """
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
