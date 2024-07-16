import argparse


def get_text():
    program_name = "Caesar cipher encrypt/decrypt"
    parser = argparse.ArgumentParser(prog=program_name, description="Encryption and decryption using the Caesar cipher")
    parser.add_argument("-e", "--encrypt",  type=str, dest="message_encrypt", help="Specify a value for encryption")
    parser.add_argument("-d", "--decrypt",  type=str, dest="message_decrypt", help="Specify a value for decryption")
    parser.add_argument("-s", "--shift",  type=int, dest="shift", help="Specify a shift value")
    args = parser.parse_args()
    return args


def caesar(text, shift_value):
    list_value = []
    result = ""
    for element in text:
        if element.isalpha():
            if element.isupper():
                first_value = 65  # ASCII offset for uppercase letters
                ascii_value = ord(element)  # Convert letter to its corresponding ASCII value
                index_value = ascii_value - first_value  # Get the index of the letter in the alphabet (0-25)
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value  # shift operation
                result += chr(shifted_value_each_element)  # Convert the shifted value back to a letter
            elif element.islower():
                first_value = 97  # ASCII offset for lowercase letters
                ascii_value = ord(element)
                index_value = ascii_value - first_value
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value
                result += chr(shifted_value_each_element)
        else:
            result += element  # Append non-alphabet characters unchanged
    return result


def main():
    args = get_text()
    if args.message_decrypt:
        if args.shift is not None:
            decrypted_message = caesar(args.message_decrypt, -args.shift)  # Decryption
            print(decrypted_message)
        else:
            print("\nSpecify a SHIFT_PARAMETER for decryption, use --help to see help message")
    elif args.message_encrypt:
        if args.shift is not None:
            encrypted_message = caesar(args.message_encrypt, args.shift)  # Encryption
            print(encrypted_message)
        else:
            print("\nSpecify a SHIFT_PARAMETER for encryption, use --help to see help message")
    else:
        print("Specify an argument, use --help to see help message")


if __name__ == "__main__":
    main()
