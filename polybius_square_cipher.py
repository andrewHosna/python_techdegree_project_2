import string

from ciphers import Cipher


class PolybiusSquare(Cipher):
    plaintext = string.ascii_uppercase  # uppercase letters in the English alphabet
    digits = string.digits  # digits 0-9

    def __init__(self, key_word=""):
        """Create an instance of PolybiusSquare().

        Keyword argument:
        key_word -- string, keyword used to map the plain alphabet to the cipher alphabet

        Pass the key_word to the is_plaintext_letter() function.
        If the key_word is a string of letters in the alphabet, then assign key_word to self.key_word.
        Generate the cipher alphabet and assign to self.ciphertext.
        Generate the polybius square and assign to self.polybius_square.
        """
        if self.is_plaintext_letter(key_word):
            self.key_word = key_word.upper()
        self.ciphertext = self.generate_ciphertext()
        self.polybius_square = self.generate_polybius_square()

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

    def generate_polybius_square(self):
        """Return a list of two digit number strings that define coordinates in a grid.

        Initialize a list of two digit number strings that define coordinates in a grid.
        Find the indices of letters 'I' and 'J' in the cipher alphabet.
        If 'I' comes before 'J' in the cipher alphabet, insert the coordinate of 'I' at the index of 'J'
        If 'I' comes after 'J' in the cipher alphabet, swap 'J' and the letter directly after 'I' in the cipher alphabet
        before inserting the coordinate of 'I' at the new index of 'J.'
        Return the polybius square.
        """
        polybius_square = [str(x+y) for x in range(10, 60, 10) for y in range(1, 6)]
        index_i, index_j = self.ciphertext.index("I"), self.ciphertext.index("J")

        # Letters 'I' and 'J' share a coordinate in this polybius square.
        # To account for messages containing the letter 'J,' the coordinates of 'I' must be duplicated so that both our
        # cipher alphabet and polybius square have 26 items.
        # 'J' must come after 'I' so that any 'J' in a plain message is encrypted to 'I,' as the index() method will
        # return the index of the first matching value found.
        if index_i < index_j:
            polybius_square.insert(index_j, polybius_square[index_i])
        else:
            temp_list = list(self.ciphertext)
            # swap 'J' and the letter directly after 'I' in the cipher alphabet
            temp_list[index_j], temp_list[index_i+1] = temp_list[index_i+1], "J"
            self.ciphertext = "".join(temp_list)
            polybius_square.insert(index_i+1, polybius_square[index_i])
        return polybius_square

    def encrypt(self, message):
        """Returns a string containing a containing an encrypted message.

        Parameter:
        message -- string, the text to be encrypted

        Convert the message to its uppercase equivalent.
        For each character in the message, try to find the index of that character in the cipher alphabet.
        If the character could not be found in the alphabet, handle the ValueError by appending the character to the
        output string.
        Use the index to look up the two digit number string at that position in the polybius square and append it to
        the output string.
        Return a string containing the encrypted message.
        """
        message = message.upper()
        encrypted_message = ""
        for char in message:
            try:
                index = self.ciphertext.index(char)
            except ValueError:
                encrypted_message += char
            else:
                encrypted_message += self.polybius_square[index]
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Return a string containing a decrypted message.

        Parameter:
        encrypted_message -- string, the text to be decrypted

        Convert the encrypted message to its uppercase equivalent.
        Declare a list to use as a queue to process the two digit number strings expected in the encrypted message.
        Iterate over each character in the encrypted message.
        If the character is a digit, then append it to the queue. Else append it to the output string.
        If there are two digits in the queue, pop the first element and the remaining element, concatenate to form the
        correct two digit coordinate string, and look up the index of that coordinate in the polybius square.
        Use the index to look up the character at that position in the cipher alphabet and append it to the
        output string.
        Return a string containing the decrypted message.
        """
        encrypted_message = encrypted_message.upper()
        decrypted_message = ""
        digit_queue = []
        for char in encrypted_message:
            if char in self.digits:
                digit_queue.append(char)
            else:
                decrypted_message += char
            if len(digit_queue) == 2:
                # Pop the first element in the queue to get the first number in the two digit coordinate string
                # Pop the remaining element in the queue to get the second number in the two digit coordinate string
                # and clear the queue
                index = self.polybius_square.index(digit_queue.pop(0)+digit_queue.pop())
                decrypted_message += self.ciphertext[index]
        return decrypted_message
