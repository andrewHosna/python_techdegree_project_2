import string

from ciphers import Cipher


class Keyword(Cipher):
    plaintext = string.ascii_uppercase  # uppercase letters in the English alphabet

    def __init__(self, key_word=""):
        """Create an instance of Keyword().

        Keyword argument:
        key_word -- string, keyword used to map the plain alphabet to the cipher alphabet

        Pass the key_word to the is_plaintext_letter() function.
        If the key_word is a string of letters in the alphabet, then assign key_word to self.key_word.
        Generate the cipher alphabet and assign to self.ciphertext.
        """
        if self.is_plaintext_letter(key_word):
            self.key_word = key_word.upper()
        self.ciphertext = self.generate_ciphertext()

    def is_plaintext_letter(self, text):
        """Raise a ValueError if a single character is not in an alphabet or return true otherwise.

        Parameter:
        text -- string, text to be analyzed

        Iterate over the text and raise a ValueError if the uppercase version of any character in the text cannot be
        found in the alphabet. Alert the user that the keyword can only contain letters from the alphabet.
        Return true otherwise.
        """
        for char in text:
            if char.upper() not in self.plaintext:
                raise ValueError("Keyword can only contain the following letters: {}".format(self.plaintext))
        return True

    def generate_ciphertext(self):
        """Return a string containing a cipher alphabet, an alphabet where the letters are reordered with unique
        letters from a keyword appearing at the beginning of the alphabet.

        Initialize ciphertext as an empty string.
        Iterate over the characters in the key_word concatenated with the plaintext.
        If a character is not in the ciphertext, append the character.
        Return the ciphertext.
        """
        ciphertext = ""
        for char in self.key_word + self.plaintext:
            if char not in ciphertext:
                ciphertext += char
        return ciphertext

    def encrypt(self, message):
        """Return a string containing an encrypted message.

        Parameter:
        message -- string, the text to be encrypted

        Convert the message to its uppercase equivalent.
        For each character in the message, try to find the index of that character in the plain alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Use the index to look up the character at that position in the cipher alphabet and append it to the
        output string.
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
                encrypted_message += self.ciphertext[index]
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Return a string containing a decrypted message.

        Parameter:
        encrypted_message -- string, the text to be decrypted

        Convert the encrypted message to its uppercase equivalent.
        For each character in the encrypted message, try to find the index of that character in the cipher alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Use the index to look up the character at that position in the plain alphabet and append it to the
        output string.
        Return a string containing the decrypted message.
        """
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
