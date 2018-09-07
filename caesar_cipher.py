import string

from ciphers import Cipher


class Caesar(Cipher):
    plaintext = string.ascii_uppercase  # uppercase letters in the English alphabet
    alphabet_size = len(plaintext)

    def __init__(self, key=3):
        """Create an instance of Caesar().

        Keyword Argument:
        key -- integer, value used for the shift (default 3)

        If the key is 0, raise a ValueError and alert the user that the message will not be encrypted if the shift is 0.
        Assign key to self.key.
        """
        if key == 0:
            raise ValueError("Message will not be encrypted when the shift is 0")
        self.key = key

    def encrypt(self, message):
        """Return a string containing an encrypted message.

        Parameter:
        message -- string, the text to be encrypted

        Convert the message to its uppercase equivalent
        For each character in the message, try to find the index of that character in the alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Get the index of the encrypted letter by adding the key to the index of the plain letter and finding the
        remainder after division by the size of the alphabet.
        Use this index to look up the encrypted letter in the alphabet and append it to the output string.
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
                encrypted_message += self.plaintext[(index + self.key) % self.alphabet_size]
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Return a string containing a decrypted message.

        Parameter:
        encrypted_message -- string, the text to be decrypted

        Convert the encrypted message to its uppercase equivalent
        For each character in the encrypted message, try to find the index of that character in the alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Get the index of the decrypted letter by adding the key to the index of the encrypted letter and
        finding the remainder after division by the size of the alphabet.
        Use this index to look up the decrypted letter in the alphabet and append it to the output string.
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
                decrypted_message += self.plaintext[(index - self.key) % self.alphabet_size]
        return decrypted_message
