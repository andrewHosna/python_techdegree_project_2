from ciphers import Cipher
from affine_cipher import Affine
from atbash_cipher import Atbash
from caesar_cipher import Caesar
from keyword_cipher import Keyword


def get_cipher():
    return input("""
Available ciphers:
 
  1. Affine
  2. Atbash
  3. Caesar
  4. Keyword

Select a cipher...
-> """).lower()


def get_message():
    return input("""
Encrypt or decrypt any message containing the following letters: {}

Enter a message...    
-> """.format(Cipher.ALPHABET))


def get_option():
    return input("""
Options:
 
  1. Encrypt
  2. Decrypt

Select an option...
-> """).lower()


def affine_controller():
    message = get_message()
    option = get_option()

    while True:
        key_a = input("Enter the first key... (Suggested value: 5)\n-> ")
        key_b = input("Enter the second key... (Suggested value: 8)\n-> ")
        try:
            key_a = int(key_a)
            key_b = int(key_b)
        except ValueError:
            print("Please enter a whole number")
        else:
            try:
                affine_cipher = Affine(key_a=key_a, key_b=key_b)
            except ValueError as error:
                print(error)
            else:
                if option == '1' or option == 'encrypt':
                    print("->", affine_cipher.encrypt(message))
                elif option == '2' or option == 'decrypt':
                    print("->", affine_cipher.decrypt(message))
                break


def atbash_controller():
    message = get_message()
    option = get_option()

    atbash_cipher = Atbash()
    if option == '1' or option == 'encrypt':
        print("->", atbash_cipher.encrypt(message))
    elif option == '2' or option == 'decrypt':
        print("->", atbash_cipher.decrypt(message))


def caesar_controller():
    message = get_message()
    option = get_option()

    while True:
        shift = input("Choose the shift... (Suggested value: 3)\n-> ")
        try:
            shift = int(shift)
        except ValueError:
            print("Please enter a whole number")
        else:
            try:
                caesar_cipher = Caesar(key=shift)
            except ValueError as error:
                print(error)
            else:
                if option == '1' or option == 'encrypt':
                    print("->", caesar_cipher.encrypt(message))
                elif option == '2' or option == 'decrypt':
                    print("->", caesar_cipher.decrypt(message))
                break


def keyword_controller():
    message = get_message()
    option = get_option()

    while True:
        key_word = input("Enter a keyword...\n-> ")
        try:
            keyword_cipher = Keyword(key_word=key_word)
        except ValueError as error:
            print(error)
        else:
            if option == '1' or option == 'encrypt':
                print("->", keyword_cipher.encrypt(message))
            elif option == '2' or option == 'decrypt':
                print("->", keyword_cipher.decrypt(message))
            break


if __name__ == '__main__':
    print("Welcome to Secret Messages!")

    while True:
        cipher = get_cipher()

        if cipher == '1' or cipher == 'affine':
            affine_controller()
        elif cipher == '2' or cipher == 'atbash':
            atbash_controller()
        elif cipher == '3' or cipher == 'caesar':
            caesar_controller()
        elif cipher == '4' or cipher == 'keyword':
            keyword_controller()
        else:
            print("\nYou did not select an available cipher")

        if input("\nContinue?... (yes/no)\n-> ") == "no":
            exit()
