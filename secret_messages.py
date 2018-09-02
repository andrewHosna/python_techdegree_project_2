from affine_cipher import Affine
from atbash_cipher import Atbash
from caesar_cipher import Caesar
from keyword_cipher import Keyword
from polybius_square_cipher import PolybiusSquare


def get_cipher():
    """Ask user to select an available cipher and return the input in lowercase."""
    return input("""
Available ciphers:
 
  1. Affine
  2. Atbash
  3. Caesar
  4. Keyword
  5. Polybius Square

Select a cipher...
-> """).lower()


def get_message():
    """Ask user for a message and return the input."""
    return input("""
Enter a message...
-> """)


def get_option():
    """Ask user to select an option and return the input in lowercase."""
    return input("""
Options:
 
  1. Encrypt
  2. Decrypt

Select an option...
-> """).lower()


def affine_controller():
    """Use the affine cipher.

    Get a message and an option from the user.
    Enter a while loop.
    Ask user for keys a and b until integer values are provided.
    Try to create an instance of Affine() with keys a and b until valid values of keys a and b are provided.
    If the option is '1' or 'encrypt' then print the encrypted message.
    If the option is '2' or 'decrypt' then print the decrypted message.
    Break out of loop.
    """
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
                affine = Affine(key_a=key_a, key_b=key_b)
            except ValueError as error:
                print(error)
            else:
                if option == '1' or option == 'encrypt':
                    print("->", affine.encrypt(message))
                elif option == '2' or option == 'decrypt':
                    print("->", affine.decrypt(message))
                break


def atbash_controller():
    """Use the atbash cipher.

    Get a message and an option from the user.
    Create an instance of Atbash().
    If the option is '1' or 'encrypt' then print the encrypted message.
    If the option is '2' or 'decrypt' then print the decrypted message.
    """
    message = get_message()
    option = get_option()

    atbash = Atbash()
    if option == '1' or option == 'encrypt':
        print("->", atbash.encrypt(message))
    elif option == '2' or option == 'decrypt':
        print("->", atbash.decrypt(message))


def caesar_controller():
    """Use the caesar cipher.

    Get a message and an option from the user.
    Enter a while loop.
    Ask user for shift until an integer value is provided.
    Try to create an instance of Caesar() with shift until a valid value of shift is provided.
    If the option is '1' or 'encrypt' then print the encrypted message.
    If the option is '2' or 'decrypt' then print the decrypted message.
    Break out of loop.
    """
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
                caesar = Caesar(key=shift)
            except ValueError as error:
                print(error)
            else:
                if option == '1' or option == 'encrypt':
                    print("->", caesar.encrypt(message))
                elif option == '2' or option == 'decrypt':
                    print("->", caesar.decrypt(message))
                break


def keyword_controller():
    """Use the keyword cipher.

    Get a message and an option from the user.
    Enter a while loop.
    Ask user for a keyword.
    Try to create an instance of Keyword() with key_word until a valid keyword is provided.
    If the option is '1' or 'encrypt' then print the encrypted message.
    If the option is '2' or 'decrypt' then print the decrypted message.
    Break out of loop.
    """
    message = get_message()
    option = get_option()

    while True:
        key_word = input("Enter a keyword...\n-> ")
        try:
            keyword = Keyword(key_word=key_word)
        except ValueError as error:
            print(error)
        else:
            if option == '1' or option == 'encrypt':
                print("->", keyword.encrypt(message))
            elif option == '2' or option == 'decrypt':
                print("->", keyword.decrypt(message))
            break


def polybius_square_controller():
    """Use the polybius square cipher.

    Get a message and an option from the user.
    Enter a while loop.
    Ask user for a keyword.
    Try to create an instance of PolybiusSquare() with key_word until a valid keyword is provided.
    If the option is '1' or 'encrypt' then print the encrypted message.
    If the option is '2' or 'decrypt' then print the decrypted message.
    Break out of loop.
    """
    message = get_message()
    option = get_option()

    while True:
        key_word = ""
        if input("Use keyword?... (yes/no)\n-> ") == "yes":
            key_word = input("Enter a keyword...\n-> ")
        try:
            polybius_square = PolybiusSquare(key_word=key_word)
        except ValueError as error:
            print(error)
        else:
            if option == '1' or option == 'encrypt':
                print("->", polybius_square.encrypt(message))
            elif option == '2' or option == 'decrypt':
                print("->", polybius_square.decrypt(message))
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
        elif cipher == '5' or cipher == 'polybius square':
            polybius_square_controller()
        else:
            print("\nYou did not select an available cipher")

        if input("\nContinue?... (yes/no)\n-> ") == "no":
            exit()
