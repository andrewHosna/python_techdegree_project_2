class Cipher:
    def encrypt(self, message):
        """Raise NotImplementedError if encrypt method not implemented in any class inheriting from Cipher"""
        raise NotImplementedError()

    def decrypt(self, encrypted_message):
        """Raise MptImplementedError if decrypt not implemented in any class inheriting from Cipher"""
        raise NotImplementedError()
