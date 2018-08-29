from ciphers import Cipher
from affine_cipher import Affine
from atbash_cipher import Atbash
from caesar_cipher import Caesar
from keyword_cipher import Keyword


if __name__ == '__main__':
    print("Welcome to Secret Messages!")
    while True:
        cipher = input("""
Available ciphers:
 
  1. Affine
  2. Atbash
  3. Caesar
  4. Keyword

Select a cipher...
-> """).lower()
        print("Encrypt or decrypt any message containing the following letters: {}".format(Cipher.ALPHABET))
        message = input("Enter a message...\n-> ")
        option = input("""Options:
 
  1. Encrypt
  2. Decrypt

Select an option...
-> """)

        if cipher == '1' or cipher == 'affine':
            while True:
                print("Default: a = 5, b = 8")
                key_a = input("Enter key a or press enter for default value...\n-> ")
                if key_a == "":
                    key_a = "5"
                key_b = input("Enter key b or press enter for default value...\n-> ")
                if key_b == "":
                    key_b = "8"
                try:
                    key_a = int(key_a)
                    key_b = int(key_b)
                except ValueError:
                    print("Please enter a whole number")
                else:
                    try:
                        affine_cipher = Affine(var_a=key_a, var_b=key_b)
                    except ValueError as err:
                        print(err)
                    else:
                        if option == '1' or option == 'encrypt':
                            print("->", affine_cipher.encrypt(message))
                        elif option == '2' or option == 'decrypt':
                            print("->", affine_cipher.decrypt(message))
                        break
        elif cipher == '2' or cipher == 'atbash':
            atbash_cipher = Atbash()
            if option == '1' or option == 'encrypt':
                print("->", atbash_cipher.encrypt(message))
            elif option == '2' or option == 'decrypt':
                print("->", atbash_cipher.decrypt(message))
        elif cipher == '3' or cipher == 'caesar':
            while True:
                print("Default: offset = 3")
                offset = input("Enter the offset or press enter for default value...\n-> ")
                if offset == "":
                    offset = "3"
                try:
                    offset = int(offset)
                except ValueError:
                    print("Please enter a whole number")
                else:
                    try:
                        caesar_cipher = Caesar()
                    except ValueError as err:
                        print(err)
                    else:
                        if option == '1' or option == 'encrypt':
                            print("->", caesar_cipher.encrypt(message))
                        elif option == '2' or option == 'decrypt':
                            print("->", caesar_cipher.decrypt(message))
                        break
        elif cipher == '4' or cipher == 'keyword':
            while True:
                key_word = input("Enter a keyword...\n-> ")
                try:
                    keyword_cipher = Keyword(key_word=key_word)
                except ValueError as err:
                    print(err)
                else:
                    if option == '1' or option == 'encrypt':
                        print("->", keyword_cipher.encrypt(message))
                    elif option == '2' or option == 'decrypt':
                        print("->", keyword_cipher.decrypt(message))
                    break
        else:
            break

        if input("Continue?... (yes/no)\n-> ") == "no":
            exit()
